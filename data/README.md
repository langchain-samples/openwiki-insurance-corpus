# Invented tables

`policies.csv` (40 rows, key `policy_id`) and `claims.csv` (90 rows, key `claim_id`, `policy_id` refers to a
policy) are invented test data for the wiki-memory sidecar's table tools. They are not source documents: the
document tools (`ls`, `glob`, `grep`, `read_file`) never show them, and OpenWiki ignores this folder.

Forms, editions and endorsements name documents in `forms/`. Ids, dates and amounts mean nothing outside the demo.
Rebuild with `python3 data/generate.py` (deterministic).
