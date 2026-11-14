# CR-1 change and review record

The proposed revision B applies the approved 500-to-200 ms change to REQ-7 while retaining its ID, trigger, local-warning end event and operating conditions. REQ-8's wording, N-01, N-02 and the protected operator note remain unchanged. No implementation has been selected and revision-B compliance is unverified.

| Artifact | Disposition |
| --- | --- |
| source.md | Exact byte copy of the approved stakeholder source, including the protected note. |
| change-request.md | Exact byte copy of CR-1, retained as the change authority. |
| requirements.md | Proposed revision-B baseline; only REQ-7's required timing changes. Requirement approval and implementation evidence status are separated. |
| architecture.md | Proposed recovery correction; existing timing allocations identified as inadequate for the new bound; engineering alternatives and unresolved definitions recorded. |
| verification.md | VER-7 retained and updated for the new criterion and configuration; VER-8 retained and expanded to exercise actual stop/resume behavior and motion inhibition. |
| report-old.json | Exact byte copy preserving EVD-A-7 and its historical result and provenance. |

The current serial allocation is 150 + 80 + 30 = 260 ms, exceeding the revised criterion by 60 ms. It cannot support a 200 ms timing guarantee. Unaccounted sampling, queuing or transfer time may increase the gap. The 460 ms historical observation also differs from that allocation; obtain the old setup and timing decomposition before assuming either describes the candidate revision-B path. A demonstrated improvement must cover the same trigger and end event, with uncertainty and operating conditions addressed.

EVD-A-7 remains applicable as a supplied historical record of a revision-A assessment against 500 ms. Its recorded “pass” is not altered. The report itself says it is an authored fixture, not a run executed by this repository; detailed instruments and uncertainty are unavailable. It is not evidence of revision-B compliance merely because its requirement link remains REQ-7. Its configuration and criterion differ, and its 460 ms observation exceeds 200 ms. Applying the new number to this old observation would not establish conformance and would not constitute a revision-B execution. The old record can inform investigation and regression planning within those limits.

The recorded INHIBITED-to-OPERATING transition contradicts N-02 and REQ-8 because it allows automatic recovery after stop release and valid-data return. The proposed architecture requires a new explicit local resume with stop released and required data valid. Stop release, reconnection, sensor restoration and shift handover do not clear the inhibit. The proposed fresh-resume, stop-precedence and indication details need design review and implementation; this document does not claim that behavior exists.

Protected note, preserved verbatim in source.md: "Please keep the stop latch visible after the network comes back. We change shifts during an outage."

The next engineering decision is selection of a feasible timing implementation after path characterization, followed by an allocated and instrumentable end-to-end timing design. The recovery correction must be incorporated into that candidate configuration. VER-7 requires actual timed execution and supporting path analysis; VER-8 requires the stop, release, outage, restoration, resume and shift-change sequences described in verification.md. Accepting CR-1, editing documents, or checking document consistency is not controller verification or approval of the candidate design.

Input files remain unchanged. The run record identifies the artifact hashes and the limited document checks actually performed. No revision-B result file was fabricated; `evidence/revision-b-results.json` remains a planned location.
