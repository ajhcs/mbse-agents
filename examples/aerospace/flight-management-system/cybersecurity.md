# Cybersecurity Analysis

## Applicable Framework

This cybersecurity analysis follows DO-326A (Airworthiness Security Process Specification) and DO-356A (Airworthiness Security Methods and Considerations). The Security Risk Assessment identifies security-relevant assets within the FMS system boundary, characterizes threat agents, maps attack paths through the system architecture, and allocates security requirements alongside safety requirements per ARP4754A.

The analysis scope covers all operating modes (MODE-001 through MODE-005) with emphasis on interfaces crossing the system boundary that connect to off-aircraft networks (datalink, maintenance port) and inter-LRU communication paths.

## Asset Identification

| AST ID   | Asset Name                              | CMP ID(s)                    | C   | I   | A   | Safety Relevance (HZ ID)     |
|----------|-----------------------------------------|------------------------------|-----|-----|-----|------------------------------|
| AST-001  | Navigation Database                     | CMP-DCU-01C, CMP-FMC-01E/F  | Low | High| High| HZ-009 (corrupted nav data)  |
| AST-002  | Active Flight Plan Data                 | CMP-FMC-01A, CMP-FMC-01B    | Low | High| High| HZ-010 (malicious plan mod)  |
| AST-003  | FMS Application Software                | CMP-FMC-01E/F/G/H, CMP-DMC-01C, CMP-DCU-01E | Low | High | High | HZ-001 (erroneous guidance via tampered software) |
| AST-004  | Guidance Command Output                 | CMP-FMC-01G                  | Low | High| High| HZ-001, HZ-002 (erroneous guidance) |
| AST-005  | Inter-LRU AFDX Communication            | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01 | Low | High | Medium | HZ-003, HZ-010 (data integrity) |
| AST-006  | Maintenance Port Access Credentials     | CMP-DCU-01C                  | High| High| Low | HZ-009 (unauthorized data load) |
| AST-007  | FMC Configuration Data                  | CMP-FMC-01A, CMP-FMC-01B    | Low | High| Medium | HZ-005 (partition config corruption) |

**C/I/A Rating Scale**: High = compromise directly enables a safety-relevant failure condition; Medium = compromise enables a precondition for a safety-relevant failure; Low = compromise has operational but not direct safety impact.

## Threat Analysis

### DO-326A Threat Conditions

| THR ID   | Threat Condition                                                    | Attack Vector                                                     | AST ID(s)      | Security Risk | HZ ID(s)       |
|----------|---------------------------------------------------------------------|-------------------------------------------------------------------|----------------|---------------|----------------|
| THR-001  | Tampered navigation database installed via maintenance port          | Physical access to maintenance port during ground operations; malicious media or compromised loading device | AST-001, AST-006 | High          | HZ-009         |
| THR-002  | Unauthorized access to maintenance port for configuration change     | Stolen or default maintenance credentials; insider threat          | AST-006, AST-007 | High          | HZ-009, HZ-005 |
| THR-003  | Malicious ACARS message injected via ground network                  | Compromise of ACARS ground infrastructure; rogue ACARS transmitter | AST-002, AST-005 | High          | HZ-010         |
| THR-004  | Malicious FANS flight plan amendment injected via datalink           | Compromise of ATC datalink infrastructure; man-in-the-middle on FANS link | AST-002   | High          | HZ-010         |
| THR-005  | DMC compromise used to inject commands into FMC via AFDX             | Exploitation of DMC software vulnerability to craft malicious AFDX frames targeting FMC | AST-004, AST-005 | Medium | HZ-001, HZ-002 |
| THR-006  | AFDX message spoofing between LRUs                                   | Physical access to AFDX network within avionics bay; rogue device on AFDX switch | AST-005 | Medium        | HZ-003, HZ-010 |
| THR-007  | Denial of service on datalink interface causing loss of FANS capability | Flood of malformed messages on ACARS/FANS link saturating DCU processing | AST-005 | Medium        | HZ-004         |
| THR-008  | Software supply chain attack: malicious code inserted into FMS software build | Compromise of development environment, compiler, or code repository | AST-003 | High          | HZ-001         |

### Threat Agent Characterization

| Threat Agent          | Capability Level | Access Path                              | Motivation                        |
|-----------------------|------------------|------------------------------------------|-----------------------------------|
| Nation-state actor    | High             | Ground network, supply chain, insider     | Disruption, intelligence          |
| Organized criminal    | Medium           | Ground network, physical (maintenance)    | Extortion, disruption             |
| Insider (maintenance) | Medium           | Physical access to maintenance port       | Sabotage, negligence              |
| Opportunistic hacker  | Low              | Ground-facing network interfaces          | Notoriety, research               |

## Security Requirements

Security requirements are listed here for context with their threat linkage. The canonical record for all requirements is in requirements.md.

| REQ ID       | Statement                                                                                             | THR ID(s)        | CTL ID(s) | Verification |
|--------------|-------------------------------------------------------------------------------------------------------|------------------|-----------|--------------|
| REQ-SEC-001  | The FMS shall authenticate all navigation database loads using cryptographic signature verification.   | THR-001          | CTL-009   | Test         |
| REQ-SEC-002  | The DCU maintenance port shall require role-based authentication before granting access.               | THR-002          | —         | Test         |
| REQ-SEC-003  | The DCU shall validate all ACARS/FANS datalink messages against expected format and reject invalid messages. | THR-003, THR-004 | CTL-009   | Test         |
| REQ-SEC-004  | The FMS shall enforce one-way data flow from FMC to DMC for display data.                             | THR-005          | —         | Test, Analysis |
| REQ-SEC-005  | The FMS shall apply message authentication codes (MAC) to safety-critical AFDX messages between LRUs. | THR-006          | —         | Test         |

### Additional Security Controls (not in requirements.md scope)

These controls are procedural or environmental and are documented here for the security evidence package:

| Control ID (Security) | Description                                                                    | THR ID(s) |
|-----------------------|--------------------------------------------------------------------------------|-----------|
| SC-001                | Software build environment uses air-gapped build servers with integrity monitoring | THR-008  |
| SC-002                | Maintenance port physical access restricted to secured maintenance areas        | THR-001, THR-002 |
| SC-003                | Datalink message rate limiting at DCU: max 100 messages/minute                 | THR-007  |
| SC-004                | Navigation database distribution chain uses signed packages from database vendor to airline to aircraft | THR-001 |

## Security-Safety Interaction

| THR ID   | Attack Consequence                                            | HZ ID   | Combined Risk | Mitigation Strategy                                                                    |
|----------|---------------------------------------------------------------|---------|---------------|----------------------------------------------------------------------------------------|
| THR-001  | Corrupted navigation database causes erroneous waypoint sequencing | HZ-009 | High          | Cryptographic signature verification (REQ-SEC-001) + CRC integrity check (REQ-FUN-022) |
| THR-002  | Unauthorized configuration change corrupts partition table     | HZ-005  | High          | Role-based authentication (REQ-SEC-002) + partition integrity monitoring (CTL-005)      |
| THR-003  | Malicious ACARS message modifies active flight plan            | HZ-010  | High          | Message format validation (REQ-SEC-003) + crew confirmation of datalink plan amendments  |
| THR-004  | Falsified FANS amendment diverts aircraft from cleared route   | HZ-010  | High          | Message format validation (REQ-SEC-003) + flight plan feasibility check (REQ-FUN-004)   |
| THR-005  | DMC-originated command corrupts FMC navigation state           | HZ-001  | Medium        | One-way data flow enforcement (REQ-SEC-004) + AFDX MAC verification (REQ-SEC-005)       |
| THR-006  | Spoofed AFDX message injects erroneous sensor data into FMC   | HZ-003  | Medium        | AFDX MAC verification (REQ-SEC-005) + FDE algorithm (CTL-003)                           |
| THR-007  | Datalink DoS degrades FANS capability                          | HZ-004  | Medium        | Rate limiting (SC-003) + FMS operates without datalink in MODE-001                       |
| THR-008  | Malicious code in FMS build causes erroneous guidance           | HZ-001  | High          | Air-gapped build (SC-001) + dissimilar software channels (CTL-001) + code review (DO-178C Table A-5) |

### Security-Safety Boundary Analysis

The primary security-safety boundary is at the DCU, which separates the off-aircraft network interfaces (datalink, maintenance port) from the FMC safety-critical domain. The DCU acts as a gateway that:

1. **Validates** all incoming datalink messages against format specifications before forwarding to the FMC.
2. **Authenticates** all maintenance port access before allowing data load or configuration operations.
3. **Filters** message rates to prevent denial-of-service propagation to the FMC.
4. **Isolates** the maintenance port (Ethernet) from the operational AFDX network using physically separate interfaces.

The secondary security boundary is between the DMC and FMC, enforced by:
1. **One-way data flow** at the AFDX virtual link level (FMC transmits to DMC; DMC cannot write to FMC virtual links).
2. **MAC verification** on safety-critical AFDX messages providing message integrity assurance.

These boundaries map directly to the independence arguments in the CMA (hazard-analysis.md) and the partitioning rationale in the architecture (architecture.md).
