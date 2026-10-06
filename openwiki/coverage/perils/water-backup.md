---
type: coverage
title: Water Backup and Sump Discharge
description: HO 04 90 (2026-01) coverage for sewer or drain backup and sump discharge or overflow, including its $10,000 default sublimit, separate deductible, below-grade backflow-device condition, loss settlement, and preserved flood and groundwater exclusions.
tags: [water backup, sump discharge, HO-3, HO 04 90, property coverage]
verified:
  - by: openwiki/0.6.1
    at: 2026-10-06T03:09:51.060Z
sources:
  - id: openwiki-source-6f2e8c6b93df2e40df6addd5
    resource: repo://bulletins/IL/idoi-2017-10-water-backup-disclosure.md
  - id: openwiki-source-0ac4f0d1fc1220eee9804cfe
    resource: repo://forms/DP/MS/DP-04-95/2021-05.md
  - id: openwiki-source-d7e85cf3e721d2c3c6ee885c
    resource: repo://forms/DP/MS/DP-3/2026-01.md
  - id: openwiki-source-cd26c30cc942869b52618f95
    resource: repo://forms/HO/MS/HO-04-90/2010-10.md
  - id: openwiki-source-36bcf8e9754ce8cd9b63db52
    resource: repo://forms/HO/MS/HO-04-90/2026-01.md
  - id: openwiki-source-6a71dbfe57881e21b8a0e5ea
    resource: repo://forms/HO/MS/HO-04-90/2027-01.md
  - id: openwiki-source-57869e6df01fc9fc3871c8c7
    resource: repo://forms/HO/MS/HO-04-91/2019-03.md
  - id: openwiki-source-0d3aa2bf4068eeb7ad43e12e
    resource: repo://forms/HO/MS/HO-04-92/2019-03.md
  - id: openwiki-source-7176aead92778c93cb0441d2
    resource: repo://forms/HO/MS/HO-3/2024-03.md
  - id: openwiki-source-ea6397bf6ad5bac1c652ab3a
    resource: repo://forms/HO/MS/HO-4/2021-10.md
  - id: openwiki-source-25d651d4a45fc0fd8ab047e2
    resource: repo://forms/HO/MS/HO-5/2022-06.md
  - id: openwiki-source-9a3362ddf208da1fe1570617
    resource: repo://forms/HO/MS/HO-6/2023-02.md
  - id: openwiki-source-d3cc221b966da1c2185d5b2f
    resource: repo://memoranda/HO-04-90-2027-01.md
  - id: openwiki-source-98a0b702206aa7ec38174d58
    resource: repo://training/water-losses-101.md
generated: { by: "openwiki/0.6.1", at: "2026-10-06T03:09:51.060Z" }
---

# Water Backup and Sump Discharge

## At a glance

HO 04 90 (2026-01) is an HO-3 endorsement. It replaces the 2010-10 edition for policies written on or after **2026-01-01** and modifies **HO-3 Section I—Exclusions A.3**. It covers direct physical loss to property described in Coverages A, B, and C when water backs up through a sewer or drain, or overflows or is discharged from a sump, sump pump, or related equipment. The endorsement expressly applies whether or not the backup, overflow, or discharge results from mechanical breakdown of that equipment. Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L1-L11`

The default maximum is **$10,000 for all loss under the endorsement in one policy period**, unless the Declarations show a higher endorsement limit. The sublimit is part of—not additional to—the Coverage A, B, and C limits. A **separate $1,000 deductible applies to each loss**; the Section I deductible does not apply to loss covered by this endorsement. Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L13-L23`

## Coverage relationship to HO-3 exclusions

The endorsement acts on the HO-3 water exclusions rather than replacing the policy wholesale:

- **Writes back:** limited coverage for the defined sewer/drain backup and sump discharge or overflow, to the extent stated in HO 04 90.
- **Preserves:** Section I—Exclusions A.1 for flood, surface water, waves, tidal water, storm surge, and overflow of a body of water; and A.2 for water below the surface of the ground, including water exerting pressure on or seeping or leaking through a building, foundation, or pool. The endorsement states, “Section I — Exclusions A.1 continues to apply in full” and “Section I — Exclusions A.2 continues to apply in full.” Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L25-L33`
- **Modifies:** Section I—Exclusions A.3 only to the extent necessary to provide this endorsement’s stated water-backup and sump-discharge coverage. All other policy provisions continue to apply. Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L1-L4`, `repo://forms/HO/MS/HO-04-90/2026-01.md#L49-L56`

The HO-3 base form confirms the boundary: sewer or drain backup is excluded unless a water-backup endorsement is attached, and sump discharge or overflow is separately excluded. Its reference to a “backup and sump overflow limit” does not itself create coverage. Source: `repo://forms/HO/MS/HO-3/2024-03.md#L593-L601`

## Decision flow

```mermaid
flowchart TD
  A["Identify the water path"] --> B{"Backup or sump event?"}
  B -->|"Sewer or drain"| C["Test HO 04 90 attachment and A.3 write-back"]
  B -->|"Sump discharge or overflow"| C
  B -->|"Flood or groundwater"| D["Apply preserved A.1 or A.2 exclusion"]
  C --> E{"Finished area below grade?"}
  E -->|"Yes"| F["Verify operable backwater valve or equivalent device"]
  E -->|"No"| G["Apply maintenance condition and policy terms"]
  F --> G
  G --> H["Determine direct physical loss"]
  H --> I["Apply $10,000 default sublimit and $1,000 separate deductible"]
  I --> J["Settle A/B by policy basis and C at ACV unless declarations say otherwise"]
```

*This flow separates the covered path from the flood and groundwater exclusions, then applies the new device condition and settlement rules.*

## Conditions that decide a 2026-01 claim

### Known maintenance failure

The maintenance condition is controlling and should be quoted, not softened into a general “maintenance issue” rule: **“We do not cover loss under this endorsement if the backup, overflow, or discharge resulted from an insured's failure to maintain the sewer line, drain, sump, or sump pump serving the residence premises, where that failure was known to the insured before the loss and a reasonable person would have remedied it.”** Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L35-L40`

The condition requires all of the stated elements: an insured’s failure to maintain a listed system, knowledge before the loss, and a condition a reasonable person would have remedied. It is not a blanket exclusion for every equipment malfunction.

### New below-grade backflow-device requirement

Where the residence premises has a **finished area below grade**, coverage applies only if **“a backwater valve or equivalent backflow prevention device was installed and operable on the sewer line serving the premises at the time of loss.”** The form expressly says this requirement is new in 2026-01 and did not appear in 2010-10. Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L42-L47`

Investigation should therefore establish whether a finished below-grade area existed, identify the device serving the premises, and document its installation and operability at the time of loss. Installing a device after the event does not establish the condition at the time of loss.

### Loss settlement

The endorsement does not create one universal valuation basis. **Coverage A and Coverage B** property is settled “on the basis stated in the policy to which this endorsement attaches.” **Coverage C** property is settled at **actual cash value**, even if a replacement-cost personal-property endorsement exists, unless the Declarations state otherwise for this endorsement. Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L49-L54`

Thus, the endorsement sublimit is a ceiling on the covered loss; it is not a replacement-cost promise. Determine the applicable policy valuation first, then apply exclusions, the $10,000 default sublimit or declared higher limit, and the separate $1,000 deductible.

## What is and is not within the grant

The covered event is water or waterborne material that backs up through sewers or drains, or water that overflows or is discharged from a sump, sump pump, or related equipment. The 2026 wording does not remove the need to establish direct physical loss to insured Coverage A, B, or C property. Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L6-L11`

The endorsement does **not** write back:

- flood, surface water, waves, tidal water, storm surge, or body-of-water overflow;
- water below ground, including pressure, seepage, or leakage through a building, foundation, or pool;
- a loss failing the quoted known-maintenance condition; or
- a loss at a residence with a finished below-grade area when the required backflow device was not installed and operable at the time of loss.

Those boundaries are not merely claims preferences: A.1 and A.2 are expressly preserved, and W.5 and W.6 state the additional endorsement conditions. Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L25-L47`

## 2010-10 and 2027-01 distinction

Do not backdate the 2026 terms or import the 2027 terms into a different policy. The 2026 form says it replaces 2010-10 for policies written on or after 2026-01-01. The older edition therefore cannot be assigned the 2026 $10,000 sublimit, separate $1,000 deductible, below-grade device condition, or Coverage C settlement rule without the governing policy text. Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L1-L4`, `repo://forms/HO/MS/HO-04-90/2010-10.md#L1-L9`

The repository also contains a distinct 2027-01 endorsement. It has a different, substantially expanded structure and states that it applies only when attached, controls conflicts, and leaves unmodified policy provisions unchanged. Treat it as a separate edition, not as interpretive text for 2026-01. Source: `repo://forms/HO/MS/HO-04-90/2027-01.md#L14-L39`

## Claim-handling checklist

1. Confirm the HO-3 edition, the HO 04 90 edition, attachment, declarations, and loss date.
2. Establish the path: sewer/drain backup, sump discharge or overflow, flood, groundwater, or another source.
3. Identify damaged property as Coverage A, B, or C and determine the policy valuation basis.
4. For a finished below-grade area, document the backwater valve or equivalent device and its operability at the time of loss.
5. Investigate the sewer, drain, sump, and pump maintenance history, including whether a correctable condition was known before the loss.
6. Apply preserved A.1 and A.2 exclusions before applying the endorsement sublimit and separate deductible.
7. Apply the default $10,000 policy-period sublimit unless the Declarations show a higher endorsement limit; then apply the $1,000 deductible to each covered loss.

The endorsement says all other policy provisions apply, so ordinary notice, mitigation, inspection, proof, and cooperation duties remain relevant even though they are not rewritten by this short endorsement. Source: `repo://forms/HO/MS/HO-04-90/2026-01.md#L49-L56`
