# MapMyRun Quality Investigation
## Assessment brief

Michael D. Jensen | Independent field investigation | August 2026

An Outside job application asked about MapMyRun's biggest current quality issues. I used the weekend to investigate the product rather than submit an opinion without evidence. The work produced a positive resilience result and a separate question about workout-record integrity. This sample cannot rank the product's biggest issues.

## Two tracks, different conclusions

| Track | Recorded observation | Supported conclusion |
| --- | --- | --- |
| Workout integrity | Two active Run sessions included known vehicle travel. One recorded a 2:02 mile. | A foreseeable unended-session mistake can produce misleading workout performance. Product intent and the appropriate response remain open. |
| GPS / device resilience | Three Gold Camp Road walks crossed Tunnel #1 twice each under different phone / Watch conditions. All saved and remained physically plausible. | Positive evidence of resilience under the tested conditions. This does not measure GPS accuracy or establish general reliability. |

## The quality question

What should the product do when a predictable user mistake creates a convincing but misleading activity record? Recording movement until the user ends a session may be intentional. Whether users can recognize, understand, and repair the result is a separate product-quality question.

Apple Health was later observed displaying affected activity in a daily view. That is a downstream user-trust signal; the synchronization timing, transformations, responsible component, and wider impact were not established.

## What I would do next

- Explore recovery: can users identify, trim, relabel, or otherwise correct the affected workout?
- Check downstream correction: does correcting the workout change what appears in Apple Health?
- Establish importance: what further evidence about repeatability, impact, and existing recovery would justify treating this as a significant quality issue?

These are follow-up questions, not completed tests or recommendations for a particular feature.

## Evidence and scope

The original assessments date the field work August 22-23, 2026. Measurements in this revision are transcribed from those assessments; raw sensor samples and original workout screenshots are not archived in this repository. No new field tests were run for this presentation revision. Root cause, population frequency, an implementation defect, and the best intervention remain unproven.

Full methods, recorded measurements, and limitations: docs/assessment.md in github.com/jensenmd/mapmyrun-quality-investigation.
