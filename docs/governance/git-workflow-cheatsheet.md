# Git Workflow Cheat Sheet — One Mandaluyong Super App

Use this exact sequence every time you make a change. `main` is protected —
you can never commit or push directly to it. Every change goes through a
branch and a pull request.

---

## Every time you start a new change

```bash
git checkout main
git pull
git checkout -b <type>/<short-description>
```

**Branch naming** (per Section 24, Branching Strategy):
- `feature/...` — new capability
- `fix/...` — bug fix
- `chore/...` — maintenance, config, non-code housekeeping (like CODEOWNERS)
- `docs/...` — documentation-only changes (like README updates)
- `hotfix/...` — urgent production fix

Examples: `docs/update-section-11-cio`, `fix/payment-timeout-bug`

---

## While working

Edit your files normally in VS Code. Save with Ctrl+S as you go.

Check what's changed anytime, without committing:
```bash
git status
```

---

## When ready to commit (can batch multiple files/edits into one commit)

```bash
git add .
git commit -m "type: short description of what changed and why"
```

Commit message examples:
- `chore: fix CODEOWNERS placeholders`
- `docs: update Section 11 for RA 12143 CIO mandate`
- `feat: add citizen identity login flow`

---

## Push your branch

```bash
git push -u origin <branch-name>
```

(First push on a new branch needs `-u`; after that, plain `git push` works.)

---

## On GitHub

1. Click the **"Compare & pull request"** banner (or go to Pull Requests → New)
2. Fill in the PR template:
   - **Architecture review required?** → Yes only if it touches shared contracts, security, identity, or data governance
   - **Compliance check** → check only if it touches citizen data or a new citizen-facing module
   - **Tests** → check only if automated tests were added
   - **Checklist** → check "Follows Coding Standards and Branching Strategy" if true; check others as applicable
3. Click **Create pull request**
4. Wait for `lint-and-validate` and `security-scan` to turn green
5. Click **Merge pull request** → confirm

---

## After merging — sync back up locally

```bash
git checkout main
git pull
git branch -d <branch-name>
```

This deletes your local copy of the finished branch (safe — it's already
merged into `main`). The remote branch on GitHub can also be deleted from
the PR page after merge (usually a button appears automatically).

---

## Quick troubleshooting

| Symptom | Meaning |
|---|---|
| `nothing to commit, working tree clean` | You haven't saved a file, or already committed everything |
| `push declined due to repository rule violations` | You tried to push directly to `main` — create a branch instead |
| Merge button greyed out on GitHub | Status checks (`lint-and-validate`, `security-scan`) haven't passed yet — wait |
| `remote origin already exists` | Remote is already set — use `git remote -v` to check it's correct, or `git remote set-url origin <url>` to fix it |
