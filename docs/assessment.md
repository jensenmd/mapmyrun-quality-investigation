# MapMyRun Quality Investigation
## 1. Challenge, scope, and method

Michael D. Jensen | Independent external assessment | August 2026

### Why I did the work

An application for a role at Outside supporting MapMyFitness prompted this investigation. I recall the question as: "What are the biggest quality issues with MapMyRun currently?" The original application text is not archived here, so this is recalled wording.

I chose to investigate before answering. The available time was a weekend, with personal iPhone and Apple Watch devices, nearby Gold Camp Road tunnels, and access to the product as an ordinary user. I had no internal requirements, source code, logs, telemetry, or product history. The useful goal was to demonstrate judgment through a focused assessment; the sample could not establish the product's biggest issues.

### Two independent tracks

Ordinary use produced an accidental pedestrian-to-vehicle observation, followed by a focused follow-up. Separate tunnel walks explored resilience under GPS obstruction and different phone / Watch conditions. These are different experiments; the tunnel results do not explain the vehicle-transition records.

| Record | Condition | Purpose |
| --- | --- | --- |
| SAT-WM | Run left active during pedestrian activity and known driving | Accidental workout-integrity observation |
| SUN-WM | Follow-up with walking, driving, stops, shopping; Auto-Pause on, Watch worn | Examine a similar transition deliberately |
| GC-01 | iPhone-started; phone carried; Watch worn | Phone-started recording under obstruction |
| GC-02 | Watch-started; powered-on phone left at start | Recording without the phone carried |
| GC-03 | Watch-started; phone powered off and left at start | Recording without an available paired phone |

Each Gold Camp walk crossed Tunnel #1, continued beyond it, reversed, and crossed back: six passages across three walks. Endpoints and execution length were not controlled precisely enough to isolate distance accuracy. The conditions describe how sessions were started; they do not prove which sensor or component supplied each value.

### Evidence provenance

The original assessments date field work August 22-23, 2026 and interpretation revision August 30. This October 15 presentation revision preserves their measurements and record IDs. The original application, field notes, workout screenshots, app / OS version record, and raw sensor samples are not archived in this repository. The tables are transcriptions of the prior assessments, not a newly revalidated raw dataset. Original PDF hashes are retained in docs/revision-notes.md. No new field execution occurred.

<!-- pagebreak -->

## 2. Recorded observations

### Workout integrity: known vehicle travel in Run records

| Measurement | SAT-WM | SUN-WM |
| --- | --- | --- |
| Saved distance | 5.64 mi | 5.25 mi |
| Saved duration | 1:18:12 | 29:21 |
| Reported vehicle-scale pace | 2:02 mile | 2:16-2:20 miles; 1:30 max pace |
| Average heart rate | 85 bpm | 100 bpm |
| Average cadence | 82 spm | 94 spm |
| Session state | Not reconstructed | Auto-Pause on; paused state observed |

The prior assessment also records Sunday mile 2 as 2:16/mi with heart rate 84 bpm and cadence 98 spm. Combined with known driving, these values support the observation that vehicle movement entered a Run record. The provenance, timing alignment, and intended semantics of each sensor value were not independently established.

An unended session is a plausible explanation for the broad behavior. This does not establish a faulty GPS algorithm, a broken pause implementation, or a violated product requirement. The recovery workflow was not evaluated comprehensively.

### Resilience: three plausible saved tunnel walks

| Measurement | GC-01 | GC-02 | GC-03 |
| --- | --- | --- | --- |
| Duration | 18:25 | 20:15 | 21:34 |
| Distance | 0.91 mi | 1.00 mi | 1.07 mi |
| Average pace / mi | 20:07 | 20:18 | 20:05 |
| Average heart rate | 125 bpm | 124 bpm | 124 bpm |
| Cadence | 94 spm | 92 spm | 94 spm |

The original reports describe transient GPS noise but successful saves and physically plausible workout summaries in all three conditions. That is useful positive evidence for this limited field sample. Without raw samples or a reference route measurement, it does not establish location accuracy, the signal source in the tunnel, or a particular fallback mechanism.

The 0.91-1.07 mile spread is not distance-defect evidence by itself: durations also increased, average pace stayed similar, and exact endpoints were not controlled. There was one walk per condition, one participant, and one device ecosystem.

<!-- pagebreak -->

## 3. Interpretation and user trust

### Requirements compliance and product quality

Recording movement until a user ends a workout may be intentional. The product-quality question is whether a foreseeable mistake deserves better prevention, detection, explanation, or recovery. A precise-looking record can be misleading even when recording behaved as intended.

![Workout record and downstream trust boundary](../Michael_Jensen_MapMyRun_Apple_Health_User_Trust.png)

The later Apple Health daily-view observation supports a downstream trust concern. It does not establish exact sync timing, field mapping, which component contributed each value, or how a corrected source record would propagate. The illustration distinguishes reported observations from the unverified processing boundary; it is not a verified system architecture.

<!-- pagebreak -->

## 4. Explanations and next investigation

### Competing explanations

| Explanation | Assessment |
| --- | --- |
| Active session intentionally records vehicle movement | Plausible; requires product requirements and policy context. |
| GPS error caused the vehicle-scale record | Not established; known driving already explains movement. Raw samples were not inspected. |
| Phone, Watch, or backend is responsible | Unknown; component attribution needs provenance and logs. |
| A warning or repair path is absent or inadequate | Open question; the full recovery workflow was not tested. |
| Tunnel results prove general GPS reliability | Unsupported; they establish only the reported outcomes under the tested conditions. |

### Priority and evidence boundary

Two affected records cannot establish prevalence or production severity. No confirmed implementation defect, component attribution, population rate, optimal threshold, or causal relationship between the two tracks is claimed. Support history, actual user impact, existing controls, and downstream behavior should inform priority. No claim is made about what Outside has already considered.

### Three focused next steps

- Explore recovery: can a user identify the affected portion, trim or relabel the workout, or otherwise correct it? Record the available controls and whether the corrected result is understandable.
- Check downstream correction: if the workout can be corrected, observe whether and how that change appears in Apple Health. Preserve before-and-after views and distinguish an observed update from assumptions about synchronization.
- Establish importance: what additional evidence would justify calling this a significant quality issue? Consider repeatability, user impact, existing recovery options, and, with product access, prevalence and support history before assigning priority.

These are proposed follow-up checks, not work completed during the weekend. Their results should determine whether any product change is worth considering. Preserve the positive Gold Camp findings as a separate baseline.

<!-- pagebreak -->

## 5. Lessons and final assessment

### How the interpretation improved

The first narrative connected the tunnel and vehicle-transition tracks too tightly. Subsequent review separated their methods and conclusions. The stronger account retains the positive findings and treats the vehicle record as a product-quality question rather than declaring the app broken. Time pressure made explicit evidence boundaries especially important.

The October revision changes organization, wording, and visual design. It does not add test runs or strengthen confidence in the underlying observations. Future evidence should extend or revise the findings rather than decorate the existing conclusion.

### AI assistance and ownership

AI assisted research, experiment planning, evidence organization, challenges to interpretation, drafting, and visual production. I executed the field work and retained responsibility for observations and final judgments. The communication difficulties and unsupported connections reinforced the need to check generated explanations against the record.

### Final assessment

The useful result is balanced: three tunnel walks produced plausible saved workouts; two separate active Run records included known vehicle travel. The evidence warrants a focused investigation of user trust and recovery, while leaving root cause, prevalence, and the right product response open.
