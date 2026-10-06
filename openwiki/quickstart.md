---
type: policy-assembly
title: Coverage Wiki Quickstart
description: Route a homeowners coverage or operations question through the issued line, state, effective date, declarations, and attachments. Use this map to select HO 04 90 editions and follow water-backup issues into contract, assembly, claims, and state-overlay guidance.
tags: [coverage, policy-assembly, claims, water-backup, state-overlays, navigation]
verified:
  - by: openwiki/0.6.1
    at: 2026-10-06T21:23:18.164Z
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
  - id: openwiki-source-36bcf8e9754ce8cd9b63db52
    resource: repo://forms/HO/MS/HO-04-90/2026-01.md
  - id: openwiki-source-6a71dbfe57881e21b8a0e5ea
    resource: repo://forms/HO/MS/HO-04-90/2027-01.md
  - id: openwiki-source-5802aac0ff04777c19a4717f
    resource: repo://forms/HO/MS/HO-23-74/2025-05.md
  - id: openwiki-source-7176aead92778c93cb0441d2
    resource: repo://forms/HO/MS/HO-3/2024-03.md
  - id: openwiki-source-0d6a76164fce2d196a0998b8
    resource: repo://forms/HO/NY/HO-01-31/2016-04.md
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
generated: { by: "openwiki/0.6.1", at: "2026-10-06T21:23:18.164Z" }
---

# Coverage Wiki Quickstart

This is a compact routing map, not a substitute for the issued policy, endorsement, declarations, state form, bulletin, or internal procedure. Forms and bulletins are frozen authority; manuals and guidelines are living operational guidance; memoranda and training explain or organize review but do not create coverage ([source roles](repo://README.md#L13-L41)).

## Start with the issued package

Before interpreting a loss, record the line, state, policy-effective date, declarations, base-form edition, attached endorsements, schedules, state form, and damaged property. The repository path carries line, state, form, and edition context, so do not replace the issued wording with the newest repository file or a familiar form title ([repository model](repo://README.md#L26-L31)).

```mermaid
flowchart TD
  Q["Coverage or operations question"] --> A["Line and state"]
  A --> D["Policy-effective date and declarations"]
  D --> E["Select frozen base and endorsement editions"]
  E --> T{"Complete attachment verified?"}
  T -->|"no"| H["Hold interpretation and obtain issued package"]
  T -->|"yes"| C["Read base form with acting endorsement"]
  C --> S["Apply attached state contract form"]
  S --> R{"Operational route needed?"}
  R -->|"claim"| CL["Claims guidance and manual"]
  R -->|"disclosure or state duty"| ST["State overlay or bulletin"]
  R -->|"binding or referral"| UW["Underwriting authority"]
```

*Caption: Date and attachment select the contract; state and operational materials are applied separately.*

<!-- openwiki: broken internal link [policy-assembly/editions-and-state-attachments.md#L15-L24] heading anchor "L15-L24" does not exist in "policy-assembly/editions-and-state-attachments.md". Fix the href or restore the target, then delete this comment. -->
Use [Policy Editions, Endorsements, and State Attachments](policy-assembly/editions-and-state-attachments.md) for the assembly record and failure controls. A state amendatory form supplies contract wording when attached; a bulletin constrains disclosure or administration; internal guidance constrains carrier action. None silently changes the issued contract ([authority boundaries](policy-assembly/editions-and-state-attachments.md#L15-L24)).

## Choose the HO 04 90 edition

<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-90/2026-01.md#L1-L4] heading anchor "L1-L4" does not exist in "../forms/HO/MS/HO-04-90/2026-01.md". Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [README.md#L33-L37] file "README.md" does not exist. Fix the href or restore the target, then delete this comment. -->
The **HO 04 90 2026-01 endorsement replaces HO 04 90 2010-10 for policies written on or after 2026-01-01**. The earlier frozen edition remains applicable to policies written under it; do not import the 2026 deductible, sublimit, conditions, or settlement rule into an earlier policy ([2026-01](../forms/HO/MS/HO-04-90/2026-01.md#L1-L4); [edition lifecycle](README.md#L33-L37)). A later edition is not retroactive: select the edition whose effective interval and issued package govern.

<!-- openwiki: broken internal link [../forms/HO/MS/HO-3/2024-03.md#L593-L601] heading anchor "L593-L601" does not exist in "../forms/HO/MS/HO-3/2024-03.md". Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-90/2026-01.md#L1-L11] heading anchor "L1-L11" does not exist in "../forms/HO/MS/HO-04-90/2026-01.md". Fix the href or restore the target, then delete this comment. -->
For HO-3 water-backup questions, the base form excludes sewer/drain backup and sump discharge unless the applicable endorsement is attached. **HO 04 90 2026-01 modifies HO-3 2024-03** by writing back direct physical loss to Coverage A, B, and C property from sewer/drain backup or sump discharge/overflow, including where mechanical breakdown caused the event ([HO-3 exclusion](../forms/HO/MS/HO-3/2024-03.md#L593-L601); [2026-01 grant](../forms/HO/MS/HO-04-90/2026-01.md#L1-L11)).

<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-90/2026-01.md#L13-L23] heading anchor "L13-L23" does not exist in "../forms/HO/MS/HO-04-90/2026-01.md". Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-90/2026-01.md#L25-L56] heading anchor "L25-L56" does not exist in "../forms/HO/MS/HO-04-90/2026-01.md". Fix the href or restore the target, then delete this comment. -->
The 2026-01 endorsement provides a shared **$10,000 per-policy-period sublimit**, unless the Declarations show more, and a separate **$1,000 deductible per endorsement loss**; the sublimit is part of the Coverage A/B/C limits and the Section I deductible does not apply ([2026-01 limits](../forms/HO/MS/HO-04-90/2026-01.md#L13-L23)). It **preserves** flood, surface-water, and below-surface-water exclusions, **conditions** coverage on a known, remediable maintenance failure not causing the loss, and requires an installed and operable backwater valve or equivalent for a finished below-grade area. Coverage A/B use the policy settlement basis; Coverage C is ACV unless the Declarations say otherwise ([2026-01 exclusions and conditions](../forms/HO/MS/HO-04-90/2026-01.md#L25-L56)).

<!-- openwiki: broken internal link [policy-assembly/editions-and-state-attachments.md#L26-L49] heading anchor "L26-L49" does not exist in "policy-assembly/editions-and-state-attachments.md". Fix the href or restore the target, then delete this comment. -->
Verify that the complete endorsement is actually attached and matched to the insured, location, subject, and policy term. A schedule label alone is not the operative endorsement. If the package is incomplete or conflicting, hold interpretation and obtain the issued copy or escalate ([attachment workflow](policy-assembly/editions-and-state-attachments.md#L26-L49)).

## Follow a water-backup issue

Open [Water Backup and Sump Discharge Coverage](coverage/perils/water-backup.md) to establish the water path, covered property, base exclusion, acting endorsement, edition-specific limit, deductible, conditions, and settlement. Do not treat a visible stain, water near a drain, or a limit reference in the base form as proof of backup coverage.

<!-- openwiki: broken internal link [claims/guidelines/water-loss-handling.md#L34-L46] heading anchor "L34-L46" does not exist in "claims/guidelines/water-loss-handling.md". Fix the href or restore the target, then delete this comment. -->
Then open [Water Loss Handling](claims/guidelines/water-loss-handling.md) for the operational sequence: safe mitigation, evidence preservation, source/path/duration investigation, exact policy consultation, separate scope and valuation, authority review, payment, recovery, and closure. Claims guidance does not create coverage; the attached policy, endorsement, declarations, and applicable law control ([claims boundary](claims/guidelines/water-loss-handling.md#L34-L46)).

For a claim, keep these questions separate:

- **Cause and path:** sewer/drain reverse flow, sump discharge, plumbing discharge, flood, surface water, or subsurface water.
- **Contract:** covered property, grant, exclusion, condition, limit, deductible, and settlement basis in the governing edition.
- **Operations:** mitigation, evidence, notice, escalation, payment, recovery, and closure under claims guidance.
- **State control:** disclosure, claims, filing, or other duties under the applicable overlay or bulletin.

## State and operational routes

<!-- openwiki: broken internal link [policy-assembly/editions-and-state-attachments.md#L67-L73] heading anchor "L67-L73" does not exist in "policy-assembly/editions-and-state-attachments.md". Fix the href or restore the target, then delete this comment. -->
Return to [Policy Editions, Endorsements, and State Attachments](policy-assembly/editions-and-state-attachments.md) when the answer involves a state attachment or edition conflict. For Illinois, use [Illinois State Overlay](state-overlays/illinois.md): the bulletin constrains disclosure and claims handling, while the attached state form modifies the contract only within its terms. A disclosure amount or claims rule is not a universal policy limit or coverage grant ([Illinois boundary](policy-assembly/editions-and-state-attachments.md#L67-L73)).

Use the claims, underwriting, and rating pages only after the contract route is established. Internal authority or referral thresholds govern who may act; they are not policy limits. If attachment, causation, edition, valuation, authority, or regulatory facts remain unresolved, document the gap and escalate rather than guess.

## Final routing checklist

1. Identify line, state, effective date, declarations, and damaged interest.
2. Select the governing frozen base and endorsement editions.
3. Verify the complete attachment and reconcile schedules with the issued package.
4. Read the acting endorsement with the base form; name the acting document and use precise relationships such as `modifies`, `preserves`, or `writes back`.
5. Apply state contract forms, bulletins, claims guidance, underwriting guidance, and rating controls in their separate roles.
6. Record the exact evidence and escalate unresolved issues.
