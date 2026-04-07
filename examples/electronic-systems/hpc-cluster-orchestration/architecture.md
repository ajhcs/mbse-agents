# Architecture

## System Context

```mermaid
graph TB
    subgraph HCOS["HPC Cluster Orchestration System"]
        SCH["CMP-SCH-01<br/>Central Job Scheduler"]
        RES["CMP-RES-01<br/>Resource Manager"]
        AGT["CMP-AGT-01<br/>Node Agents (x500)"]
        CHK["CMP-CHK-01<br/>Checkpoint/Restart Service"]
        PWR["CMP-PWR-01<br/>Power Management Controller"]
        AUD["CMP-AUD-01<br/>Audit & Data Integrity"]
        PRT["CMP-PRT-01<br/>User Submission Portal"]
    end

    USER["Users / Scientists<br/>(Workstations)"]
    STOR["NVMe-oF Storage Fabric<br/>(10 PB)"]
    COOL["Data Center Cooling<br/>System"]
    PDUS["Power Distribution<br/>Units"]
    EMRG["Facility Emergency<br/>System"]
    NODES["Compute Nodes<br/>(500 x 8xH100)"]

    USER -->|Job submissions (HTTPS)| PRT
    SCH -->|Job dispatch| AGT
    AGT -->|Health, telemetry| RES
    CHK -->|Checkpoint data| STOR
    RES -->|Storage mount requests| STOR
    PWR -->|Power queries/limits| PDUS
    PWR -->|Thermal telemetry| COOL
    EMRG -->|Emergency shutdown signal| PWR
    AGT -->|Job lifecycle mgmt| NODES
    AUD -->|Audit records| STOR
```

## Functional Architecture

| FUN ID       | Function Name                         | Description                                                              | Inputs                                      | Outputs                                     | Dependencies        |
|--------------|---------------------------------------|--------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------|----------------------|
| FUN-SCH-01   | Job Scheduling                        | Priority-based fair-share scheduling with preemption and backfill        | Job queue, resource availability, policies   | Job-to-node assignments, preemption commands | FUN-RES-01           |
| FUN-RES-01   | Resource Management                   | Track node inventory, GPU allocation state, and storage mounts           | Node agent heartbeats, allocation requests   | Resource maps, availability reports          | None                 |
| FUN-AGT-01   | Node Agent Lifecycle                  | Manage job start/stop, health monitoring, GPU telemetry on each node     | Scheduler commands, local sensor data        | Job status, health heartbeats, GPU temps     | None                 |
| FUN-CHK-01   | Checkpoint/Restart                    | Coordinated distributed checkpointing and restore from shared storage    | Checkpoint triggers, GPU/CPU state           | Checkpoint files, restore commands           | FUN-AGT-01, FUN-RES-01 |
| FUN-PWR-01   | Power and Thermal Management          | Enforce rack power budgets, throttle GPUs, sequence emergency shutdown   | PDU telemetry, GPU temps, facility signals   | Throttle commands, shutdown sequences        | FUN-AGT-01           |
| FUN-AUD-01   | Audit and Data Integrity              | Immutable logging of scheduling decisions, input/output checksums        | All system events, data checksums            | Audit records, integrity violation alerts    | None                 |
| FUN-PRT-01   | User Submission and Retrieval         | Accept job submissions, enforce quotas, deliver results                  | User requests via REST API                   | Job IDs, status updates, result pointers     | FUN-SCH-01           |

## Physical Architecture

### Component Hierarchy

| CMP ID        | Component Name                        | Type      | Parent   | Description                                                        |
|---------------|---------------------------------------|-----------|----------|--------------------------------------------------------------------|
| CMP-SCH-01    | Central Job Scheduler                 | Software  | System   | Fair-share priority scheduler with preemption and backfill on HA control plane |
| CMP-SCH-01A   | Priority Queue Engine                 | Software  | CMP-SCH-01 | Multi-level feedback queue with fair-share accounting per group   |
| CMP-SCH-01B   | Preemption and Backfill Logic         | Software  | CMP-SCH-01 | Checkpoint-and-preempt for high-priority regulated workloads     |
| CMP-RES-01    | Resource Manager                      | Software  | System   | Node inventory, GPU allocation state machine, storage mount broker |
| CMP-AGT-01    | Node Agent                            | Software  | System   | Per-node daemon: job lifecycle, health heartbeat, GPU telemetry collection |
| CMP-CHK-01    | Checkpoint/Restart Service            | Software  | System   | Distributed checkpoint coordinator using DMTCP or custom NCCL-aware protocol |
| CMP-PWR-01    | Power Management Controller           | Software  | System   | Rack-level power monitoring, GPU frequency throttling, emergency shutdown sequencer |
| CMP-AUD-01    | Audit and Data Integrity Service      | Software  | System   | Append-only log with cryptographic chaining (SHA-256) for tamper evidence |
| CMP-AUD-01A   | Immutable Log Store                   | Software  | CMP-AUD-01 | Write-once storage with hash-chain integrity verification        |
| CMP-AUD-01B   | Checksum Verification Engine          | Software  | CMP-AUD-01 | Independent result checksum computation and comparison            |
| CMP-PRT-01    | User Submission Portal                | Software  | System   | REST API server with OAuth 2.0, quota enforcement, and job status streaming |
| CMP-CTL-01    | HA Control Plane                      | Hardware  | System   | 3-node dedicated server cluster running scheduler, resource manager, and audit services |

## Allocation

| FUN ID       | REQ ID(s)                                    | CMP ID(s)                          | Assurance Level | Rationale                                                    |
|--------------|----------------------------------------------|-------------------------------------|-----------------|--------------------------------------------------------------|
| FUN-SCH-01   | REQ-FUN-001, REQ-FUN-004                     | CMP-SCH-01                          | Non-SIL         | Scheduling is operational; safety addressed by audit and checksum verification |
| FUN-RES-01   | REQ-FUN-002, REQ-FUN-003                     | CMP-RES-01, CMP-AGT-01              | Non-SIL         | Resource tracking supports safety indirectly through deterministic allocation |
| FUN-AGT-01   | REQ-FUN-003, REQ-SAF-004                     | CMP-AGT-01                           | SIL 1           | Node agents execute thermal monitoring which is safety-relevant |
| FUN-CHK-01   | REQ-FUN-005, REQ-SAF-003                     | CMP-CHK-01                           | SIL 1           | Checkpoint integrity affects ability to recover regulated workloads correctly |
| FUN-PWR-01   | REQ-FUN-006, REQ-SAF-003, REQ-SAF-004        | CMP-PWR-01                           | SIL 1           | Power management enforces thermal safety and emergency shutdown |
| FUN-AUD-01   | REQ-SAF-001, REQ-SAF-002                     | CMP-AUD-01                           | SIL 1           | Audit and checksum verification is the primary safety barrier for regulated data integrity |
| FUN-PRT-01   | REQ-IFC-001                                  | CMP-PRT-01                           | Non-SIL         | User portal is not safety-critical; authentication is a security concern |

## Interfaces

### External Interfaces

| IFC ID       | Partner System                  | Data Item                                    | Direction     | Protocol               | Timing                    |
|--------------|---------------------------------|----------------------------------------------|---------------|------------------------|---------------------------|
| IFC-EXT-001  | User Workstations               | Job submissions, status queries, results     | Bidirectional | HTTPS REST (OAuth 2.0) | < 500 ms response         |
| IFC-EXT-002  | NVMe-oF Storage Fabric          | Checkpoint data, scratch mounts, audit logs  | Bidirectional | NVMe-oF / RDMA         | 100 GB/s aggregate write   |
| IFC-EXT-003  | Data Center Cooling System      | Inlet/outlet temps, cooling capacity status  | In            | SNMP / Modbus TCP      | 10 s polling              |
| IFC-EXT-004  | Facility Emergency System       | Emergency shutdown signal                    | In            | Hardwired discrete / BACnet | < 1 s latency          |
| IFC-EXT-005  | Power Distribution Units        | Rack power draw, circuit status              | In            | SNMP / Modbus TCP      | 5 s polling               |
| IFC-EXT-006  | Compute Nodes (x500)            | Job commands, health heartbeats, telemetry   | Bidirectional | gRPC over 100GbE       | 1 s heartbeat; async cmd  |

### Internal Interfaces

| IFC ID       | Source CMP ID  | Target CMP ID  | Data Item                                | Mechanism              | Timing               |
|--------------|----------------|-----------------|------------------------------------------|------------------------|----------------------|
| IFC-INT-001  | CMP-SCH-01     | CMP-RES-01      | Resource allocation requests/grants      | Internal gRPC          | Per scheduling cycle |
| IFC-INT-002  | CMP-SCH-01     | CMP-AGT-01      | Job dispatch and preemption commands     | gRPC (via IFC-EXT-006) | Per job event        |
| IFC-INT-003  | CMP-AGT-01     | CMP-CHK-01      | Checkpoint trigger and status            | Internal gRPC          | Per checkpoint cycle |
| IFC-INT-004  | CMP-AGT-01     | CMP-AUD-01      | Job events, GPU telemetry, checksums     | Event stream (Kafka)   | Per event            |
| IFC-INT-005  | CMP-PWR-01     | CMP-AGT-01      | Throttle commands, shutdown sequences    | gRPC                   | Per power event      |
| IFC-INT-006  | CMP-PRT-01     | CMP-SCH-01      | Validated job submissions                | Internal gRPC          | Per submission       |

## Failure Containment / Partitioning

### Control Plane / Data Plane Separation

The HCOS control plane (CMP-SCH-01, CMP-RES-01, CMP-AUD-01, CMP-PRT-01) runs on a dedicated 3-node HA cluster (CMP-CTL-01) that is physically separate from the 500 compute nodes. A control plane failure does not terminate running jobs — node agents (CMP-AGT-01) continue executing active jobs autonomously for up to 30 minutes using locally cached job state. When the control plane recovers, node agents resynchronize, and any jobs that completed or failed during the outage are reconciled. This separation ensures that a scheduler crash does not corrupt in-flight computational results.

### Audit Service Independence

The Audit and Data Integrity Service (CMP-AUD-01) runs as an independent process with its own dedicated storage partition on the HA cluster. Audit log writes use a separate storage volume from the scheduler database, ensuring that a scheduler database corruption event does not affect the integrity of the audit trail. The immutable log store (CMP-AUD-01A) uses cryptographic hash chaining (each record includes the SHA-256 hash of the previous record), making it detectable if any record is modified, deleted, or inserted out of sequence.

### Node-Level Fault Isolation

Each compute node runs an independent node agent (CMP-AGT-01) that monitors local hardware health. A hardware failure on one node (GPU error, memory ECC uncorrectable, NVMe failure) is contained to that node. The resource manager (CMP-RES-01) removes the failed node from the allocation pool, and the checkpoint service (CMP-CHK-01) coordinates with the remaining nodes to preserve consistent state for multi-node jobs that included the failed node. No single node failure can corrupt the job state on other nodes in the same multi-node job, because NCCL collective operations use timeout-based failure detection and the checkpoint protocol requires all participating nodes to reach a barrier before the checkpoint is committed.

## Architecture Decisions

### AD-01: Dedicated HA Control Plane over Co-Located Scheduler

**Decision:** Run the HCOS control plane (scheduler, resource manager, audit service) on a dedicated 3-node HA cluster rather than co-locating scheduler processes on compute nodes.

**Rationale:** Co-locating the scheduler on compute nodes creates a failure coupling between workload execution and cluster management. A GPU driver crash or kernel panic on a compute node would also take down the scheduler instance on that node. The dedicated HA cluster provides independent fault domains, and the 3-node Raft consensus ensures scheduler state survives any single control-plane node failure.

**Trade-off:** Additional hardware cost (3 dedicated servers) and operational complexity (separate maintenance for the control plane). Accepted because the ALCOA+ audit trail integrity and SIL 1 safety argument require demonstrable independence between the control function and the controlled process.

### AD-02: Cryptographic Hash-Chain Audit Log over Relational Database Logging

**Decision:** Implement the audit trail as an append-only log with SHA-256 hash chaining rather than storing audit records in a relational database.

**Rationale:** Relational databases allow UPDATE and DELETE operations that could (through bug, misconfiguration, or malicious action) modify historical audit records. ALCOA+ requires that records be original and enduring — modifications must be detectable. A hash-chain log makes any tampering computationally evident: modifying any record breaks the hash chain from that point forward. The log is verified by recomputing the hash chain from the first record to the last.

**Trade-off:** Append-only storage is less efficient for queries (no indexing, sequential scan for search). Mitigated by maintaining a read-only query index that is rebuilt periodically from the authoritative hash-chain log. The index is not authoritative — the hash-chain log is the single source of truth.

### AD-03: Exclusive GPU Assignment over GPU Sharing

**Decision:** Enforce exclusive GPU assignment (one job per GPU, no MPS/MIG sharing) for all SIL 1 classified workloads.

**Rationale:** GPU sharing (via NVIDIA MPS or MIG) introduces non-deterministic resource contention that can produce different numerical results across repeated runs of the same workload. For pharmaceutical simulation and reactor physics calculations, reproducibility of results is a regulatory requirement under ALCOA+ (accuracy, consistency). Exclusive GPU assignment eliminates this contention, ensuring bitwise reproducible results when combined with deterministic NCCL communication patterns.

**Trade-off:** Lower GPU utilization when SIL 1 workloads do not fully utilize the GPU. Mitigated by allowing non-SIL workloads to use GPU sharing during periods when the cluster is not running regulated jobs, with the scheduler enforcing exclusive mode only for workloads tagged as SIL 1.
