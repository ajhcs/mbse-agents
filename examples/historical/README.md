# Historical systems engineering gallery

21 cases across 10 domains, centered on events and design baselines before 2015.

Study a system's purpose, boundaries, interfaces, alternatives, evidence,
lifecycle, and organizational decisions. The collection includes successful
delivery and recovery, early design baselines, and failures. It is a curated
teaching collection, not a representative sample for estimating failure rates.

Every case includes source-attributed facts, a new retrospective analysis,
a proposed artifact, reasoning questions, and a clearly synthetic transfer exercise.
All `HG-` IDs are teaching IDs, never original project identifiers. Source
inspection is not independent verification of the historical investigation,
and proposed tests are not executed evidence.

| ID | Case | Year | Domain | Focus |
| --- | --- | --- | --- | --- |
| HG-01 | [Apollo 13: reframe the mission after a loss](apollo-13/README.md) | 1970 | space | Separate the original mission objective, the survival objective, and the resources that make a new operating concept feasible. |
| HG-02 | [Challenger: make dissent reach the decision](challenger/README.md) | 1986 | space | Treat readiness as an evidence and communication process with identifiable decision authority. |
| HG-03 | [Hubble: verify the verifier](hubble-optics/README.md) | 1990 | space | Independence concerns the assumptions and physical references behind a test, not just the number of test results. |
| HG-04 | [Ariane 501: requalify reused assumptions](ariane-501/README.md) | 1996 | space | A reused component brings an operating envelope and inactive-looking functions that still require explicit disposition. |
| HG-05 | [Mars Climate Orbiter: own the meaning of an interface](mars-climate-orbiter/README.md) | 1999 | space | An interface contract includes semantic meaning, producers, consumers, checks, and operational handover. |
| HG-06 | [Columbia: keep anomalies visible across organizational boundaries](columbia/README.md) | 2003 | space | Successful previous operations do not resolve an unexplained hazard; information flow is part of system performance. |
| HG-07 | [Mars Exploration Rovers: connect scientific intent to operational choices](mars-exploration-rovers/README.md) | 2004 | space | Turn a broad scientific question into a sequence of feasible observations, then manage the life of that capability. |
| HG-08 | [US Airways 1549: model the decision-maker’s time](us-airways-1549/README.md) | 2009 | aviation | Validate scenarios against the time and information available to the operator, including recognition and decision delays. |
| HG-09 | [United 232: functional redundancy is not physical independence](united-232/README.md) | 1989 | aviation | Test redundant architecture against shared physical hazards and the operational capability remaining after damage. |
| HG-10 | [Heathrow Terminal 5: opening a service is an integration test](heathrow-terminal-5/README.md) | 2008 | transport | Operational readiness depends on people, logistics, software, facilities, and shared authority working together under representative conditions. |
| HG-11 | [Boston tunnel ceiling: match evidence to duration and use](boston-tunnel-ceiling/README.md) | 2006 | public infrastructure | A short acceptance test cannot close a long-duration load claim without a justified model of time-dependent behavior. |
| HG-12 | [Northeast blackout: know whether the monitoring system is working](northeast-blackout/README.md) | 2003 | energy | Operators need evidence about both the physical system and the health of the tools used to observe it. |
| HG-13 | [Texas City refinery: measure the hazard you intend to control](texas-city-refinery/README.md) | 2005 | industrial | Steady production and favorable injury statistics do not establish readiness for a hazardous startup. |
| HG-14 | [Herald of Free Enterprise: close the loop between physical state and permission](herald-free-enterprise/README.md) | 1987 | maritime | A safety-critical departure condition needs observable state, accountable confirmation, and a response to unknown or failed indication. |
| HG-15 | [TCP: define what an acknowledgment means](tcp/README.md) | 1981 | communications computing | A useful interface states both the service it provides and the stronger claims it does not establish. |
| HG-16 | [DNS: distribute authority and manage stale information](dns/README.md) | 1987 | communications computing | Scalability changes who owns data, how long others may reuse it, and what temporary disagreement means. |
| HG-17 | [World Wide Web proposal: start with the organization’s information problem](world-wide-web-proposal/README.md) | 1989 | communications computing | A concept becomes credible when it explains the users, existing assets, adoption constraints, and deliberate scope boundaries. |
| HG-18 | [Therac-25: treat interaction timing and hazard communication as design concerns](therac-25/README.md) | 1987 | medical devices | A credible safety argument must account for temporal interactions, operator feedback, and what users are told when a defect is found. |
| HG-19 | [Infusion Pump Improvement Initiative: design across the product lifecycle](infusion-pump-initiative/README.md) | 2010 | medical devices | A device is used, maintained, and understood within a care system; design review must span that lifecycle. |
| HG-20 | [London 2012: separate event readiness from legacy value](london-2012/README.md) | 2012 | public services | A program can deliver its immediate service while long-term benefits remain separate claims with different owners and evidence. |
| HG-21 | [San Bruno: preserve the provenance of configuration data](san-bruno-pipeline/README.md) | 2010 | energy | Digitizing a record does not validate the physical configuration it describes. |

## Follow a decision across domains

- **Evidence independence:** Hubble, Boston ceiling, San Bruno. What claim does each record actually support?
- **Interfaces and shared causes:** Mars Climate Orbiter, Ariane 501, United 232, TCP. Where does one team's assurance stop?
- **Operational readiness:** Heathrow Terminal 5, Herald of Free Enterprise, London 2012. What must work together at the transition?
- **Information and authority:** Challenger, Columbia, Northeast blackout, Therac-25. Which observation reaches which decision-maker?
- **Mission value and adaptation:** Apollo 13, Mars Exploration Rovers, DNS, the Web proposal. What changes when objectives or context change?
- **Lifecycle learning:** Texas City, infusion pumps, San Bruno. How does a weak field signal become an owned change?

## Connected review tasks

Some cases add editable interface and evidence registers, a hypothetical change,
and a relation view. Start from the review task and make a disposition using
the connected files. Historical records establish context; the change requests
are deliberately new teaching scenarios.

- [Hubble: verify the verifier](hubble-optics/review-task.md)
- [Mars Climate Orbiter: own the meaning of an interface](mars-climate-orbiter/review-task.md)
- [Heathrow Terminal 5: opening a service is an integration test](heathrow-terminal-5/review-task.md)

## Reproduce and extend

The canonical records are each case's `analysis.json`. The [catalog](catalog.json)
indexes them for the documentation site. [Authoring and use guidance](../../docs/historical-gallery.md)
describes the evidence boundaries; the [source register](../../docs/sources-historical.md)
records inspected URLs, publication dates, locators, and source-specific limits.

```bash
python3 examples/historical/render_gallery.py --write
python3 examples/historical/render_gallery.py --check
python3 scripts/check_historical.py --check
```

These local checks validate structure, references, and generated-file freshness.
They do not measure agent quality or validate historical engineering models.

[All examples](../README.md) · [Evaluation guidance](../../docs/evaluation.md)
