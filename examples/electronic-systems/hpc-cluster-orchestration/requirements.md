# Requirements

All requirements are atomic, testable shall-statements.

## Requirement Record Schema

| Field         | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| ID            | Unique identifier (e.g., REQ-FUN-001)                                                            |
| Statement     | Atomic shall-statement                                                                            |
| Rationale     | Why this requirement exists                                                                       |
| Source        | Hazard ID (HZ-), control ID (CTL-), regulatory clause, or stakeholder need                       |
| Parent        | Parent requirement ID (if derived)                                                                |
| Verification  | Method: test, analysis, inspection, demonstration, formal verification                            |
| Allocation    | Target component ID(s) from architecture.md                                                       |
| Status        | Draft, baselined, verified, deferred                                                              |

## Functional Requirements

### REQ-FUN-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall accept job submissions via a REST API (IFC-EXT-001), supporting batch, interactive, and array job types, and shall queue up to 100,000 pending jobs with priority-based fair-share scheduling. |
| **Rationale**    | Multi-user HPC clusters require a high-capacity job queue with fair resource allocation across research groups. |
| **Source**       | Stakeholder need (computational scientist; cluster administrator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SCH-01 |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall allocate compute resources (CPU cores, GPU devices, memory, local storage) to scheduled jobs in discrete node-level or GPU-level granularity, enforcing exclusive GPU assignment (no GPU sharing between jobs) for deterministic computation. |
| **Rationale**    | GPU sharing introduces non-determinism that violates ALCOA+ reproducibility requirements for regulated workloads. |
| **Source**       | ALCOA+ (accuracy, consistency); stakeholder need (regulatory compliance officer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RES-01 |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall detect compute node failure (hardware fault, OS crash, network partition) within 10 seconds of failure occurrence via heartbeat monitoring from node agents. |
| **Rationale**    | Rapid failure detection minimizes wasted compute and enables timely job rescheduling. |
| **Source**       | Stakeholder need (cluster administrator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-AGT-01, CMP-RES-01 |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall automatically reschedule failed jobs on healthy nodes within 60 seconds of failure detection, restoring execution from the most recent checkpoint if available. |
| **Rationale**    | Automatic recovery minimizes impact of node failures on long-running simulations. |
| **Source**       | Stakeholder need (computational scientist) |
| **Parent**       | REQ-FUN-003 |
| **Verification** | Test |
| **Allocation**   | CMP-SCH-01, CMP-CHK-01 |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall perform distributed job checkpointing, capturing a consistent snapshot of all GPU memory and CPU state for multi-node jobs (up to 64 GPUs across 8 nodes) within 30 seconds, writing checkpoint data to NVMe-oF shared storage via IFC-EXT-002. |
| **Rationale**    | Checkpoint-restart is the primary fault recovery mechanism for long-running simulations that may run for days. |
| **Source**       | Stakeholder need (computational scientist) |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-CHK-01, CMP-AGT-01 |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall enforce per-rack power budgets by throttling GPU clock frequencies or deferring job starts when the aggregate power draw of a rack exceeds 80% of the rack PDU capacity (200 kW). |
| **Rationale**    | Exceeding PDU capacity trips circuit breakers, causing uncontrolled power loss and data corruption for in-flight jobs. |
| **Source**       | Stakeholder need (facility operations engineer); ASHRAE TC 9.9 |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-PWR-01 |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall record all job scheduling decisions, input dataset checksums (SHA-256), and computational result checksums in an immutable, append-only audit log that satisfies ALCOA+ principles, with each record timestamped to UTC within 1 second accuracy. |
| **Rationale**    | Regulated pharmaceutical and nuclear simulation results require a complete, tamper-evident audit trail for regulatory submission. |
| **Source**       | ALCOA+; 21 CFR Part 11; stakeholder need (regulatory compliance officer) |
| **Parent**       | — |
| **Verification** | Inspection, Test |
| **Allocation**   | CMP-AUD-01 |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall verify the integrity of computational results for SIL 1 classified workloads by comparing output checksums against independently computed reference checksums, and shall flag any mismatch as a data integrity violation in the audit log. |
| **Rationale**    | Corrupted simulation results (from silent data corruption, memory errors, or software faults) could propagate to pharmaceutical dosing decisions or reactor safety analyses. |
| **Source**       | IEC 61508 Part 3 (software safety integrity); stakeholder need (safety engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-AUD-01, CMP-AGT-01 |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall execute an orderly emergency shutdown sequence — checkpointing all running jobs, flushing write buffers, and sequencing node power-off from highest to lowest rack — within 5 minutes of receiving a facility emergency signal via IFC-EXT-004. |
| **Rationale**    | Orderly shutdown prevents data corruption and hardware damage during power or cooling emergencies. |
| **Source**       | Stakeholder need (facility operations engineer); IEC 61508 (safe state definition) |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-PWR-01, CMP-CHK-01, CMP-AGT-01 |
| **Status**       | Draft |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall monitor GPU junction temperatures via node agents and shall initiate workload throttling when any GPU exceeds 80 C, and shall terminate the workload and power-off the GPU when any GPU exceeds 90 C. |
| **Rationale**    | Sustained operation above thermal limits causes GPU degradation and can lead to silent data corruption in safety-critical computations. |
| **Source**       | IEC 61508 Part 2 (hardware safety); ASHRAE TC 9.9; stakeholder need (facility operations engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-AGT-01, CMP-PWR-01 |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall provide a user submission portal via HTTPS REST API (IFC-EXT-001) supporting OAuth 2.0 authentication, with job submission response latency of not more than 500 ms under a concurrent load of 100 users. |
| **Rationale**    | Secure, performant job submission is required for multi-tenant cluster access. |
| **Source**       | Stakeholder need (computational scientist; IT security officer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PRT-01 |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The HCOS shall interface with the NVMe-oF storage fabric (IFC-EXT-002) to provision job scratch space, mount shared datasets, and write checkpoint data, with a minimum sustained write throughput of 100 GB/s aggregate across all active checkpoint streams. |
| **Rationale**    | Checkpoint throughput determines the maximum checkpoint frequency and thus the maximum data loss on failure. |
| **Source**       | Stakeholder need (computational scientist); checkpoint budget analysis |
| **Parent**       | REQ-FUN-005 |
| **Verification** | Test |
| **Allocation**   | CMP-CHK-01, CMP-RES-01 |
| **Status**       | Draft |
