The log proves too little: a transport acknowledgment does not establish that an operator saw, accepted, or performed the instruction. An unattended dashboard can receive data successfully while the operational handoff fails.

The historical basis here is the request-supplied statement from RFC 793 (1981), section 2.6. I have not independently retrieved the RFC. The following contract is a proposed application of that distinction.

| State or property | Evidence that could support it | Remaining gap |
| --- | --- | --- |
| Transport receipt | Transport reports acknowledgment of the relevant bytes | Application processing and human attention remain unknown. |
| Application receipt | Recipient application validates and records the identified instruction | Receipt does not establish display. |
| Display | Application records that the current instruction was rendered on the intended operator's display | Rendering does not establish that someone looked at it or understood it. |
| Operator acknowledgment | Identified person deliberately responds to that instruction, distinguishing “seen,” “accepted,” and “declined” | A response alone does not establish authority or action. |
| Authority | Identity and current role/delegation permit this person to accept and act on this target; operational responsibility is assigned | Authorization does not establish execution. |
| Performed action | Target-state observation shows the specified shutdown outcome, with time and configuration | A button press or command acceptance alone is insufficient. |

The minimum contract should give each instruction a unique ID, target, content/revision, authorized issuer, deadline/expiry, and explicit acceptance meaning. Correlate receipt, display, acknowledgment, acceptance/rejection, command, and observed outcome to that ID. Keep failure and unknown states visible. Check current operator authority when accepting and executing; record who held it. Retries must not create duplicate action, and expired or superseded instructions must be rejected.

Assign a staffed recipient and an accountable backup. Shift handover must explicitly transfer every outstanding instruction and its state. Set acknowledgment and action deadlines from the system's consequences; the packet gives no defensible numeric values. Unacknowledged work must escalate to an available authorized person through a route that does not depend solely on the unattended display. The system's approved contingency governs timeout behavior; automatic shutdown is not justified by this packet alone.

A proposed verification scenario is to send a uniquely identified shutdown instruction during shift change while the dashboard is unattended. Allow transport and application receipt. Verify that the system retains an unacknowledged state and escalates by the agreed deadline, without logging operator acceptance or completion. Attempt acceptance by an unauthorized person and verify refusal. Transfer responsibility to the incoming authorized operator, record deliberate acceptance, then check the target's shutdown state separately. Repeat a message and present an expired message to check duplicate and expiry handling. Include a command that fails to achieve shutdown: its outcome must remain failed or unknown, never completed on the strength of an ACK.

Retain message-correlated application, identity, handover, escalation, and target-state records with comparable timestamps. These are planned checks, not observed results; no approval or performed shutdown is established by the supplied evidence.
