# Legal and Regulatory References — One Mandaluyong Super App

**Source:** Originally extracted from README.md, Section 19 (Legal and Regulatory Compliance); since expanded with specific implementing circulars, resolutions, and ordinances not individually named in that section's prose (see Maintenance Notes below for what was added and why).
**Version tracked against:** README.md v1.9.3
**Status:** Engineering-side reference list — not a legal opinion. Requires review and confirmation by the City Legal Department (Office of the Chief Legal Counsel) before use in procurement, budget, or Sanggunian submissions.

This file exists so Legal, ICTD, and future contributors can check the platform's legal basis without opening the full engineering blueprint. It is a citation index, not a substitute for the fuller discussion in README.md Section 19, which explains *why* each law applies to which module.

---

## Local Government Authority

- **Republic Act No. 7160** — Local Government Code of 1991

## Data Privacy

- **Republic Act No. 10173** — Data Privacy Act of 2012 (and Implementing Rules and Regulations)
- **NPC Circular No. 2022-04** — Registration of Personal Data Processing Systems, Notification Regarding Automated Decision-Making or Profiling, Designation of Data Protection Officer, and the National Privacy Commission Seal of Registration. Sets the specific registration mechanics behind the Phase 0 compliance checklist's NPC-registration item.
- **NPC Circular No. 2023-06** — Security of Personal Data in the Government and Private Sector. Sets specific security obligations for government agencies, distinct from the general Act.

## Digital Identity

- **Republic Act No. 11055** — Philippine Identification System Act (PhilSys Act) (and Implementing Rules and Regulations)

## Electronic Transactions

- **Republic Act No. 8792** — Electronic Commerce Act of 2000

## Ease of Doing Business and Efficient Government Service Delivery

- **Republic Act No. 9485** — Anti-Red Tape Act of 2007. The original law that RA 11032 amended; cited here because RA 11032 is an amendment, not a standalone act, and its processing-time and Citizen's Charter obligations trace back to this Act.
- **Republic Act No. 11032** — Ease of Doing Business and Efficient Government Service Delivery Act of 2018 (and Implementing Rules and Regulations)

## Government Procurement

- **Republic Act No. 12009** — New Government Procurement Act (NGPA), effective August 2024
- **Implementing Rules and Regulations of RA No. 12009** — approved by the Government Procurement Policy Board under **GPPB Resolution No. 02-2025**, published February 10, 2025. Cited separately from the Act itself because bidding documents and Terms of Reference must be checked against the current IRR text, not just the Act.
- **Republic Act No. 9184** — Government Procurement Reform Act (repealed by RA 12009; applies transitionally for a three-year period to procurement not yet covered by NGPA's IRR)

## Government Digital Transformation Mandate

- **Republic Act No. 12254** — E-Governance Act, signed September 5, 2025
  - Section 40 establishes the **E-Government Interoperability Fund (EIF)**, a DICT-managed funding avenue (donations, grants, loans, PPP arrangements, Spectrum User Fees) potentially relevant to co-funding this platform.
  - The **Philippine Government Interoperability Framework (PGIF)** is established directly within RA 12254's own IRR (Section 16), not through a separate DICT Memorandum Circular. There is currently no standalone MC to cite for PGIF itself; it is a component of the IRR already cited above.
  - **Statutory deadline:** Sections 9(b) and 32 of the Act set the LGU digital-portal / eLGU adoption deadline at one (1) year from the *Act's own effectivity* (signed September 5, 2025; effective ~late September 2025) — placing the deadline at approximately **late September 2026**, not from the IRR's own effectivity date. See README.md, IT Governance Structure, for the full timeline correction and reasoning.
  - **Terminology note:** `eNGU` (electronic Next-Generation LGU platform) and `eBPLS` (electronic Business Permit and Licensing System) are not competing systems — eBPLS is the business-permit module within the broader eNGU/eLGU platform, which handles business applications, tax assessments, and clearances specifically. When a source refers to "the DICT rolling out eNGU," it means the whole platform; when a source refers to "LGUs must integrate eBPLS," it means specifically the business-permit module required to satisfy ARTA's eBOSS (Electronic Business One-Stop Shop) mandate. Sourced primarily to PIA's Nov 1, 2026 ARTA eBOSS deadline coverage; treat as a working clarification rather than a DICT-confirmed definition, given thinner secondary sourcing (including social-media posts) on the exact naming history and rollout timeline of "eNGU" as a next-generation rebrand of "eLGU."
- **MITHI Steering Committee Resolution No. 2025-05** — a 2025 directive prescribing a standards-based approach to information system harmonization and interoperability across government agencies, including LGUs, under the Medium-Term ICT Harmonization Initiative (MITHI). Sits one level below PGIF as an implementing instrument; relevant to this platform's API-first integration approach.

## Records Management

- **Republic Act No. 9470** — National Archives of the Philippines Act of 2007

## Accessibility and Inclusion

- **Republic Act No. 7277** — Magna Carta for Persons with Disabilities
  - as amended by **Republic Act No. 9442**
  - as amended by **Republic Act No. 10754**

## Cybersecurity and Critical Information Infrastructure

- **Republic Act No. 10175** — Cybercrime Prevention Act of 2012

## Transparency and Public Access to Information

- **Executive Order No. 2, s. 2016** — Freedom of Information (Executive Branch)

---

## Local Ordinances

The blueprint currently references "relevant Mandaluyong City ordinances" without citing specific ordinance numbers for most modules. The table below is the placeholder structure requested — populated where an official source was found, left blank where it wasn't.

| Ordinance No. | Title | Relevant Module(s) | Status |
|---|---|---|---|
| 484, S-2011 | Mandaluyong City Revenue Code of 2011 | Business Tax and Revenue Services, Real Property Tax | **Confirmed** — published on mandaluyong.gov.ph. Governs both business tax and real property tax; several sections since amended (see below). Still, confirm the current consolidated text with the City Legal Department before citing in procurement or Sanggunian submissions, since a codified LGU revenue code is routinely amended piecemeal. |
| 553-14 | Amending certain sections of Ordinance No. 484, S-2011 pertaining to real properties | Tax and Revenue Services | **Confirmed** (amendment only, not standalone) |
| 750-19 | Amending Sections 32, 37, 90, 116, and 121 of Ordinance No. 484, S-2011 | Tax and Revenue Services | **Confirmed** (amendment only, not standalone) |
| 906, S-2022 | Tax discounts on prompt payment of Real Property Tax, amending Ordinance No. 415, S-2008 and Section 13 of Ordinance No. 484, S-2011 | Tax and Revenue Services, Digital Documents (electronic receipts) | **Confirmed** (amendment only, not standalone) |
| *(not yet identified)* | Local data privacy or e-governance ordinance, if one exists | Data Privacy, Government Digital Transformation Mandate | **Not found.** Web search turned up only narrative references to the Sangguniang Panlungsod's "Digital Transformation Initiatives" (paperless sessions, e-legislation, online ordinance access) — no citable ordinance number specific to data privacy or e-governance was located. This may mean no such ordinance exists yet, or it exists but isn't indexed publicly. Confirm directly with the City Legal Department or the Sangguniang Panlungsod Secretary's Office. |
| *(not yet identified)* | Barangay Services–specific ordinance(s), if any | Barangay Services | **Not found** — not searched for specifically; add if the City Legal Department identifies one. |

**Action item:** obtain and add specific ordinance citations for the two "not yet identified" rows, and confirm whether Ordinance No. 484, S-2011 (as amended) is still the current consolidated Revenue Code in force, from:

- The City Legal Department, or
- The Sangguniang Panlungsod Secretary's Office

---

## Maintenance Notes

- **Latest update (v1.9.3):** removed a drifted, redundant date-comparison in README.md §19 (Legal and Regulatory Compliance) that duplicated §11's (IT Governance Structure) explanation of why the LGU portal deadline is measured from the Act's effectivity rather than its IRR's; §11 remains the single canonical explanation, with §19 now pointing back to it instead of restating a slightly different comparison. Fixed a stray typographic error in §11's deadline sentence. Added a terminology note clarifying `eNGU` vs. `eBPLS` under Government Digital Transformation Mandate, above.
- **Previous update:** added RA 9485 (Anti-Red Tape Act), NPC Circular No. 2022-04, NPC Circular No. 2023-06, the RA 12009 IRR (GPPB Resolution No. 02-2025), and MITHI Steering Committee Resolution No. 2025-05. Confirmed PGIF has no separate DICT MC of its own — it lives inside RA 12254's IRR, already cited under Government Digital Transformation Mandate.
- This list should be updated whenever README.md Section 19 changes.
- Legal applicability is reassessed at every Project Roadmap phase gate, not only at project initiation — laws, IRRs, and referenced national platforms may change over time.
- This file should be reviewed and confirmed by the City Government of Mandaluyong's Legal Office before being treated as authoritative.

---

