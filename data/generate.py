"""Writes the invented tables (policies.csv, claims.csv, handlers.csv, claim_notes.csv). Deterministic: rerun it to
rebuild them byte for byte.

Every row is invented. Forms, editions and endorsements name documents in this corpus, so a row can be read
against the form it was written on; ids, names, dates, amounts and notes mean nothing outside this demo.

The claims desk (openwiki-insurance-poc, docs/specs/claims-desk/01-claims-data.md) needs claims that call for a
handler's attention, so some are seeded with an issue on purpose, each beside look-alikes that are fine. Every
issue rests on a corpus provision, located and quoted at build (`PROVISIONS`). `python3 data/generate.py --key-out
PATH` also writes the answer key; the key never lives in this repo, because the agents' sandboxes read it.

The first 40 policies and 90 claims come from the original random stream and keep every original value; the new
columns are filled from a second stream, and the new rows (P-1041..., C-5091...) are written out below.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import random
import re
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).parent
CORPUS = HERE.parent
rng = random.Random(20261020)

# ---- the original 40 policies and 90 claims: this block's draws must never change (R6) -------------------------

FORMS = {  # form -> editions in forms/<line>/MS/<form>/
    "HO-3": ["2011-05", "2018-09", "2024-03"], "HO-4": ["2013-07", "2021-10"], "HO-5": ["2015-01", "2022-06"],
    "HO-6": ["2014-04", "2023-02"], "DP-3": ["2012-11", "2020-08", "2026-01"],
}
STATES = {"MS": None, "TX": "HO-01-45", "FL": "HO-01-09"}  # state -> its amendatory endorsement (HO forms)
ENDORSEMENTS = ["HO-04-90", "HO-04-61", "HO-04-10", "HO-04-20", "HO-04-41"]
LOSSES = {"water backup": "HO-04-90", "wind": None, "hail": None, "theft": "HO-04-61", "fire": None,
          "freeze": None, "sewer": "HO-04-90"}


LAST_EFFECTIVE, LAST_LOSS = date(2026, 6, 30), date(2026, 10, 1)  # bounds of the original rows only


def money(lo: int, hi: int, step: int) -> int:
    return rng.randrange(lo, hi, step)


policies = []
for n in range(40):
    form = rng.choice(list(FORMS))
    edition = rng.choice(FORMS[form])
    state = rng.choices(list(STATES), weights=[6, 2, 2])[0]
    effective = min(date(int(edition[:4]), 1, 1) + timedelta(days=rng.randrange(0, 900)), LAST_EFFECTIVE)
    endorsements = sorted(set(rng.sample(ENDORSEMENTS, k=rng.randrange(0, 3))))
    if form != "DP-3" and STATES[state]:
        endorsements = [STATES[state], *endorsements]
    policies.append({
        "policy_id": f"P-{1001 + n}",
        "form": form,
        "form_edition": edition,
        "state": state,
        "status": rng.choices(["active", "lapsed", "cancelled"], weights=[7, 2, 1])[0],
        "effective_date": effective.isoformat(),
        "coverage_a_limit": "" if form in ("HO-4", "HO-6") else money(150_000, 650_000, 5_000),
        "deductible": rng.choice([500, 1000, 1000, 2500, 5000]),
        "endorsements": ";".join(endorsements),
    })

claims = []
for n in range(90):
    policy = rng.choice(policies)
    loss = rng.choice(list(LOSSES))
    reported = money(800, 60_000, 50)
    status = rng.choices(["open", "closed", "denied"], weights=[3, 6, 1])[0]
    if LOSSES[loss] == "HO-04-90" and "HO-04-90" not in policy["endorsements"]:
        status = "denied"  # the base forms exclude water backup; only the endorsement buys it back
    claims.append({
        "claim_id": f"C-{5001 + n}",
        "policy_id": policy["policy_id"],
        "loss_type": loss,
        "loss_date": min(date.fromisoformat(policy["effective_date"]) + timedelta(days=rng.randrange(10, 700)),
                         LAST_LOSS).isoformat(),
        "status": status,
        "reported_amount": reported,
        "paid_amount": 0 if status != "closed" else max(0, reported - int(policy["deductible"]) - money(0, 2_000, 50)),
        "endorsement_applied": LOSSES[loss] if LOSSES[loss] and LOSSES[loss] in policy["endorsements"] else "",
    })

# ---- the claims desk: new columns, rows and tables ----------------------------------------------------------------

TODAY = date(2027, 3, 2)  # the demo's today: HO 04 90 2027-01 is in force, so an edition can be misapplied
rng2 = random.Random(20270302)  # every new value; the stream above stays untouched
D = date.fromisoformat

HANDLERS = [  # authority is company data, so it lives here, not in the corpus (water-loss handling H.7.4)
    {"handler_id": "H-01", "name": "Dana Whitcombe", "role": "adjuster", "authority_usd": 5_000},
    {"handler_id": "H-02", "name": "Ravi Castellano", "role": "adjuster", "authority_usd": 15_000},
    {"handler_id": "H-03", "name": "Imogen Ashgrove", "role": "adjuster", "authority_usd": 15_000},
    {"handler_id": "H-04", "name": "Tobias Okafor", "role": "senior adjuster", "authority_usd": 50_000},
    {"handler_id": "H-05", "name": "Lena Marchetti", "role": "senior adjuster", "authority_usd": 50_000},
    {"handler_id": "H-06", "name": "Grace Abernathy", "role": "claims manager", "authority_usd": 150_000},
]
HANDLER = {h["handler_id"]: h for h in HANDLERS}

WATER_BACKUP = {"water backup", "sewer"}
WATER_LOSS = WATER_BACKUP | {"freeze"}  # water-loss handling covers freezing (H.1.35)
WIND = {"wind", "hail"}  # treated as roof losses for roof claim handling H.5.28 (their notes inspect the roof)
HO0490 = {"2010-10": {"limit": 5_000, "deductible": 500}, "2027-01": {"limit": 10_000, "deductible": 1_000}}
NUMBER = {1: "one", 2: "two", 5: "five", 10: "ten", 15: "fifteen"}
PCT_RANGE = {  # windstorm and hail deductible percentages each amendatory edition allows (its T.1 section)
    ("HO-01-45", "2019-01"): (1, 5), ("HO-01-45", "2022-01"): (1, 10),
    ("HO-01-09", "2019-01"): (2, 10), ("HO-01-09", "2023-07"): (2, 15),
}


def endorsement_dir(code: str) -> Path:
    state = {"HO-01-45": "TX", "HO-01-09": "FL"}.get(code, "MS")
    return CORPUS / "forms" / "HO" / state / code


def edition_in_force(code: str, effective: date) -> str:
    """The latest edition effective on or before the policy's effective date; the earliest in the corpus when the
    policy predates them all."""
    editions = sorted(p.stem for p in endorsement_dir(code).glob("*.md"))
    assert editions, f"no editions of {code} in the corpus"
    in_force = [e for e in editions if D(f"{e}-01") <= effective]
    return in_force[-1] if in_force else editions[0]


def round50(x: float) -> int:
    return int(x // 50 * 50)


def business_days(start: date, end: date) -> int:
    """Weekdays after `start` up to and including `end` (the corpus defines no holidays)."""
    return sum(1 for i in range(1, (end - start).days + 1) if (start + timedelta(days=i)).weekday() < 5)


def add_business_days(start: date, n: int) -> date:
    day = start
    while n:
        day += timedelta(days=1)
        n -= day.weekday() < 5
    return day


# ---- new policies (P-1041...): written for the seeded issues -------------------------------------------------------
# P-1042 and P-1048 took effect in January 2027, so they carry HO 04 90 2027-01; every other policy is on 2010-10.

NEW_POLICIES = [  # policy_id, form, form_edition, state, effective_date, coverage_a_limit, deductible, endorsements, wind %
    ("P-1041", "HO-3", "2024-03", "MS", "2026-04-01", 420_000, 2_500, "HO-04-90", ""),
    ("P-1042", "HO-5", "2022-06", "MS", "2027-01-08", 510_000, 2_500, "HO-04-90", ""),
    ("P-1043", "HO-3", "2024-03", "TX", "2025-09-01", 380_000, 1_000, "HO-01-45;HO-04-90", 2),
    ("P-1044", "HO-3", "2018-09", "TX", "2021-05-10", 300_000, 2_500, "HO-01-45", 1),
    ("P-1045", "HO-3", "2024-03", "FL", "2026-02-01", 450_000, 1_000, "HO-01-09;HO-04-90", 2),
    ("P-1046", "HO-5", "2022-06", "FL", "2024-06-01", 520_000, 2_500, "HO-01-09;HO-04-10", 5),
    ("P-1047", "HO-6", "2023-02", "MS", "2026-08-01", "", 500, "HO-04-90", ""),
    ("P-1048", "HO-3", "2024-03", "MS", "2027-01-20", 360_000, 1_000, "HO-04-61;HO-04-90", ""),
    ("P-1049", "DP-3", "2026-01", "TX", "2026-03-01", 350_000, 1_000, "", ""),
    ("P-1050", "HO-4", "2021-10", "FL", "2025-11-01", "", 1_000, "HO-01-09", ""),
]
for pid, form, edition, state, effective, cov_a, deductible, endorsements, pct in NEW_POLICIES:
    policies.append({"policy_id": pid, "form": form, "form_edition": edition, "state": state, "status": "active",
                     "effective_date": effective, "coverage_a_limit": cov_a, "deductible": deductible,
                     "endorsements": endorsements, "windstorm_deductible_pct": pct})

for p in policies:  # the new policy columns
    codes = [e for e in p["endorsements"].split(";") if e]
    p["endorsement_editions"] = ";".join(f"{c}@{edition_in_force(c, D(p['effective_date']))}" for c in codes)
    if "windstorm_deductible_pct" not in p:  # TX and FL policies with a Coverage A limit for the % to apply to
        amendatory = STATES[p["state"]]
        if amendatory in codes and p["coverage_a_limit"] != "":
            lo, hi = PCT_RANGE[(amendatory, edition_in_force(amendatory, D(p["effective_date"])))]
            p["windstorm_deductible_pct"] = rng2.choice([x for x in (1, 2, 5) if lo <= x <= hi])
        else:
            p["windstorm_deductible_pct"] = ""
POLICY = {p["policy_id"]: p for p in policies}


def editions(policy: dict) -> dict[str, str]:
    return dict(e.split("@") for e in policy["endorsement_editions"].split(";") if e)


def correct_deductible(claim: dict, policy: dict) -> int:
    """The deductible the policy calls for on this loss."""
    if claim["endorsement_applied"] == "HO-04-90":
        return HO0490[editions(policy)["HO-04-90"]]["deductible"]
    if claim["loss_type"] in WIND and policy["windstorm_deductible_pct"] != "":
        return int(policy["coverage_a_limit"]) * int(policy["windstorm_deductible_pct"]) // 100
    return int(policy["deductible"])


# ---- new columns on the original 90 claims ---------------------------------------------------------------------------

def referral(claim: dict) -> str:
    """Why a referral is required, or '' (H.7.4: exposure above authority; H.5.9: a water loss above $25,000)."""
    exposure = claim["reserve"] if claim["status"] == "open" else claim["paid_amount"]
    authority = HANDLER[claim["handler_id"]]["authority_usd"]
    if exposure > authority:
        return f"{'reserve' if claim['status'] == 'open' else 'settlement'} ${exposure:,} exceeds my ${authority:,} authority"
    if claim["loss_type"] in WATER_LOSS and max(claim["reported_amount"], claim["reserve"]) > 25_000:
        return "water loss claimed above $25,000"
    return ""


for c in claims:
    p = POLICY[c["policy_id"]]
    reported_date = min(D(c["loss_date"]) + timedelta(days=rng2.randrange(0, 21)), TODAY)
    ack = reported_date + timedelta(days=rng2.randrange(0, 6))
    handler = rng2.choice(["H-01", "H-02", "H-02", "H-03", "H-03", "H-04", "H-05", "H-06"])
    factor = rng2.uniform(0.8, 1.0)
    items = decision = ""
    if c["status"] != "open":  # decided within every deadline that could apply (10 business days, TX 2022-01)
        items_day = ack + timedelta(days=rng2.randrange(3, 30))
        items, decision = items_day.isoformat(), add_business_days(items_day, rng2.randrange(2, 10)).isoformat()
    # closed rows were paid net of the policy's own deductible (the original paid_amount), so that is what was applied;
    # a denial adjudicates nothing, so it records no deductible and no edition
    deductible = {"open": correct_deductible(c, p), "closed": int(p["deductible"]), "denied": ""}[c["status"]]
    reserve = 0
    if c["status"] == "open":
        exposure = max(0, c["reported_amount"] - deductible)
        if c["endorsement_applied"] == "HO-04-90":
            exposure = min(exposure, HO0490[editions(p)["HO-04-90"]]["limit"])
        reserve = round50(exposure * factor)
    code = c["endorsement_applied"] if c["status"] != "denied" else ""
    c.update({"reported_date": reported_date.isoformat(), "handler_id": handler, "reserve": reserve,
              "acknowledged_date": ack.isoformat(), "items_complete_date": items, "decision_date": decision,
              "edition_applied": f"{code}@{editions(p)[code]}" if code else "", "deductible_applied": deductible})
    c["referred"] = "yes" if referral(c) else "no"

OLD_ROW_SEEDS = {  # new columns only, on original rows (R6)
    "C-5010": {"handler_id": "H-04", "reserve": 52_000, "referred": "no"},  # kind 5
    # kind 9; referred because a roof loss above $10,000 needs a referral (roof claim handling H.5.28)
    "C-5005": {"handler_id": "H-05", "deductible_applied": 5_000, "reserve": 23_800, "referred": "yes"},
    "C-5082": {"handler_id": "H-02", "reserve": 48_000, "referred": "yes"},  # look-alike of 5
    # look-alike of 5: within authority and under the claims manual's $25,000 referral line (1.V, 19.A)
    "C-5019": {"handler_id": "H-05", "reserve": 24_500, "referred": "no"},
    "C-5076": {"referred": "yes"},  # look-alike of 9; a roof loss above $10,000 (H.5.28)
}
for c in claims:
    c.update(OLD_ROW_SEEDS.get(c["claim_id"], {}))

# ---- new claims (C-5091...) ----------------------------------------------------------------------------------------
# claim_id, policy, loss, status, loss_date, reported, paid, reported_date, handler, ack, items, decision,
# edition_applied, deductible_applied, reserve, referred

NEW_CLAIMS = [
    # 1 · wrongful denial: water backup or sewer denied although the policy carries HO 04 90
    ("C-5091", "P-1041", "water backup", "denied", "2026-11-14", 4_650, 0, "2026-11-16", "H-02", "2026-11-17", "2026-11-30", "2026-12-04", "", "", 0, "no"),
    ("C-5092", "P-1043", "sewer", "denied", "2026-12-08", 3_900, 0, "2026-12-09", "H-04", "2026-12-11", "2026-12-21", "2026-12-29", "", "", 0, "no"),
    # 1 + 8 · the same, and after the denial letter the insured disputes the cause (a note); not referred
    ("C-5093", "P-1042", "water backup", "denied", "2027-01-24", 12_400, 0, "2027-01-25", "H-01", "2027-01-26", "2027-02-03", "2027-02-09", "", "", 0, "no"),
    ("C-5094", "P-1048", "sewer", "denied", "2027-02-06", 9_300, 0, "2027-02-08", "H-01", "2027-02-09", "2027-02-15", "2027-02-19", "", "", 0, "no"),
    # 2 · wrong edition applied, both directions; look-alikes: the right edition on either side of 2027-01-01
    ("C-5095", "P-1041", "water backup", "open", "2027-02-03", 4_300, 0, "2027-02-04", "H-03", "2027-02-05", "", "", "HO-04-90@2027-01", 1_000, 3_300, "no"),
    ("C-5096", "P-1042", "sewer", "open", "2027-02-11", 3_600, 0, "2027-02-12", "H-02", "2027-02-15", "", "", "HO-04-90@2010-10", 500, 3_100, "no"),
    ("C-5097", "P-1048", "water backup", "open", "2027-02-14", 6_800, 0, "2027-02-15", "H-02", "2027-02-16", "", "", "HO-04-90@2027-01", 1_000, 5_800, "no"),
    ("C-5098", "P-1041", "water backup", "open", "2027-02-20", 3_200, 0, "2027-02-22", "H-03", "2027-02-23", "", "", "HO-04-90@2010-10", 500, 2_700, "no"),
    # 3 · over the HO 04 90 limit; look-alikes: just under 2010-10's, and over it but under 2027-01's
    ("C-5099", "P-1020", "water backup", "closed", "2024-06-02", 7_450, 6_900, "2024-06-04", "H-03", "2024-06-05", "2024-06-20", "2024-06-27", "HO-04-90@2010-10", 500, 0, "no"),
    ("C-5100", "P-1030", "sewer", "open", "2026-12-19", 11_200, 0, "2026-12-21", "H-02", "2026-12-22", "", "", "HO-04-90@2010-10", 500, 8_500, "no"),
    ("C-5101", "P-1001", "water backup", "closed", "2024-05-10", 5_450, 4_950, "2024-05-13", "H-02", "2024-05-14", "2024-05-24", "2024-05-31", "HO-04-90@2010-10", 500, 0, "no"),
    ("C-5102", "P-1048", "water backup", "closed", "2027-02-02", 8_600, 7_600, "2027-02-03", "H-02", "2027-02-04", "2027-02-09", "2027-02-16", "HO-04-90@2027-01", 1_000, 0, "no"),
    # 4 · the policy's Section I deductible used instead of the endorsement's; look-alike: the endorsement's
    ("C-5103", "P-1020", "sewer", "open", "2026-10-22", 4_100, 0, "2026-10-23", "H-03", "2026-10-26", "", "", "HO-04-90@2010-10", 2_500, 1_600, "no"),
    ("C-5104", "P-1001", "water backup", "closed", "2025-01-15", 4_200, 3_200, "2025-01-16", "H-02", "2025-01-17", "2025-01-28", "2025-02-04", "HO-04-90@2010-10", 1_000, 0, "no"),
    ("C-5105", "P-1030", "sewer", "closed", "2025-03-08", 3_700, 3_200, "2025-03-10", "H-03", "2025-03-11", "2025-03-20", "2025-03-27", "HO-04-90@2010-10", 500, 0, "no"),
    # 9 · the flat deductible on a TX wind loss (2% of $380,000 applies); look-alike: FL 5% applied. Both reserves stay
    # at or under $10,000, so neither roof loss needs a referral (roof claim handling H.5.28)
    ("C-5106", "P-1043", "wind", "open", "2027-02-01", 10_400, 0, "2027-02-02", "H-04", "2027-02-04", "", "", "", 1_000, 9_400, "no"),
    # 5 · reserve above the handler's authority, not referred
    ("C-5107", "P-1049", "fire", "open", "2027-01-28", 21_800, 0, "2027-01-29", "H-03", "2027-02-01", "", "", "", 1_000, 18_600, "no"),
    ("C-5108", "P-1046", "wind", "open", "2027-01-05", 34_800, 0, "2027-01-06", "H-04", "2027-01-08", "", "", "", 26_000, 8_800, "no"),
    # 6 · not acknowledged, deadline near or passed (TX 15 days, FL 14); look-alikes: acknowledged in time, and a
    # fresh MS claim (the claims manual's 15 days, 12.4, are far off)
    ("C-5109", "P-1043", "theft", "open", "2027-02-15", 7_500, 0, "2027-02-17", "H-02", "", "", "", "", 1_000, 6_500, "no"),
    ("C-5110", "P-1044", "fire", "open", "2027-02-08", 11_700, 0, "2027-02-10", "H-03", "", "", "", "", 2_500, 9_200, "no"),
    ("C-5111", "P-1045", "freeze", "open", "2027-02-12", 8_400, 0, "2027-02-13", "H-02", "", "", "", "", 1_000, 7_400, "no"),
    ("C-5112", "P-1043", "fire", "open", "2027-02-16", 15_000, 0, "2027-02-18", "H-04", "2027-02-19", "", "", "", 1_000, 14_000, "no"),
    ("C-5113", "P-1050", "theft", "open", "2027-02-10", 6_200, 0, "2027-02-12", "H-03", "2027-02-25", "", "", "", 1_000, 5_200, "no"),
    ("C-5114", "P-1047", "theft", "open", "2027-02-23", 3_400, 0, "2027-02-25", "H-02", "", "", "", "", 500, 2_900, "no"),
    # 7 · TX: items complete, no decision after 15 business days; look-alike: accepted on business day 12 under
    # HO 01 45 2019-01 (fifteen business days) and paid two business days later, inside B-2019-02's five (B.4.13); it
    # stays open with no exposure left until the payment clears
    ("C-5115", "P-1044", "fire", "open", "2026-12-20", 12_500, 0, "2026-12-21", "H-03", "2026-12-23", "2027-01-29", "", "", 2_500, 10_000, "no"),
    ("C-5116", "P-1049", "theft", "open", "2026-12-30", 7_300, 0, "2027-01-04", "H-02", "2027-01-06", "2027-02-03", "", "", 1_000, 6_300, "no"),
    ("C-5117", "P-1044", "fire", "open", "2027-01-18", 9_800, 7_300, "2027-01-19", "H-04", "2027-01-21", "2027-02-09", "2027-02-25", "", 2_500, 0, "no"),
    # 8 · a note records a disputed cause or competing estimates, not referred; look-alike: the same, referred
    ("C-5118", "P-1047", "water backup", "open", "2027-01-30", 6_900, 0, "2027-02-01", "H-02", "2027-02-02", "", "", "HO-04-90@2010-10", 500, 4_500, "no"),
    ("C-5119", "P-1046", "freeze", "open", "2027-01-17", 21_400, 0, "2027-01-18", "H-02", "2027-01-19", "", "", "", 2_500, 12_500, "no"),
    ("C-5120", "P-1030", "water backup", "open", "2027-01-26", 5_400, 0, "2027-01-27", "H-03", "2027-01-28", "", "", "HO-04-90@2010-10", 500, 4_400, "yes"),
]
assert [row[0] for row in NEW_CLAIMS] == [f"C-{5091 + i}" for i in range(len(NEW_CLAIMS))]
for (cid, pid, loss, status, loss_date, reported, paid, reported_date, handler, ack, items, decision, edition,
     deductible, reserve, referred) in NEW_CLAIMS:
    covered_by = LOSSES[loss]
    claims.append({
        "claim_id": cid, "policy_id": pid, "loss_type": loss, "loss_date": loss_date, "status": status,
        "reported_amount": reported, "paid_amount": paid,
        # a denial means the handler applied no endorsement: that is the wrongful denial's mistake
        "endorsement_applied": covered_by if status != "denied" and covered_by in POLICY[pid]["endorsements"].split(";") else "",
        "reported_date": reported_date, "handler_id": handler, "reserve": reserve, "acknowledged_date": ack,
        "items_complete_date": items, "decision_date": decision, "edition_applied": edition,
        "deductible_applied": deductible, "referred": referred,
    })

# ---- claim notes ----------------------------------------------------------------------------------------------------

DISPUTE, ESTIMATES = "dispute", "estimates"
DISPUTE_TEXT, ESTIMATES_TEXT = "Insured disputes the cause", "Two contractor estimates"  # how a kind 8 note opens
PAYMENT = re.compile(r"Payment of \$([\d,]+) issued")  # how a payment note on an accepted, still open claim opens
SCENARIO_NOTES = {  # claim -> [(date, text, tag)]: facts a rule needs (kind 8, payment) or a handler's stated reason
    "C-5117": [("2027-03-01", "Payment of $7,300 issued for the fire repairs; the file closes once the payment clears", None)],
    "C-5093": [("2027-02-16", "Insured disputes the cause after the denial letter: says the water heater supply line burst, not a drain backup", DISPUTE)],
    "C-5094": [("2027-02-24", "Insured disputes the cause after the denial letter: says a toilet supply line cracked and flooded the lower level, not a sewer backup", DISPUTE)],
    "C-5118": [("2027-02-10", "Insured disputes the cause: says a washing machine supply line failed, not a drain backup", DISPUTE)],
    "C-5120": [("2027-02-08", "Insured disputes the cause: says the dishwasher drain line split, not a sewer backup", DISPUTE)],
    "C-5119": [("2027-02-05", "Two contractor estimates, $9,800 (dry out and patch) and $21,400 (replace drywall, cabinets and flooring)", ESTIMATES)],
    "C-5053": [("2025-03-20", "Two contractor estimates, $31,000 (dry out and patch) and $54,500 (replace drywall, cabinets and flooring)", ESTIMATES)],
}
LOSS_NOTES = {
    "water backup": ["Inspected; water came up through the basement floor drain", "Moisture behind the finished basement wall",
                     "Mitigation company on site; drying equipment placed"],
    "sewer": ["Inspected; sewage came up through the lower-level toilet and shower drain",
              "Mitigation company on site; affected carpet and pad removed"],
    "freeze": ["Pipe in an exterior wall split during the freeze; plumber's invoice received",
               "Drying equipment placed in the kitchen and hall"],
    "wind": ["Roof inspected; shingles missing on the south slope", "Tarp placed on the roof",
             "Fence panels down along the rear lot line"],
    "hail": ["Roof inspected; hail strikes on shingles and gutters", "Dents on roof vents and downspouts"],
    "theft": ["Police report number received", "Inventory of stolen items received",
              "Receipts requested for jewelry and electronics"],
    "fire": ["Kitchen fire contained to the range area; smoke damage in adjacent rooms", "Fire department report received",
             "Contents inventory started"],
}
ACK_NOTES = ["Acknowledged receipt by email; requested photos and receipts",
             "Acknowledged receipt by phone; explained the claim process and requested a proof of loss",
             "Acknowledged receipt by letter; requested photos, receipts and a signed proof of loss"]


def denial_note(claim: dict) -> str:
    if claim["loss_type"] in WATER_BACKUP:
        if claim["claim_id"] >= "C-5091":  # the wrongful denials: the handler read the base form only
            return f"Denied: {claim['loss_type']} is excluded under the policy form; denial letter sent"
        return f"Denied: {claim['loss_type']} is excluded and the policy has no HO 04 90; denial letter sent"
    return "Denied; denial letter sent with the basis for the decision"


def referral_target(claim: dict) -> str:
    exposure = max(claim["reserve"], claim["paid_amount"])
    own = HANDLER[claim["handler_id"]]["authority_usd"]
    able = [h for h in HANDLERS if h["authority_usd"] > own and h["authority_usd"] >= exposure]
    return f"{able[0]['name']} ({able[0]['role']})" if able else "the home office claims committee"


notes = []
for c in claims:
    end = D(c["decision_date"]) if c["decision_date"] else TODAY
    start = D(c["acknowledged_date"] or c["reported_date"])
    written = [(start, rng2.choice(ACK_NOTES) if c["acknowledged_date"] else "New claim assigned from the intake queue")]
    if rng2.random() < (0.5 if c["status"] == "open" else 0.15):
        span = max(0, (end - start).days)
        written.append((start + timedelta(days=rng2.randrange(0, span + 1)), rng2.choice(LOSS_NOTES[c["loss_type"]])))
    for day, text, _tag in SCENARIO_NOTES.get(c["claim_id"], []):
        written.append((D(day), text))
    if c["referred"] == "yes":
        target = referral_target(c)
        if referral(c):
            reason = referral(c)
        elif c["loss_type"] in WIND:  # roof claim handling H.5.28
            reason = f"roof loss above $10,000 (reserve ${c['reserve']:,})"
        else:
            reason = {DISPUTE: "insured disputes the cause", ESTIMATES: "competing estimates"}[SCENARIO_NOTES[c["claim_id"]][0][2]]
        last = max(day for day, _ in written)
        written.append((min(last + timedelta(days=1), end), f"Referred to {target}: {reason}"))
    if c["decision_date"]:
        text = {"closed": "Requested items received; payment issued and claim closed", "denied": denial_note(c),
                "open": "Claim accepted; payment to issue"}[c["status"]]
        written.append((end, text))
    for day, text in sorted(written, key=lambda w: w[0]):
        notes.append({"note_id": f"N-{len(notes) + 1:04d}", "claim_id": c["claim_id"], "date": day.isoformat(),
                      "handler_id": c["handler_id"], "text": text})

# ---- provisions: every rule an issue rests on, located and quoted at build (R3) ------------------------------------

HO_04_90 = {"2010-10": "forms/HO/MS/HO-04-90/2010-10.md", "2027-01": "forms/HO/MS/HO-04-90/2027-01.md"}
WLH = "guidelines/claims/water-loss-handling.md"
B_2019_02 = "bulletins/TX/b-2019-02-prompt-payment.md"
MANUAL = "manuals/claims/manual.md"
ROOF = "guidelines/claims/roof-claim-handling.md"
TX_AMEND = {e: f"forms/HO/TX/HO-01-45/{e}.md" for e in ("2019-01", "2022-01")}
FL_AMEND = {e: f"forms/HO/FL/HO-01-09/{e}.md" for e in ("2019-01", "2023-07")}

# id -> (path, section heading, paragraph marker, words the paragraph must contain, label)
PROVISIONS = {
    "wb-cover-2010-10": (HO_04_90["2010-10"], "## W.1 ", "**W.1**", "caused by a \"water backup\"", "HO 04 90 2010-10 W.1: covers water backup"),
    "wb-cover-2027-01": (HO_04_90["2027-01"], "## W.1 ", "**W.2**", "caused by Water Backup", "HO 04 90 2027-01 W.1: covers water backup"),
    "wb-limit-2010-10": (HO_04_90["2010-10"], "## W.2 ", "**W.2**", "five thousand dollars", "HO 04 90 2010-10 W.2: limit $5,000"),
    "wb-limit-2027-01": (HO_04_90["2027-01"], "## W.2 ", "**W.1**", "ten thousand dollars", "HO 04 90 2027-01 W.2: limit $10,000"),
    "wb-ded-2010-10": (HO_04_90["2010-10"], "## W.3 ", "**W.3**", "five hundred dollars", "HO 04 90 2010-10 W.3: deductible $500"),
    "wb-ded-2027-01": (HO_04_90["2027-01"], "## W.3 ", "**W.3**", "one thousand dollars", "HO 04 90 2027-01 W.3: deductible $1,000"),
    "wb-superseded": (HO_04_90["2010-10"], None, "> SUPERSEDED", "remains in force for policies written under it",
                      "HO 04 90 2010-10: superseded for policies effective on or after 2027-01-01, in force for policies written under it"),
    "governing-edition": ("training/choosing-the-governing-edition.md", "## L.2 ", "**L.2.10**", "depends on what was issued",
                          "Choosing the governing edition L.2.10: what was issued governs, not the claim date"),
    "tx-ack-2019-01": (TX_AMEND["2019-01"], "## T.5 ", "**T.5**", "within fifteen days", "HO 01 45 2019-01 T.5: acknowledge within 15 days"),
    "tx-ack-2022-01": (TX_AMEND["2022-01"], "## T.5 ", "**T.5**", "within fifteen days", "HO 01 45 2022-01 T.5: acknowledge within 15 days"),
    "tx-decide-2019-01": (TX_AMEND["2019-01"], "## T.5 ", "**T.5**", "within fifteen business days", "HO 01 45 2019-01 T.5: accept or reject within 15 business days"),
    "tx-decide-2022-01": (TX_AMEND["2022-01"], "## T.5 ", "**T.7**", "within ten business days", "HO 01 45 2022-01 T.5 (T.7): accept or reject within 10 business days"),
    "b-ack": (B_2019_02, "## B.4 ", "**B.4.3**", "fifteen (15) days", "Bulletin B-2019-02 B.4.3: acknowledge within 15 days"),
    "b-decide": (B_2019_02, "## B.4 ", "**B.4.8**", "fifteen (15) business days", "Bulletin B-2019-02 B.4.8: accept or reject within 15 business days"),
    "fl-ack-2019-01": (FL_AMEND["2019-01"], "## T.5 ", "**T.2**", "within fourteen days", "HO 01 09 2019-01 T.5 (T.2): acknowledge within 14 days"),
    "fl-ack-2023-07": (FL_AMEND["2023-07"], "## T.5 ", "**T.5**", "within fourteen days", "HO 01 09 2023-07 T.5: acknowledge within 14 days"),
    "manual-ack": (MANUAL, "## Chapter 12 ", "**12.4**", "within 15 days", "Claims manual 12.4: acknowledge within 15 days"),
    "manual-decide": (MANUAL, "## Chapter 12 ", "**12.18**", "within 30 days", "Claims manual 12.18: accept or reject within 30 days"),
    "authority": (WLH, "## H.7 ", "**H.7.4**", "exceed your available authority", "Water-loss handling H.7.4: refer when exposure may exceed your authority"),
    "endorsement-issue": (WLH, "## H.7 ", "**H.7.5**", "endorsement issue", "Water-loss handling H.7.5: refer when coverage turns on an endorsement issue"),
    "disputed-cause": (WLH, "## H.7 ", "**H.7.17**", "disputed cause of loss", "Water-loss handling H.7.17: refer a disputed cause of loss"),
    "competing-estimates": (WLH, "## H.7 ", "**H.7.21**", "competing estimates", "Water-loss handling H.7.21: refer competing estimates"),
    "water-over-25k": (WLH, "## H.5 ", "**H.5.9**", "above $25,000", "Water-loss handling H.5.9: refer a water loss above $25,000"),
    "manual-refer-25k": (MANUAL, "## Chapter 1 ", "**1.V**", "evaluated amount above $25,000",
                         "Claims manual 1.V: refer a loss evaluated above $25,000"),
    "manual-19a": (MANUAL, "## Chapter 19 ", "**19.A**", "incurred amount above $25,000",
                   "Claims manual 19.A: refer a loss incurred above $25,000"),
    "roof-10k": (ROOF, "## H.5 ", "**H.5.28**", "incurred amount above $10,000 before authorizing final payment",
                 "Roof claim handling H.5.28: refer a roof loss above $10,000 before final payment"),
    # payment of an accepted claim: no claim may trip these (no issue kind models them), but the windows rest on them
    "b-pay": (B_2019_02, "## B.4 ", "**B.4.13**", "within five (5) business days",
              "Bulletin B-2019-02 B.4.13: pay an accepted claim within 5 business days"),
    "tx-pay-2019-01": (TX_AMEND["2019-01"], "## T.5 ", "**T.5**", "within five business days",
                       "HO 01 45 2019-01 T.5: pay an accepted claim within 5 business days"),
    "tx-pay-2022-01": (TX_AMEND["2022-01"], "## T.5 ", "**T.8**", "within five business days",
                       "HO 01 45 2022-01 T.5 (T.8): pay an accepted claim within 5 business days"),
    "fl-pay-2019-01": (FL_AMEND["2019-01"], "## T.5 ", "**T.62**", "within twenty business days",
                       "HO 01 09 2019-01 T.5 (T.62): pay an accepted claim within 20 business days"),
    "fl-pay-2023-07": (FL_AMEND["2023-07"], "## T.5 ", "**T.34**", "within twenty business days",
                       "HO 01 09 2023-07 T.5 (T.34): pay an accepted claim within 20 business days"),
    "tx-wind-2019-01": (TX_AMEND["2019-01"], "## T.1 ", "**T.4**", "applicable deductible percentage to the deductible basis",
                        "HO 01 45 2019-01 T.1 (T.4): the windstorm and hail percentage applies to the deductible basis"),
    "tx-wind-2022-01": (TX_AMEND["2022-01"], "## T.1 ", "**T.5**", "using the applicable limit of liability",
                        "HO 01 45 2022-01 T.1 (T.5): the windstorm and hail deductible is calculated from the limit of liability"),
    "fl-wind-2019-01": (FL_AMEND["2019-01"], "## T.1 ", "**T.10**", "used to calculate the Windstorm and Hail Deductible",
                        "HO 01 09 2019-01 T.1 (T.10): the windstorm and hail deductible is calculated on the deductible basis"),
    "fl-wind-2023-07": (FL_AMEND["2023-07"], "## T.1 ", "**T.10**", "from the policy limits applicable to the damaged property",
                        "HO 01 09 2023-07 T.1 (T.10): the windstorm and hail deductible is determined from the policy limits"),
}


def locate(pid: str) -> str:
    """`path#Lstart-Lend (label)`, after confirming the paragraph says what the rule needs."""
    path, section, marker, words, label = PROVISIONS[pid]
    lines = (CORPUS / path).read_text().splitlines()
    lo, hi = 0, len(lines)
    if section:
        lo = next(i for i, line in enumerate(lines) if line.startswith(section))
        hi = next((i for i in range(lo + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    start = next(i for i in range(lo, hi) if lines[i].startswith(marker))
    end = next((i for i in range(start + 1, hi) if not lines[i].strip() or lines[i].startswith("**")), hi)
    paragraph = " ".join(" ".join(lines[start:end]).split())
    assert words in paragraph, f"{pid}: {path} line {start + 1} no longer says {words!r}"
    return f"{path}#L{start + 1}-L{end} ({label})"


for (code, edition), (lo, hi) in PCT_RANGE.items():  # the percentages written above stay within the edition's range
    path = (TX_AMEND if code == "HO-01-45" else FL_AMEND)[edition]
    text = " ".join((CORPUS / path).read_text().split())
    section = text[text.index("## T.1 "):text.index("## T.2 ")]
    assert f"{NUMBER[lo]} percent" in section and f"{NUMBER[hi]} percent" in section, f"{path}: range {lo}-{hi}%"

# ---- serialize, then read the tables back as the agent's tools serve them ------------------------------------------
# Every condition below reads only these parsed rows (strings, as in the CSV files), never the generator's own
# variables: an issue the tables do not show cannot be seeded (01 §7).

POLICY_COLUMNS = ["policy_id", "form", "form_edition", "state", "status", "effective_date", "coverage_a_limit",
                  "deductible", "endorsements", "endorsement_editions", "windstorm_deductible_pct"]
CLAIM_COLUMNS = ["claim_id", "policy_id", "loss_type", "loss_date", "status", "reported_amount", "paid_amount",
                 "endorsement_applied", "reported_date", "handler_id", "reserve", "acknowledged_date",
                 "items_complete_date", "decision_date", "edition_applied", "deductible_applied", "referred"]
TABLES = {"policies": (policies, POLICY_COLUMNS), "claims": (claims, CLAIM_COLUMNS),
          "handlers": (HANDLERS, list(HANDLERS[0])), "claim_notes": (notes, list(notes[0]))}


def to_csv(rows: list[dict], columns: list[str]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


TEXT = {name: to_csv(rows, columns) for name, (rows, columns) in TABLES.items()}
SEEN = {name: list(csv.DictReader(io.StringIO(text, newline=""))) for name, text in TEXT.items()}
S_POLICY = {p["policy_id"]: p for p in SEEN["policies"]}
S_HANDLER = {h["handler_id"]: h for h in SEEN["handlers"]}
S_CLAIM = {c["claim_id"]: c for c in SEEN["claims"]}
S_NOTES: dict[str, list[tuple[str, str]]] = {}  # claim -> [(date, text)]
for n in SEEN["claim_notes"]:
    S_NOTES.setdefault(n["claim_id"], []).append((n["date"], n["text"]))


def note_tags(claim_id: str) -> set[str]:
    """The kind 8 facts a claim's notes record."""
    openings = {DISPUTE: DISPUTE_TEXT, ESTIMATES: ESTIMATES_TEXT}
    return {tag for tag, opening in openings.items() if any(t.startswith(opening) for _, t in S_NOTES.get(claim_id, []))}


# ---- the issue conditions (01 §4), evaluated on every claim -----------------------------------------------------------


def ack_deadline(policy: dict) -> int:
    return 14 if policy["state"] == "FL" else 15  # FL: HO 01 09; TX: HO 01 45, B-2019-02; elsewhere: manual 12.4


def decision_late(claim: dict, policy: dict) -> bool:
    """Items complete and the accept/reject deadline passed without, or before, a decision."""
    if not claim["items_complete_date"]:
        return False
    items, decided = D(claim["items_complete_date"]), D(claim["decision_date"]) if claim["decision_date"] else TODAY
    if policy["state"] == "TX":  # B-2019-02 B.4.8; the policy's own HO 01 45 2022-01 is stricter (T.7)
        return business_days(items, decided) > (10 if editions(policy).get("HO-01-45") == "2022-01" else 15)
    return (decided - items).days > 30  # claims manual 12.18


def kinds_of(c: dict) -> list[int]:
    p = S_POLICY[c["policy_id"]]
    eds = editions(p)
    status, found = c["status"], []
    paid, reserve = int(c["paid_amount"]), int(c["reserve"])
    governing = HO0490.get(eds.get("HO-04-90", ""), {})
    wb = c["endorsement_applied"] == "HO-04-90" and status in ("open", "closed")
    right_edition = c["edition_applied"] == (f"HO-04-90@{eds['HO-04-90']}" if "HO-04-90" in eds else None)
    if status == "denied" and c["loss_type"] in WATER_BACKUP and "HO-04-90" in eds:
        found.append(1)
    if status == "open" and c["edition_applied"]:
        code, _, edition = c["edition_applied"].partition("@")
        if code in eds and eds[code] != edition:
            found.append(2)
    if wb and max(paid, reserve) > governing["limit"]:
        found.append(3)
    if wb and right_edition and int(c["deductible_applied"]) != governing["deductible"]:
        found.append(4)
    # the exposure the row shows: an open claim's reserve, a closed claim's payment, nothing on a denial
    if max(paid, reserve) > int(S_HANDLER[c["handler_id"]]["authority_usd"]) and c["referred"] == "no":
        found.append(5)
    if status == "open":
        waited = (D(c["acknowledged_date"]) if c["acknowledged_date"] else TODAY) - D(c["reported_date"])
        if (not c["acknowledged_date"] and waited.days >= ack_deadline(p) - 5) or waited.days > ack_deadline(p):
            found.append(6)
        if decision_late(c, p):
            found.append(7)
    if status != "closed" and c["referred"] == "no" and c["loss_type"] in WATER_LOSS and note_tags(c["claim_id"]):
        found.append(8)  # a denial the insured disputes is still live
    if status in ("open", "closed") and c["loss_type"] in WIND and p["windstorm_deductible_pct"] != "" and \
            int(c["deductible_applied"]) != correct_deductible(c, p):
        found.append(9)  # a closed one was paid with the wrong deductible (02 §3 screens closed claims for it)
    return found


PAY_WINDOW = {"TX": 5, "FL": 20}  # business days from acceptance to payment (B-2019-02 B.4.13, HO 01 45; HO 01 09)


def payment_late(c: dict, p: dict) -> bool:
    """An accepted claim (open, with a decision) whose payment is not on record by the state's deadline. Unpaid counts
    as due or overdue: TX allows five business days. A payment shows as a note naming the amount paid."""
    if c["status"] != "open" or not c["decision_date"]:
        return False
    paid_on = [D(day) for day, text in S_NOTES.get(c["claim_id"], [])
               if (m := PAYMENT.match(text)) and int(m.group(1).replace(",", "")) == int(c["paid_amount"])]
    if int(c["paid_amount"]) <= 0 or not paid_on:
        return True
    window = PAY_WINDOW.get(p["state"])
    return window is not None and min(paid_on) > add_business_days(D(c["decision_date"]), window)


def other_issues(c: dict) -> list[str]:
    """Rules outside the nine kinds that a row's columns can still trip; a look-alike must trip none, and a flagged
    claim only those its key line lists (`also`), or that its kinds already cover."""
    p = S_POLICY[c["policy_id"]]
    exposure = max(int(c["paid_amount"]), int(c["reserve"]))
    found = []
    if payment_late(c, p):
        found.append("payment")
    if c["status"] != "open":  # kinds 6 and 7 judge open claims; a decided one must have met both deadlines too
        if (D(c["acknowledged_date"]) - D(c["reported_date"])).days > ack_deadline(p):
            found.append("acknowledgment")
        if decision_late(c, p):
            found.append("decision")
    if exposure > 25_000 and c["referred"] == "no":
        found.append("refer-25k")  # claims manual 1.V, 19.A: any loss, not only water (H.5.9)
    if c["loss_type"] in WIND and exposure > 10_000 and c["referred"] == "no":
        found.append("roof-10k")  # roof claim handling H.5.28
    return found


OTHER_PROVISIONS = {"refer-25k": ["manual-refer-25k", "manual-19a"], "roof-10k": ["roof-10k"]}
COVERED = {5: {"refer-25k"}}  # kind -> other issues its finding already states (the same referral is missing)


def provisions_of(c: dict, kind: int) -> list[str]:
    p = S_POLICY[c["policy_id"]]
    eds = editions(p)
    wb = eds.get("HO-04-90")
    ids = {
        1: [f"wb-cover-{wb}", "endorsement-issue"],
        2: ["wb-superseded", "governing-edition", f"wb-ded-{wb}"],
        3: [f"wb-limit-{wb}"],
        4: [f"wb-ded-{wb}"],
        5: ["authority"] + (OTHER_PROVISIONS["refer-25k"] if "refer-25k" in other_issues(c) else []),
        6: {"TX": [f"tx-ack-{eds.get('HO-01-45')}", "b-ack"] if "HO-01-45" in eds else ["b-ack"],
            "FL": [f"fl-ack-{eds.get('HO-01-09')}"]}.get(p["state"], ["manual-ack"]),
        7: (["b-decide"] + ([f"tx-decide-{eds['HO-01-45']}"] if "HO-01-45" in eds else [])) if p["state"] == "TX"
        else ["manual-decide"],
        8: [{DISPUTE: "disputed-cause", ESTIMATES: "competing-estimates"}[t] for t in sorted(note_tags(c["claim_id"]))],
        9: [f"{'tx' if p['state'] == 'TX' else 'fl'}-wind-{eds.get(STATES[p['state']])}"],
    }[kind]
    return [locate(i) for i in ids]


# Each seeded claim names its kinds; each look-alike, the kind it resembles. Flags on original rows that their
# original values already make (paid with the Section I deductible, above the limit, or with the flat deductible on a
# wind or hail loss) are listed as existing; `ALSO`, the rules outside the nine kinds such a row also trips.
SEEDED = {"C-5091": [1], "C-5092": [1], "C-5093": [1, 8], "C-5094": [1, 8], "C-5095": [2], "C-5096": [2],
          "C-5099": [3], "C-5100": [3], "C-5103": [4], "C-5104": [4], "C-5010": [5], "C-5107": [5],
          "C-5109": [6], "C-5110": [6], "C-5111": [6], "C-5115": [7], "C-5116": [7], "C-5118": [8], "C-5119": [8],
          "C-5005": [9], "C-5106": [9]}
EXISTING = {"C-5045": [3], "C-5046": [4], "C-5054": [3, 4], "C-5003": [9], "C-5016": [9], "C-5027": [9], "C-5068": [9],
            "C-5069": [9], "C-5080": [9]}
ALSO = {"C-5003": ["roof-10k"], "C-5016": ["refer-25k", "roof-10k"], "C-5080": ["roof-10k"]}
LOOKALIKES = {
    "C-5001": (1, "denied water backup; the policy has no HO 04 90"),
    "C-5043": (1, "denied sewer backup; the policy has HO 01 45 but no HO 04 90"),
    "C-5097": (2, "P-1048 took effect 2027-01-20 on HO 04 90 2027-01: its edition, $1,000 deductible and $10,000 limit govern"),
    "C-5098": (2, "loss after 2027-01-01, but P-1041 was written under 2010-10, which stays in force for it"),
    "C-5101": (3, "paid $4,950, under 2010-10's $5,000 limit"),
    "C-5102": (3, "paid $7,600: over 2010-10's limit, under the $10,000 of 2027-01, which governs P-1048"),
    "C-5105": (4, "the endorsement's $500 deductible applied"),
    "C-5055": (4, "the endorsement's $500 deductible applied, not the policy's $1,000"),
    "C-5082": (5, "reserve above the adjuster's authority, and referred"),
    "C-5019": (5, "reserve $24,500: within the senior adjuster's $50,000 authority and under the claims manual's $25,000 referral line (1.V, 19.A)"),
    "C-5112": (6, "TX, acknowledged two days after the report"),
    "C-5113": (6, "FL, acknowledged on day 13 of 14"),
    "C-5114": (6, "MS, reported 5 days ago: the claims manual's 15 days (12.4) are not near"),
    "C-5117": (7, "accepted on business day 12 (P-1044 carries HO 01 45 2019-01: fifteen business days) and paid $7,300 two business days later, inside B-2019-02's five"),
    "C-5120": (8, "insured disputes the cause, and the claim was referred"),
    "C-5053": (8, "competing estimates, and the claim was referred"),
    "C-5108": (9, "FL wind: 5% of the $520,000 Coverage A applied; reserve under the roof referral line"),
    "C-5076": (9, "FL hail: the policy's percentage of Coverage A applied; referred as a roof loss above $10,000"),
}

# ---- checks (01 §7): only what would break the demo -------------------------------------------------------------

found = {cid: kinds_of(c) for cid, c in S_CLAIM.items()}
flagged = {cid: k for cid, k in found.items() if k}
expected = {**SEEDED, **EXISTING}
assert flagged == expected, f"issue conditions disagree with the seeds: " \
    f"{ {cid: (flagged.get(cid), expected.get(cid)) for cid in set(flagged) | set(expected) if flagged.get(cid) != expected.get(cid)} }"
for cid, (kind, _) in LOOKALIKES.items():
    assert cid not in flagged and cid not in expected, f"look-alike {cid} carries an issue"
    assert not other_issues(S_CLAIM[cid]), f"look-alike {cid} trips {other_issues(S_CLAIM[cid])}"
for cid, kinds in expected.items():  # a flagged claim carries its kinds and only the other issues its key line lists
    covered = set().union(*(COVERED.get(k, set()) for k in kinds))
    extra = [i for i in other_issues(S_CLAIM[cid]) if i not in covered]
    assert extra == ALSO.get(cid, []), f"{cid} also trips {extra}, the key lists {ALSO.get(cid, [])}"
for c in S_CLAIM.values():  # no issue kind models a late payment, so no claim may have one
    assert not payment_late(c, S_POLICY[c["policy_id"]]), f"{c['claim_id']}: accepted and not paid in time"
for pid in ("b-pay", "tx-pay-2019-01", "tx-pay-2022-01", "fl-pay-2019-01", "fl-pay-2023-07"):
    locate(pid)  # the payment windows above still say what PAY_WINDOW assumes
for c in S_CLAIM.values():  # no water loss above $25,000 left unreferred (H.5.9): an issue the key would not name
    assert not (c["loss_type"] in WATER_LOSS and c["referred"] == "no"
                and max(int(c["reported_amount"]), int(c["reserve"])) > 25_000), f"{c['claim_id']} needs an H.5.9 referral"
for c in S_CLAIM.values():  # a denial adjudicates nothing: no deductible, edition or reserve on it
    if c["status"] == "denied":
        assert c["deductible_applied"] == c["edition_applied"] == "" and c["reserve"] == "0", c["claim_id"]
for c in S_CLAIM.values():  # keys resolve, and no date runs past today or before the loss
    assert c["policy_id"] in S_POLICY and c["handler_id"] in S_HANDLER, c["claim_id"]
    days = [c[k] for k in ("reported_date", "acknowledged_date", "items_complete_date", "decision_date") if c[k]]
    assert all(c["loss_date"] <= d <= TODAY.isoformat() for d in days), c["claim_id"]
for n in SEEN["claim_notes"]:
    assert n["claim_id"] in S_CLAIM and n["handler_id"] in S_HANDLER and n["date"] <= TODAY.isoformat(), n["note_id"]

# ---- write ---------------------------------------------------------------------------------------------------------

for name, text in TEXT.items():
    with open(HERE / f"{name}.csv", "w", newline="") as f:
        f.write(text)

parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
parser.add_argument("--key-out", type=Path, help="write the triage answer key (JSON lines) to this file or directory")
args = parser.parse_args()
if args.key_out:
    out = args.key_out / "claims-triage-key.jsonl" if args.key_out.is_dir() else args.key_out
    lines = []
    for cid in sorted(set(expected) | set(LOOKALIKES)):
        if cid in expected:
            line = {"claim_id": cid, "expect": "flag", "kinds": expected[cid],
                    "provisions": [ref for k in expected[cid] for ref in provisions_of(S_CLAIM[cid], k)],
                    "origin": "seeded" if cid in SEEDED else "existing"}
            if cid in ALSO:  # a rule outside the nine kinds the row's original values also break
                line["also"] = [locate(i) for issue in ALSO[cid] for i in OTHER_PROVISIONS[issue]]
            lines.append(line)
        else:
            kind, why = LOOKALIKES[cid]
            lines.append({"claim_id": cid, "expect": "clear", "lookalike_of": kind, "why": why})
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(line) + "\n" for line in lines))
    print(f"key: {len(expected)} flags, {len(LOOKALIKES)} look-alikes -> {out}")
print(f"{len(policies)} policies, {len(claims)} claims ({sum(c['status'] == 'open' for c in claims)} open), "
      f"{len(HANDLERS)} handlers, {len(notes)} notes")
