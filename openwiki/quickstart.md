---
type: concept
title: Coverage Wiki Quickstart
description: Compact routing map for coverage and operational questions across line, state, effective date, policy editions, endorsements, claims, underwriting, and rating. Use it to locate the updated HO-3 water-backup and policy-assembly guidance without treating operational material as contract wording.
tags: [coverage, policy-assembly, claims, underwriting, state-overlays, navigation]
verified:
  - by: openwiki/0.6.1
    at: 2026-10-08T18:16:34.451Z
sources:
  - id: openwiki-source-7dd90be03dbdd65accd7c766
    resource: repo://bulletins/CA/cdi-2022-03-earthquake-offer.md
  - id: openwiki-source-cf3bdf4919dc01656b85cad5
    resource: repo://bulletins/FL/oir-2022-01-hurricane-deductible.md
  - id: openwiki-source-3bd145be9dd2d256294b3e9a
    resource: repo://bulletins/NC/ncdoi-2021-06-claims-handling.md
  - id: openwiki-source-d2d0e0eee59ab93741467060
    resource: repo://bulletins/TX/b-2019-02-prompt-payment.md
  - id: openwiki-source-38049e374f54d1eb9a15f4ef
    resource: repo://bulletins/TX/b-2021-08-windstorm-deductibles.md
  - id: openwiki-source-cd26c30cc942869b52618f95
    resource: repo://forms/HO/MS/HO-04-90/2010-10.md
  - id: openwiki-source-36bcf8e9754ce8cd9b63db52
    resource: repo://forms/HO/MS/HO-04-90/2026-01.md
  - id: openwiki-source-6a71dbfe57881e21b8a0e5ea
    resource: repo://forms/HO/MS/HO-04-90/2027-01.md
  - id: openwiki-source-5802aac0ff04777c19a4717f
    resource: repo://forms/HO/MS/HO-23-74/2025-05.md
  - id: openwiki-source-e727058d16eee86c951e380a
    resource: repo://forms/HO/MS/HO-3/2011-05.md
  - id: openwiki-source-f4ebd2ece3eaf490178dfc41
    resource: repo://forms/HO/MS/HO-3/2018-09.md
  - id: openwiki-source-7176aead92778c93cb0441d2
    resource: repo://forms/HO/MS/HO-3/2024-03.md
  - id: openwiki-source-0d6a76164fce2d196a0998b8
    resource: repo://forms/HO/NY/HO-01-31/2016-04.md
  - id: openwiki-source-ff7de1315ac46ce4dd65d251
    resource: repo://forms/HO/TX/HO-01-45/2022-01.md
  - id: openwiki-source-1a7fd187295c6f9ef57d73cb
    resource: repo://guidelines/appetite/ca-homeowners.md
  - id: openwiki-source-243115596013c4ec281c4a90
    resource: repo://guidelines/appetite/fl-homeowners.md
  - id: openwiki-source-1a23ac5f105f70e05c6ce688
    resource: repo://guidelines/appetite/la-homeowners.md
  - id: openwiki-source-b4a32c6164f88c97824a6cfb
    resource: repo://guidelines/appetite/nc-homeowners.md
  - id: openwiki-source-ff8a10adb5aaa9d147aa506d
    resource: repo://guidelines/appetite/ny-homeowners.md
  - id: openwiki-source-da67a262bebb42780999bd2a
    resource: repo://guidelines/appetite/tx-homeowners.md
  - id: openwiki-source-e3f8eeadc60c530791e87a00
    resource: repo://guidelines/authority/binding-authority.md
  - id: openwiki-source-b835c3d80d50a5ec159c2c2a
    resource: repo://guidelines/claims/liability-claim-handling.md
  - id: openwiki-source-826017f9c17ff1c446a5e4f6
    resource: repo://guidelines/claims/mold-claim-handling.md
  - id: openwiki-source-98996e9748507677077d5997
    resource: repo://guidelines/claims/roof-claim-handling.md
  - id: openwiki-source-fe5cf28f9b15285dd496cba1
    resource: repo://guidelines/claims/water-loss-handling.md
  - id: openwiki-source-77e27410bda4d59c2b779d5e
    resource: repo://manuals/claims/manual.md
  - id: openwiki-source-add01ee6690ea277c5253419
    resource: repo://manuals/rating/manual.md
  - id: openwiki-source-2b86de67275893a8b33d953b
    resource: repo://manuals/underwriting/manual.md
  - id: openwiki-source-9a9291b2de270f91ca242ea5
    resource: repo://memoranda/HO-3-2024-03.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
  - id: openwiki-source-d2ea423343a02d2233c77383
    resource: repo://training/attaching-endorsements.md
  - id: openwiki-source-8460fe3c58470ce6ec8d9b51
    resource: repo://training/choosing-the-governing-edition.md
  - id: openwiki-source-a6e7a7f52df2ed58605a3898
    resource: repo://training/guidance-versus-contract.md
generated: { by: "openwiki/0.6.1", at: "2026-10-08T18:16:34.451Z" }
---

# Coverage Wiki Quickstart

Use this page to route a question; do not treat it as a substitute for the issued policy, attached endorsements, applicable state form, law, or operating manual. The repository separates frozen forms and bulletins from living manuals and guidelines, while memoranda and training explain rather than replace operative wording ([document families](repo://README.md#L15-L27)).

## The shortest safe route

```mermaid
flowchart TD
  Q[Coverage or operational question] --> L[Identify line]
  L --> S[Identify state]
  S --> D[Confirm policy-effective date]
  D --> P[Read Declarations and complete issued package]
  P --> F[Select governing base form and attachments]
  F --> C[Read contract wording and state form]
  C --> R{Operational follow-up}
  R --> CL[Claims]
  R --> UW[Underwriting and authority]
  R --> RT[Rating]
```

1. Record the **line, state, policy-effective date, Declarations, coverage part, damaged interest, and reported cause**.
2. Select the base-form edition whose effective interval contains the policy date. Older frozen editions remain relevant to policies written under them; do not substitute the newest repository file ([frozen authority](repo://README.md#L33-L41)).
3. Verify every referenced page, schedule, endorsement, and state amendatory form is actually attached and matched to the insured, location, property, and term. If the package is incomplete or labels conflict, hold the conclusion and obtain the issued wording ([attachment workflow](repo://training/attaching-endorsements.md#L65-L87)).
4. Read the assembled contract first, then branch to claims, underwriting, rating, or state operations. A bulletin, memorandum, training page, manual, or appetite guide cannot silently create, restrict, or waive coverage ([guidance boundary](repo://training/guidance-versus-contract.md#L61-L83)).

## Route by domain

| Need | Start here | Then verify |
| --- | --- | --- |
| Homeowners dwelling, property, liability, or form edition | [HO-3 Homeowners Form Editions](coverage/forms/ho-3.md) | Exact base edition, Coverage A–F, exclusions, conditions, and attachments |
| Sewer, drain, or sump backup | [Water Backup and Sump Discharge Coverage](coverage/perils/water-backup.md) | Attached HO 04 90 edition, water path, exclusions, limit, deductible, and maintenance facts |
| Composing forms and state attachments | [Policy Editions, Endorsements, and State Attachments](policy-assembly/editions-and-state-attachments.md) | Effective date, Declarations, complete package, precedence, and state form |
| Claim intake, investigation, mitigation, or closure | [Intake, Investigation, and Mitigation](claims/manual/intake-investigation-and-mitigation.md) | Contract route first; then cause, scope, evidence, authority, and applicable state procedure |
| Underwriting endorsements or deductibles | [Endorsements and Deductibles](underwriting/manual/endorsements-and-deductibles.md) | Internal eligibility, referral, evidence, and attachment controls—not coverage terms |
| State-specific contract and operations | [Texas State Overlay](state-overlays/texas.md) or the relevant [state-overlay directory](state-overlays/) | State amendatory form as contract wording; bulletin as regulatory constraint |
| Rating inputs and adjustments | [Rating Inputs and Adjustments](underwriting/rating/inputs-and-adjustments.md) | Complete submission, approved calculation, evidence, and state exceptions |

## Important current routes

### HO-3 and water backup

For a policy written on or after **2026-01-01**, use HO 04 90 2026-01 only when it is attached; it replaces the 2010-10 endorsement for that policy population. The endorsement provides a default **$10,000 policy-period sublimit** and a separate **$1,000 deductible per loss**, while preserving the HO-3 flood, surface-water, and subsurface-water exclusions and imposing its stated maintenance and below-grade backflow-prevention conditions ([2026-01 endorsement](repo://forms/HO/MS/HO-04-90/2026-01.md#L1-L47)). Do not carry those terms into a policy governed by HO 04 90 2010-10, and do not infer attachment from a system label alone.

The HO-3 base edition remains date-sensitive: 2011-05 applies before 2018-09-01, 2018-09 applies from 2018-09-01 through 2024-02-29, and 2024-03 applies from 2024-03-01 onward, subject to the issued policy record ([HO-3 edition headers](repo://forms/HO/MS/HO-3/2011-05.md#L2-L9), [HO-3 2018-09](repo://forms/HO/MS/HO-3/2018-09.md#L2-L9), [HO-3 2024-03](repo://forms/HO/MS/HO-3/2024-03.md#L2-L8)).

### State, claims, and underwriting boundaries

A state amendatory form is contract language; a regulator bulletin constrains issuance, disclosure, rating, claims, or administration. For example, Texas HO 01 45 implements the state deductible mechanism, while Bulletin B-2021-08 governs disclosure and administration; neither should be substituted for the other ([Texas form](repo://forms/HO/TX/HO-01-45/2022-01.md#L13-L23), [Texas bulletin](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L47-L73)).

Claims guidance controls file handling, evidence, investigation, mitigation, payment, and closure after the contract route is established. Underwriting guidance controls eligibility, referrals, authority, and whether an endorsement may attach. Keep coverage, causation, scope, valuation, payment authority, eligibility, and rating as separate work products ([claims manual](repo://manuals/claims/manual.md#L13-L19), [underwriting manual](repo://manuals/underwriting/manual.md#L21-L43)).

## Final check

Before publishing a position, confirm the governing edition and attachment package, read the applicable state wording, cite the operative form and narrow evidence lines, and escalate unresolved attachment, causation, valuation, authority, or regulatory conflicts. Use memoranda to understand edition changes, not to rewrite the filed form ([citation conventions](repo://README.md#L53-L60)).
