# Handoff Context — One Mandaluyong Super App

Paste this whole note into a new chat, along with the attached README.md file,
if continuing this project in a different account or after hitting a usage limit.

---

## What this project is

"One Mandaluyong Super App" — a monorepo digital transformation platform for
the City Government of Mandaluyong, Philippines. Built by Highimbrits
(GitHub: jusbreakindacycle), a self-initiated civic tech project.

## Repo

- GitHub: https://github.com/jusbreakindacycle/one_mandaluyong_super_app
- Public repo, `main` branch protected via a GitHub Ruleset (`main-protection`):
  requires PR before merging, requires `lint-and-validate` and `security-scan`
  status checks to pass, blocks force pushes and deletions, no bypass list.
- Branching model: trunk-based (Section 24 of README) — `main` is the only
  long-lived branch; short-lived `feature/`, `fix/`, `chore/`, `docs/` branches
  merge back via PR.
- CI: `.github/workflows/ci.yml` — GitHub Actions, jobs are `detect-changes`,
  `lint-and-validate`, `security-scan`.
- CODEOWNERS already fixed to use real username (`@jusbreakindacycle`)
  instead of placeholder team handles.

## README.md status

- Current version: **v1.6.0**
- 31 sections total, all written (no more TOC-only placeholder sections)
- Attach the actual current README.md file to the new chat — don't rely on
  Claude's memory or a shared link, neither will carry over

## Pending, not yet pushed to GitHub

- Section 17 (Data Architecture) — new "Records Retention Schedule"
  subsection was added locally (RA 9470, NAP Records Disposition Schedule
  requirement) but has NOT been committed/pushed yet. If the attached
  README.md already includes this subsection, it's done — just needs pushing
  whenever ready.

## Parking lot (identified, not yet actionable)

1. Full separate ISSP (Information Systems Strategic Plan) document —
   blocked on City Budget Office (ICT budget figures) and City HRMO
   (staffing plantilla) data. An "ISSP Readiness Note" one-pager was already
   drafted to request this data — see attached .docx if available.
2. Records Disposition Schedule confirmation with the National Archives of
   the Philippines (NAP) — City needs to formally initiate this.
3. IT Steering Committee / CIO structure — proposed in Section 11, pending
   formal confirmation by the City Administrator's Department. Note: CIO
   designation is now a legal requirement under RA 12143 (E-Governance Act
   of 2025), not just best practice.
4. CODEOWNERS still uses one real username as a stand-in for all module
   owners — needs real GitHub Teams once a GitHub Organization exists.

## Working preferences

- Always reply in English regardless of Tagalog/Taglish input
- User is still learning git — has used the branch → commit → push → PR →
  merge flow successfully several times now, with a saved cheat sheet
  (git-workflow-cheatsheet.md)
- Prefers explanations before big changes, and appreciates honest pushback
  (e.g. was talked out of a 3-branch Git Flow model in favor of trunk-based)

## Next likely steps (pick up here)

- Push the Records Retention Schedule change (branch → PR → merge)
- Continue deciding on ISSP submission (see ISSP Readiness Note)
- Eventually start real Phase 0 code in one module (e.g. `platform/identity-access`)
