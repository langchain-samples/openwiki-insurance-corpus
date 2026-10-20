"""Writes the invented policy and claim tables (policies.csv, claims.csv). Deterministic: rerun it to rebuild them.

Every row is invented. Forms, editions and endorsements name documents in this corpus, so a row can be read
against the form it was written on; policy and claim ids, dates and amounts mean nothing outside this demo.
"""

from __future__ import annotations

import csv
import random
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).parent
rng = random.Random(20261020)

FORMS = {  # form -> editions in forms/<line>/MS/<form>/
    "HO-3": ["2011-05", "2018-09", "2024-03"], "HO-4": ["2013-07", "2021-10"], "HO-5": ["2015-01", "2022-06"],
    "HO-6": ["2014-04", "2023-02"], "DP-3": ["2012-11", "2020-08", "2026-01"],
}
STATES = {"MS": None, "TX": "HO-01-45", "FL": "HO-01-09"}  # state -> its amendatory endorsement (HO forms)
ENDORSEMENTS = ["HO-04-90", "HO-04-61", "HO-04-10", "HO-04-20", "HO-04-41"]
LOSSES = {"water backup": "HO-04-90", "wind": None, "hail": None, "theft": "HO-04-61", "fire": None,
          "freeze": None, "sewer": "HO-04-90"}


LAST_EFFECTIVE, LAST_LOSS = date(2026, 6, 30), date(2026, 10, 1)  # the demo's "today" is October 2026


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

for name, rows in (("policies", policies), ("claims", claims)):
    with open(HERE / f"{name}.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
print(f"{len(policies)} policies, {len(claims)} claims")
