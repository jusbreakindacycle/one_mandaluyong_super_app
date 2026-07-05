# Synthetic Test Data — One Mandaluyong Super App

**All records in this dataset are entirely fictional.** No real citizens,
businesses, or transactions are represented. Names, IDs, contact details,
and reference numbers are randomly generated and do not correspond to real
individuals or entities. Barangay names are real (public administrative
divisions of Mandaluyong), used only for geographic realism.

**Email addresses and IP addresses use reserved, non-routable values by
design.** Emails use only `example.com` / `example.org` / `example.net`
(reserved for documentation use under RFC 2606), and IP addresses use only
`192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24` (reserved for
documentation use under RFC 5737). This guarantees no generated record can
ever correspond to a real person's inbox or a real, live internet address.
**Email usernames are also derived from each record's own Filipino name**
(e.g. `juan.gonzales@example.net`), not from an independent default-locale
name generator, so citizen records stay internally consistent.

This dataset exists to support development, testing, and demonstration of
the platform's data structures — it is not a substitute for the actual
Records Retention Schedule required under RA 9470, which must still be
confirmed with the National Archives of the Philippines before real citizen
data is collected in Phase 1.

## Contents

| File | Records | Description |
|---|---|---|
| `citizens.json` / `.csv` | 520 | Citizen profile records |
| `business_permits.json` / `.csv` | 540 | Business permit / clearance applications |
| `payments.json` / `.csv` | 530 | Payment transactions linked to permits |
| `audit_logs.json` / `.csv` | 560 | System activity / audit trail entries |

**Total: 2,150 synthetic records.**

## Relationships

- `business_permits.citizen_id` → `citizens.citizen_id`
- `payments.permit_id` → `business_permits.permit_id`
- `payments.citizen_id` → `citizens.citizen_id`
- `audit_logs.actor_id` → `citizens.citizen_id` (when `actor_type` is "Citizen")

## Regenerating

Run `python3 generate.py` to regenerate with the same fixed random seed
(reproducible) or change the seed values at the top of the script for a
different dataset.
