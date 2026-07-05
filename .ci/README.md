# .ci/

The root README's Section 21 (Repository Structure) describes this folder generically as "GitLab CI/CD or GitHub Enterprise pipelines," since the blueprint is platform-agnostic.

Since this repository is hosted on GitHub, actual pipeline definitions live in `.github/workflows/` (GitHub Actions), not here. This folder is kept as a placeholder for any shared CI configuration, templates, or scripts referenced by those workflows (e.g. reusable composite actions).
