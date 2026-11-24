# Invented tables

Invented test data for the wiki-memory sidecar's table tools and the claims desk. They are not source documents:
the document tools (`ls`, `glob`, `grep`, `read_file`) never show them, and OpenWiki ignores this folder.

| Table | Rows | Key | Columns |
|---|---|---|---|
| `policies.csv` | 50 | `policy_id` | `form`, `form_edition`, `state`, `status`, `effective_date`, `coverage_a_limit`, `deductible`, `endorsements` (`;`-separated), `endorsement_editions` (`CODE@EDITION`, one per endorsement), `windstorm_deductible_pct` |
| `claims.csv` | 120 | `claim_id` | `policy_id`, `loss_type`, `loss_date`, `status`, `reported_amount`, `paid_amount`, `endorsement_applied`, `reported_date`, `handler_id`, `reserve`, `acknowledged_date`, `items_complete_date`, `decision_date`, `edition_applied`, `deductible_applied`, `referred` |
| `handlers.csv` | 6 | `handler_id` | `name`, `role`, `authority_usd` |
| `claim_notes.csv` | about 270 | `note_id` | `claim_id`, `date`, `handler_id`, `text` |

- The demo's today is **2027-03-02**: deadlines are counted to it.
- `endorsement_editions` gives the edition in force on the policy's `effective_date` (the earliest edition in the
  corpus when the policy predates them all). Policies that took effect in 2027 carry HO 04 90 2027-01.
- `windstorm_deductible_pct` is filled for TX and FL policies that carry the state amendatory endorsement and have a
  Coverage A limit, the amount the percentage applies to; it is empty elsewhere.
- `reserve` is the handler's current estimate of exposure on an open claim, 0 once closed or denied. An empty
  `acknowledged_date`, `items_complete_date` or `decision_date` means it has not happened yet. `items_complete_date`
  is when the last requested item arrived; `decision_date` is when the claim was accepted, denied or closed.
- `edition_applied` and `deductible_applied` are what the handler used, which is not always what the policy says.
  A denied claim adjudicated nothing, so both are empty on it.
- Notes stand in for claim documents.

Forms, editions and endorsements name documents in `forms/`. Ids, names, dates, amounts and notes mean nothing
outside the demo. Some claims carry an issue on purpose, for the claims desk to find; the answer key is not kept in
this repo.

Rebuild with `python3 data/generate.py` (deterministic: byte-identical output). `--key-out PATH` also writes the
claims desk's answer key to `PATH`; the generator fails if a seeded issue or a look-alike does not hold, judged only
from the tables as written (the rows the agent reads), or if a provision it cites no longer says what the issue
rests on.
