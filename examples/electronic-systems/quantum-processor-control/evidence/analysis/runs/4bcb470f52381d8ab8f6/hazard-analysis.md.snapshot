# Hazard Analysis

> Proposed teaching baseline. Physical performance and risk acceptance remain open. Executed abstract-model evidence and its exact scope are in [analysis/report.md](analysis/report.md). [Source review](source-review.md) identifies candidate citations and unresolved applicability; [review status](review-status.json) identifies the checked scope.

## Methodology

This hazard analysis follows IEC 61508 (Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems) Parts 1-7 with FMEA/FMECA at the component level per IEC 60812. The scope covers the Quantum Processor Control System as defined in the system boundary (README.md), analyzed across all operating modes (MODE-001 through MODE-005).

The analysis progresses through:
- **Hazard and Risk Analysis**: Identification and classification of hazardous events and hazardous situations at the system level per IEC 61508 Part 1 Section 7.4.
- **FMEA/FMECA**: Failure mode, effects, and criticality analysis at the component level for safety-relevant subsystems per IEC 60812.
- **SIL Determination**: Assignment of Safety Integrity Level based on risk reduction required per IEC 61508 Part 5.
- **Safety Function Definition**: Specification of safety instrumented functions (SIFs) and their SIL targets.

## Terminology

| Term                | Definition (this system)                                                                 | Standard Reference       |
|---------------------|------------------------------------------------------------------------------------------|--------------------------|
| Hazard              | Source of potential damage to the quantum processor chip, cryogenic hardware, or personnel through electrical overstress | IEC 61508 Part 4 Section 3.1.2 |
| Cause               | The failure event, external event, or combination thereof that produces the hazardous event | IEC 61508 Part 4 Section 3.1.3 |
| Failure Mode        | The manner in which a component or function fails (e.g., output high, output stuck, loss of output, erratic output) | IEC 60812 Section 3.2 |
| Hazardous Event     | The occurrence of the hazard in conjunction with the operational conditions that leads to harm | IEC 61508 Part 4 Section 3.1.4 |
| Harm                | Damage to quantum processor chip (Josephson junction failure), cryogenic hardware damage, or thermal excursion | IEC 61508 Part 4 Section 3.1.1 |
| Severity            | Classification of consequence: Catastrophic (chip destruction + cryostat damage), Critical (chip damage, recoverable), Marginal (experiment corruption), Negligible (no damage) | IEC 61508 Part 5 risk matrix |

## Assumptions and Preconditions

| Assumption ID | Statement                                                                                          | Validity Basis                   |
|---------------|-----------------------------------------------------------------------------------------------------|----------------------------------|
| ASM-001       | The dilution refrigerator provides independent thermal regulation and the cryostat will not reach temperatures above 4 K at the readout stage without independent alarm. | Cryostat manufacturer specifications; independent temperature monitoring system |
| ASM-002       | Cryogenic coaxial cable attenuation at each temperature stage limits maximum deliverable RF power to the chip to approximately -10 dBm even if room-temperature electronics output saturates. | Measured cable attenuation; attenuator specifications per cryostat wiring design |
| ASM-003       | The quantum processor chip can withstand RF power up to -15 dBm and flux bias current up to 8 mA without permanent damage, with safety margins of 5 dB and 2 mA respectively. | Chip manufacturer test data; Josephson junction critical current specifications |
| ASM-004       | Operators are trained in QPCS operation including emergency shutdown procedures and calibration safety protocols. | Operator training program; standard operating procedures |
| ASM-005       | The facility power system provides conditioned AC mains with UPS backup of at least 10 minutes, sufficient for a controlled shutdown sequence. | Facility infrastructure specification |

## Hazard Log

| HZ ID   | Description                                                              | Cause(s)                                                          | Effect                                                                         | MODE ID(s)            | Severity    | Likelihood    | Initial Risk | CTL ID(s)            | Residual Risk | Owner / Acceptance Authority | REQ ID(s)                                    |
|---------|--------------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------|-------------|---------------|--------------|----------------------|---------------|------------------------------|----------------------------------------------|
| HZ-001  | RF power overdrive damaging qubit Josephson junctions                    | Software commanding excessive pulse amplitude; AWG DAC fault producing full-scale output; RF amplifier oscillation | Permanent Josephson junction failure on affected qubits; partial or total chip loss | MODE-001, MODE-002    | Critical    | Occasional    | High         | CTL-001, CTL-002     | Proposed control; validation pending     | Safety officer               | REQ-FUN-007, REQ-SAF-001, REQ-SAF-002       |
| HZ-002  | Flux bias current overdrive damaging Josephson junctions                 | Software commanding excessive current; DAC fault producing full-scale output; calibration exploring outside safe range | Permanent junction damage on affected qubits; qubit frequency shift or open circuit | MODE-001, MODE-002    | Critical    | Occasional    | High         | CTL-003, CTL-004     | Proposed control; validation pending     | Safety officer               | REQ-FUN-013, REQ-SAF-003, REQ-SAF-004       |
| HZ-003  | Calibration sequence driving outputs into unsafe parameter region        | Calibration algorithm exploring beyond safe bounds; parameter database corruption providing wrong starting points | Transient or permanent qubit damage if hardware limits not triggered; wasted calibration time | MODE-002              | Critical    | Probable      | High         | CTL-005, CTL-002, CTL-003 | Proposed control; validation pending  | Safety officer               | REQ-SAF-005, REQ-FUN-018                     |
| HZ-004  | Cryogenic thermal excursion during active qubit control                  | Cryocooler compressor failure; helium leak; excessive heat load from control electronics at 4 K | Qubit coherence loss; thermal shock to chip and cryogenic components; potential helium contamination | MODE-001, MODE-004    | Catastrophic| Remote        | High         | CTL-006              | Proposed control; validation pending     | Safety officer / cryogenic engineer | REQ-FUN-021                                  |
| HZ-005  | Safety interlock system failure leaving control outputs unprotected       | Safety PLC hardware fault; analog comparator drift; interlock wiring fault | Loss of safety barrier; subsequent control fault can cause HZ-001 or HZ-002 without detection | MODE-001, MODE-002, MODE-004 | Catastrophic | Improbable | High    | CTL-008, CTL-009     | Proposed control; validation pending     | Safety officer               | REQ-SAF-006, REQ-SAF-007, REQ-SAF-008, REQ-SAF-009 |
| HZ-006  | Timing synchronization loss causing simultaneous multi-qubit damage      | TDU reference oscillator failure; clock distribution network fault; trigger sequencer FPGA fault | Multiple qubits receive out-of-sync pulses; potential frequency collision causing multi-qubit damage | MODE-001, MODE-004    | Critical    | Remote        | Medium       | CTL-007              | Proposed control; validation pending     | Safety officer               | REQ-FUN-003                                  |
| HZ-007  | Formal verifier failure passing an unsafe sequence                       | Verifier software bug; model incomplete; timeout treated as pass | Sequence with power/frequency violations executes; potential for HZ-001 or HZ-002 | MODE-001              | Critical    | Improbable    | Medium       | CTL-001, CTL-002, CTL-003 | Proposed control; validation pending  | Safety officer               | REQ-FUN-003                                  |
| HZ-008  | Cryogenic readout electronics failure causing persistent high-power readout | CRE FPGA firmware fault; ADC stuck at full-scale output driving readout resonator continuously | Excessive microwave power at mixing chamber stage from readout channel; localized heating | MODE-001, MODE-004    | Marginal    | Remote        | Low          | CTL-006, CTL-010     | Proposed control; validation pending     | Control electronics engineer | REQ-FUN-022                                  |
| HZ-009  | Unauthorized modification of safety interlock limits                     | Intentional or accidental modification of safety PLC parameters; calibration range override without proper authorization | Safety limits set too high, reducing protective margin; subsequent fault can cause damage | MODE-002, MODE-005    | Critical    | Improbable    | Medium       | CTL-009, CTL-011     | Proposed control; validation pending     | Safety officer               | REQ-SAF-010                                  |
| HZ-010  | Power supply fault causing simultaneous loss of safety and control       | Common power supply failure affecting both RTO and safety PLC; facility power loss without proper UPS switchover | Control outputs may drive to undefined state during power transient; safety system unavailable to protect | MODE-001, MODE-002    | Critical    | Remote        | Medium       | CTL-008, CTL-012     | Proposed control; validation pending     | Safety officer / facility ops | REQ-SAF-009                                  |

## Risk Controls

| CTL ID   | HZ ID(s)             | Description                                                                                     | Type                | REQ ID(s)                              | VER ID(s)                 | Residual Risk Contribution                  |
|----------|----------------------|-------------------------------------------------------------------------------------------------|---------------------|----------------------------------------|---------------------------|---------------------------------------------|
| CTL-001  | HZ-006, HZ-007       | Formal verification of gate sequences before execution, checking timing, power, and frequency constraints | Reduction          | REQ-FUN-003                            | VER-T-003, VER-FV-001     | Prevents known-unsafe sequences from reaching hardware |
| CTL-002  | HZ-001, HZ-003, HZ-007 | Hardware RF power limiter with analog comparator trip at -20 dBm at cryostat input flange    | Reduction           | REQ-FUN-007, REQ-SAF-001, REQ-SAF-002 | VER-T-001, VER-T-002      | Limits RF power regardless of software state |
| CTL-003  | HZ-002, HZ-003, HZ-007 | Hardware flux bias current limiter with analog clamp at 10 mA per channel                     | Reduction           | REQ-FUN-013, REQ-SAF-003, REQ-SAF-004 | VER-T-004, VER-T-005      | Limits current regardless of software state |
| CTL-004  | HZ-002               | Automatic detection and response to flux current trip events with operator acknowledgment required | Protective measure | REQ-SAF-004                            | VER-T-005                  | Ensures controlled response to current exceedance |
| CTL-005  | HZ-003               | Software-enforced calibration parameter validation against physical bounds with Safety Monitor approval | Reduction         | REQ-FUN-018, REQ-SAF-005              | VER-T-013, VER-T-014      | Catches calibration errors before they reach hardware limits |
| CTL-006  | HZ-004, HZ-008       | Cryostat temperature monitoring with automatic output inhibition on thermal excursion          | Protective measure  | REQ-FUN-021                            | VER-T-015                  | Prevents control during thermal event |
| CTL-007  | HZ-006               | TDU lock monitoring with automatic output inhibition on loss of timing synchronization         | Protective measure  | REQ-FUN-003, REQ-FUN-022              | VER-T-003, VER-T-017       | Prevents operation without valid timing reference |
| CTL-008  | HZ-005, HZ-010       | Safety PLC self-diagnostic with automatic safe-state transition on internal fault detection     | Reduction          | REQ-SAF-006, REQ-SAF-009              | VER-T-006, VER-T-007      | Detects safety system faults before they become dangerous |
| CTL-009  | HZ-005, HZ-009       | Analog comparator trip circuits operating independently of safety PLC with dedicated sense points | Reduction         | REQ-SAF-008                            | VER-T-008, VER-I-001      | Provides protection even if digital safety system fails |
| CTL-010  | HZ-008               | Continuous CRE health monitoring with automatic CRE power-down on anomaly detection            | Protective measure  | REQ-FUN-022                            | VER-T-017                  | Limits duration of CRE fault condition |
| CTL-011  | HZ-009               | Tamper-evident audit log with role-based access control for safety parameter changes            | Information for safety | REQ-SAF-010                         | VER-T-018, VER-I-002      | Detects unauthorized safety parameter modifications |
| CTL-012  | HZ-010               | Independent power supplies for safety PLC and control electronics with UPS backup               | Reduction          | REQ-SAF-009                            | VER-T-007                 | Prevents common power failure from disabling both control and safety |

## Fault Analysis

### FMEA: RF Pulse Generator (CMP-RPG-01) — Safety-Relevant Failure Modes

| Item | Failure Mode | Local Effect | System Effect | HZ ID | Severity | Detection Method | Detection Coverage | Recommended Action |
|------|-------------|-------------|--------------|-------|----------|-----------------|-------------------|-------------------|
| CMP-RPG-01A (AWG Card) | DAC output stuck at full scale | Maximum amplitude waveform on affected channel | RF power at chip exceeds safe limit on affected qubit(s) | HZ-001 | Critical | Hardware power limiter (CTL-002); continuous output monitoring | >99% (analog comparator) | Power limiter trips; channel inhibited |
| CMP-RPG-01A (AWG Card) | DAC output stuck at zero | No pulse output on affected channel | Gate operations fail on affected qubit(s); no safety impact | — | Negligible | BIT detects missing output; experiment error detected | >95% | Replace AWG card |
| CMP-RPG-01A (AWG Card) | DAC output erratic (noise) | Random amplitude variations | Reduced gate fidelity; potential transient power exceedances | HZ-001 | Marginal | Power limiter for exceedances; fidelity monitoring | >90% | Power limiter prevents damage; flag channel for replacement |
| CMP-RPG-01B (Upconversion) | LO oscillator failure | No RF output or wrong frequency | Gates on affected qubit fail; possible frequency collision with adjacent qubit | HZ-006 | Critical | LO lock detection; formal verifier catches frequency violations | >95% | Inhibit channel; recalibrate |
| CMP-RPG-01B (Upconversion) | Mixer imbalance degradation | Increased image/LO leakage | Reduced gate fidelity; spectral leakage to adjacent qubits | HZ-001 | Marginal | Periodic calibration measurement | >80% | Schedule replacement; adjust calibration |
| CMP-RPG-01C (Power Limiter) | Limiter fails open (no limiting) | Safety barrier lost on affected channel | Subsequent DAC fault can deliver damaging power to chip | HZ-005 | Catastrophic | Safety PLC monitoring of limiter status; analog comparator as backup | >99% | Analog comparator (CTL-009) provides backup; immediate maintenance |
| CMP-RPG-01C (Power Limiter) | Limiter fails closed (always limiting) | Channel permanently suppressed | Loss of control on affected qubit(s); no safety impact | — | Negligible | BIT detects missing output | >95% | Replace limiter module |
| CMP-RPG-01D (Sequencer FPGA) | Firmware hang | Pulse sequencing stops | Gate operations halt on all channels in FPGA; safety interlock unaffected | — | Marginal | Watchdog timer resets FPGA | >95% | Reset and re-initialize |

### FMEA: Flux Bias Controller (CMP-FBC-01) — Safety-Relevant Failure Modes

| Item | Failure Mode | Local Effect | System Effect | HZ ID | Severity | Detection Method | Detection Coverage | Recommended Action |
|------|-------------|-------------|--------------|-------|----------|-----------------|-------------------|-------------------|
| CMP-FBC-01A (Precision DAC) | DAC output stuck at full scale | Maximum current on affected channel | Flux bias current exceeds safe limit; junction damage on affected qubit | HZ-002 | Critical | Hardware current limiter (CTL-003); current monitoring | >99% (analog clamp) | Current limiter clamps; channel zeroed |
| CMP-FBC-01A (Precision DAC) | DAC output noise above specification | Excess current noise | Qubit frequency jitter; reduced coherence; no safety impact below limit | — | Marginal | Periodic noise measurement during calibration | >80% | Replace DAC module |
| CMP-FBC-01B (Current Limiter) | Limiter fails open (no clamping) | Safety barrier lost on affected channel | Subsequent DAC fault can deliver damaging current | HZ-005 | Catastrophic | Safety PLC monitoring; analog comparator as backup | >99% | Analog comparator provides backup; immediate maintenance |
| CMP-FBC-01C (Bias Sequencer FPGA) | FPGA registers corrupted | Incorrect bias values on multiple channels | Multiple qubits at wrong frequency; potential current exceedance | HZ-002 | Critical | Current limiter; ECC on FPGA configuration memory | >95% | Current limiter prevents damage; FPGA reset |

### FMEA: Safety Interlock Module (CMP-SAF-01) — Common-Cause Analysis

| Item | Failure Mode | Local Effect | System Effect | HZ ID | Severity | Detection Method | Detection Coverage | Recommended Action |
|------|-------------|-------------|--------------|-------|----------|-----------------|-------------------|-------------------|
| CMP-SAF-01A (Safety PLC) | PLC processor fault | Safety logic stops executing | Digital safety barrier lost; analog comparators still active | HZ-005 | Critical | PLC self-diagnostic; watchdog; RTO monitors PLC heartbeat | >99% | RTO transitions to safe state (REQ-SAF-009); analog comparators provide backup |
| CMP-SAF-01A (Safety PLC) | PLC communication fault | Status/trip data not received by RTO | RTO loses safety status visibility; analog trips still functional | HZ-005 | Critical | Communication timeout detection (REQ-SAF-009) | >99% | Safe state transition within 200 ms |
| CMP-SAF-01B (Analog Comparator) | Comparator threshold drift | Trip point above or below design value | Limiter may trip too early (nuisance) or too late (reduced protection margin) | HZ-005 | Critical | Periodic calibration check during MODE-005 | >90% | Schedule recalibration; margin analysis |
| CMP-SAF-01B (Analog Comparator) | Comparator stuck not-tripped | No trip signal regardless of input | Analog backup protection lost; PLC and software limits still active | HZ-005 | Critical | BIT injects known over-limit signal during MODE-005 diagnostic | >95% | Replace comparator circuit |

### Fault Tree: HZ-001 — explicit dependency model

Passive attenuation remains in every cut set. The verifier can intercept software requests but does not prevent faults arising later in the DAC/amplifier. Shared protection causes bypass claimed independence. These tests do not simulate quantum dynamics, RF propagation, cryogenic thermal behavior, or establish a SIL.

```mermaid
flowchart TD
  BE1["BE1: Software sequence requests excessive RF"]
  BE2["BE2: AWG DAC hardware produces excessive RF after precheck"]
  BE3["BE3: RF amplifier oscillation creates excessive power after precheck"]
  BE4["BE4: Sequence verifier misses an excessive software request"]
  BE5["BE5: Hardware RF power limiter fails"]
  BE6["BE6: Analog comparator fails to trip"]
  BE7["BE7: Passive attenuation cannot bound the delivered RF energy"]
  BE8["BE8: Shared sensing/power dependency defeats limiter and comparator"]
  G1A["G1A: AND"]
  G1A --> BE1
  G1A --> BE4
  G1["G1: OR"]
  G1 --> G1A
  G1 --> BE2
  G1 --> BE3
  G2["G2: OR"]
  G2 --> BE5
  G2 --> BE8
  G3["G3: OR"]
  G3 --> BE6
  G3 --> BE8
  TOP["TOP: AND"]
  TOP --> G1
  TOP --> G2
  TOP --> G3
  TOP --> BE7
```

The machine-readable [failure model](analysis/failure-model.json) is authoritative for this authored abstraction. [Executed results and interpretation](analysis/report.md) provide complete minimal cuts, scenario calculations, proof obligations and retained counterexamples. Event IDs from the earlier model retain their stated failure meaning; new shared-dependency events are explicit. Probabilities are synthetic per-demand inputs under the declared mutual-independence hypothesis after shared events are represented. No flight-hour rate, ASIL/SIL achievement, physical effectiveness or risk acceptance follows from these results.

### Proposed integrity allocation: decision still open

The former PFD ranges were not a defensible SIL determination. Preserve SIL 2 as a proposed design target for the first three functions, and SIL 1 as a proposed target for thermal shutdown, pending an adopted framework, operating mode, risk criterion, exposure and required reduction. Equipment value and ordinal "High" labels alone cannot determine an integrity level.

| Function | Hazard | Retained proposed target | Evidence needed before allocation |
| --- | --- | --- | --- |
| RF power limiting | HZ-001 | SIL 2 proposal | Damage threshold/envelope; demand definition; independent protection coverage; consequence and exposure model |
| Flux bias current limiting | HZ-002 | SIL 2 proposal | Current-duration envelope; fault initiation/detection rates; actual protection dependencies |
| Calibration parameter validation | HZ-003 | SIL 2 proposal | Validation scope, bypass paths, parameter provenance and downstream protection allocation |
| Thermal excursion shutdown | HZ-004 | SIL 1 proposal | Cryostat protection boundary, thermal response, shared sensing and shutdown obligations |

## FMECA Summary

### Detection coverage hypotheses

The percentages below are retained teaching assumptions, not measured diagnostic coverage. Their failure-mode population, weighting and physical detection evidence are absent. Recalculate coverage from an explicit injected-fault campaign and representative operating modes before assigning safety credit.

| Subsystem | Number of Safety-Relevant Failure Modes | Average Detection Coverage | Minimum Detection Coverage | Notes |
|-----------|----------------------------------------|---------------------------|---------------------------|-------|
| CMP-RPG-01 (RF Pulse Generator) | 8 | 94% | 80% (mixer imbalance) | Hardware limiter provides high coverage for power exceedances |
| CMP-FBC-01 (Flux Bias Controller) | 4 | 94% | 80% (DAC noise) | Current limiter provides high coverage for current exceedances |
| CMP-SAF-01 (Safety Interlock) | 4 | 96% | 90% (comparator drift) | Self-diagnostic and dual-layer design |
| CMP-CRE-01 (Cryogenic Readout) | 2 | 88% | 80% (marginal severity only) | Health monitoring; not safety-critical |
| CMP-TDU-01 (Timing Distribution) | 2 | 95% | 90% (lock detection) | Timing loss causes fidelity degradation, not damage |

### Overall Safety Assessment

The FMECA identifies candidate protections, but it does not establish universal detection or independence. The executed HZ-001 model shows that a sequence verifier does not prevent downstream DAC/amplifier faults and that shared protection dependencies remain. Passive attenuation is explicitly required in every derived cut. Establish the RF/current envelopes, common resources and protection response before concluding which risk contribution dominates. No residual risk has been accepted.
