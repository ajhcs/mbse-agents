# Source checks and limits

Checked 2026-10-12. This ledger records narrow source checks, not verification of
the entire standards catalog. All linked material is primary; summaries and
project recommendations remain distinct from normative text.

| Claim / correction | Primary source and locator | What this establishes / limits |
| --- | --- | --- |
| Task-specific discovery, progressive disclosure, proportionate instructions | [OpenAI Astra skills article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), “Better skills,” “Decision boundaries,” “Persistence” | Authoring approach, not measured MBSE performance |
| Required skill entrypoint and resource/tool boundary | [OpenAI skills concepts](https://developers.openai.com/plugins/concepts/skills), “Skills” and “How skills activate” | Instructions/resources can work without MCP; skills do not grant authorization |
| Local skill locations and invocation | [OpenAI skill authoring](https://learn.chatgpt.com/docs/build-skills), “Where Codex loads local skills” and “How ChatGPT and Codex use skills” | `.agents/skills` discovery; explicit/implicit use; host availability can differ |
| Current model identities and settings | [GPT-6 guide](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra), model choices/limitations/prompting; [Sol model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol), reasoning and snapshot fields | Sol/Astra IDs and family guidance; no local comparison or future-capability claim |
| General infusion pump class | [21 CFR 880.5725](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-880/subpart-F/section-880.5725), (a)-(b) | General healthcare-facility pumps are Class II; actual intended use/product code still matters |
| Former pump regulation was unrelated | [21 CFR 876.5820](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-876/subpart-F/section-876.5820), title and (a)-(b) | Hemodialysis systems/accessories; does not establish Class III for a general pump |
| Pump submission context | [FDA infusion-pump guidance](https://www.fda.gov/media/78369/download), section 3, printed page 5 | Class II scope and Class III-system distinction; guidance is recommendations, not clearance |
| EU pump rule | [MDCG 2021-24 Rev.1](https://health.ec.europa.eu/system/files/2021-10/mdcg_2021-24_en_0.pdf), Rule 11 notes and Rule 12 table, printed pages 47-48 | Rule 12 administration, potentially hazardous IIb examples; Rule 11 software; provisional device-specific assessment |
| Current FDA quality basis | [FDA QMSR](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr), effective-date notice; [21 CFR 820.10](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/subpart-A/section-820.10), (a)-(c) | Effective February 2, 2026; ISO 13485 incorporation and design/development applicability; old 820.30 is historical |
| Tool qualification mapping and model-based supplement scope | [FAA AC 20-115D](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf), paragraphs 6 and 10, Table 2, printed page 11 | Criterion 1: A/B/C/D -> TQL 1/2/3/4; Criterion 2: A/B -> 4, C/D -> 5; Criterion 3 -> 5. Table is a legacy correlation; new-use criteria require actual DO-178C basis. DO-331 is software model-based guidance |

eCFR is authoritative but unofficial; pages fetched showed Title 21 current to
2026-10-08. Preserve the accessed edition/date for a real regulatory decision.
FAA's public table supports the correction; we did not obtain licensed DO-178C,
DO-330, SAE, ISO, or IEC text. Unverified exact clause assertions were removed
from the new domain references and the pump evidence index. The remaining
gallery still needs section-level source review before regulated program use.

The official DoDAF site blocked page retrieval (403). The SV-5a wording is a
well-established view-definition correction, but that page was not freshly
retrieved here; verify the applicable official release before normative use.
Other crosswalks are explicitly engineering proposals, not vendor mappings.

Cole's chapter notes and lectures were not supplied. No method is attributed to
them. Future integration needs the actual material, provenance, and a focused
review; no textbook passages have been copied.
