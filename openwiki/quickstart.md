---
type: policy-assembly
title: Coverage Wiki Quickstart
description: Route homeowners coverage and operational questions by line, state, effective date, declarations, and attachments. Use the 2026-01 water-backup route to separate issued contract wording from claims, underwriting, regulatory, and training guidance.
tags: [coverage, policy-assembly, claims, underwriting, water backup, navigation]
verified:
  - by: openwiki/0.6.1
    at: 2026-10-06T03:09:51.060Z
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
generated: { by: "openwiki/0.6.1", at: "2026-10-06T03:09:51.060Z" }
---

# Coverage Wiki Quickstart

This page is the entry point, not a substitute for an issued policy, endorsement, state form, claims procedure, underwriting rule, or rating procedure. Start with the policy facts, then follow the assembled contract and the separate operational route.

## Required route

```mermaid
flowchart TD
    Q["Question"] --> L["Line"]
    L --> S["State"]
    S --> D["Policy effective date"]
    D --> R["Declarations"]
    R --> A["Attached forms and endorsements"]
    A --> C["Governing contract wording"]
    C --> X{"Operational follow-up"}
    X --> CL["Claims"]
    X --> UW["Underwriting"]
    X --> RT["Rating or state controls"]
```

1. **Identify the line.** Begin with the applicable [HO-3 form page](coverage/forms/ho-3.md), or the relevant HO-4, HO-5, HO-6, or DP-3 form page when the risk is another line.
2. **Identify the state.** Check the applicable state overlay and attached amendatory form. A state form supplies contract wording only on the subjects it changes; a bulletin constrains issuance, disclosure, or administration and does not itself create coverage.
3. **Confirm the effective date.** Select the base form and endorsement edition by the policy date, then preserve the historical edition that governs an older policy. Do not substitute the newest repository file for the wording actually issued.
4. **Read the Declarations.** Capture selected limits, deductibles, schedules, and any state or endorsement entries.
5. **Verify attachments.** Confirm the complete, legible package is matched to the insured, location, subject, and policy term. A form label, quote, or system schedule is not proof that an endorsement attached.
6. **Read the governing contract.** Identify the coverage part, damaged interest, cause, exclusion, condition, limit, deductible, and settlement basis before branching to operations.

For composed answers, use [Policy Editions and State Attachments](policy-assembly/editions-and-state-attachments.md). Name the acting document and relationship—`supersedes`, `modifies`, `writes back`, `preserves`, `implements`, or `constrains`—and keep contract authority distinct from guidance.

## 2026-01 water-backup route

For a 2026 policy with attached HO 04 90, go from the [HO-3 form page](coverage/forms/ho-3.md) to [Water Backup and Sump Discharge](coverage/perils/water-backup.md), then confirm assembly in [Policy Editions and State Attachments](policy-assembly/editions-and-state-attachments.md).

<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-90/2026-01.md#L1-L23] heading anchor "L1-L23" does not exist in "../forms/HO/MS/HO-04-90/2026-01.md". Fix the href or restore the target, then delete this comment. -->
HO 04 90 (2026-01) attaches to HO-3 and modifies Section I—Exclusions A.3. For policies written on or after 2026-01-01 it replaces the 2010-10 edition. It covers direct physical loss to Coverage A, B, and C property from sewer or drain backup or sump, sump-pump, or related-equipment discharge or overflow, including mechanical breakdown. The default maximum is $10,000 for all endorsement loss in one policy period unless the Declarations show a higher limit; the sublimit is part of, not additional to, the Coverage A–C limits. A separate $1,000 deductible applies to each covered loss, instead of the Section I deductible. ([HO 04 90 2026-01](../forms/HO/MS/HO-04-90/2026-01.md#L1-L23))

<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-90/2026-01.md#L25-L56] heading anchor "L25-L56" does not exist in "../forms/HO/MS/HO-04-90/2026-01.md". Fix the href or restore the target, then delete this comment. -->
The endorsement preserves the HO-3 exclusions for flood, surface water, waves, tidal water, storm surge, body-of-water overflow, and below-ground water, including pressure, seepage, or leakage through a building, foundation, or pool. It also contains a known-maintenance condition and, where the residence has finished area below grade, requires an installed and operable backwater valve or equivalent device on the serving sewer line at the time of loss. Coverage A and B follow the attached policy’s settlement basis; Coverage C is actual cash value unless the endorsement Declarations say otherwise. ([HO 04 90 2026-01](../forms/HO/MS/HO-04-90/2026-01.md#L25-L56))

Do not apply those 2026 terms to 2010-10 or import 2027-01 wording into a 2026 policy. Confirm the edition and attachment in the issued package before applying the water-backup limit, deductible, device condition, or settlement rule.

## Choose the operational route

| Need | Route |
| --- | --- |
| Water-loss investigation, source, mitigation, evidence, coverage consultation, limits, or escalation | [Water Loss Claims Handling](claims/guidelines/water-loss-handling.md) |
| Water-peril classification or preserved flood and groundwater exclusions | [Claims Property Perils and Loss Types](claims/manual/property-perils-and-loss-types.md) |
| Attaching the endorsement, declared limit, deductible, device condition, or edition transition | [Endorsements and Deductibles](underwriting/manual/endorsements-and-deductibles.md) |
| Edition selection, complete package, Declarations, or state attachment | [Policy Editions and State Attachments](policy-assembly/editions-and-state-attachments.md) |

Claims guidance controls investigation and file handling; underwriting guidance controls eligibility, referral, authority, documentation, and attachment; neither creates, expands, restricts, or waives coverage. A bulletin, manual, memorandum, or training page may constrain or explain operations, but the issued HO-3, attached endorsement, Declarations, applicable state form, and law control the coverage result.

## Final check

Before publishing a position, verify line, state, effective date, Declarations, base edition, attached endorsement edition, state form, coverage part, damaged interest, cause, and evidence. Keep coverage, causation, scope and valuation, payment authority, eligibility, rating, and regulatory duties as separate work products. If the package, edition, attachment, cause, device evidence, or authority is incomplete or conflicting, hold the conclusion and obtain the missing record rather than guessing.

<!-- openwiki: broken internal link [../README.md#L13-L41] heading anchor "L13-L41" does not exist in "../README.md". Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [../README.md#L92-L95] heading anchor "L92-L95" does not exist in "../README.md". Fix the href or restore the target, then delete this comment. -->
The repository is synthetic: forms and bulletins are frozen authority, while manuals and guidelines are living internal guidance. The evidence path preserves line, state, form, and edition context, so use canonical repository citations when documenting the conclusion. ([repository layout and lifecycle](../README.md#L13-L41), [document relationships](../README.md#L92-L95))
