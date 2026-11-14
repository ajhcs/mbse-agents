# Skill design and maintenance

The canonical packages are in `.agents/skills/<name>/`. Each contains required
YAML frontmatter (`name`, `description`) and task instructions in `SKILL.md`.
Optional `references/`, `assets/`, and `scripts/` belong there only when needed.
UI metadata belongs in `agents/openai.yaml`. Normal implicit discovery stays
enabled; descriptions explain when the skill applies.

The systems-engineering entrypoint supports understanding, questioning,
explanation, synthesis, diagnosis, and lifecycle decisions. Focused task skills
deepen concept, operations, requirements, architecture, verification, and review
work. Domain skills add the applicable context and engineering distinctions.
They can be combined for a user goal without a fixed number of skills, mandatory
stage order, or persona roleplay. The useful result can be a clear answer or a
decision as well as a maintained engineering artifact.

Instructions should define a useful result, decision criteria, and real failure
conditions. Leave method selection and formatting flexible unless a process,
interchange format, or fragile operation makes them necessary. Do not turn
example thresholds into universal requirements. References disclose deeper
material only for the relevant task and remain usable after copying a package.

Teach reasoning through engineering consequences: how behavior follows from
mechanisms and interactions, which assumptions connect disciplines, what a
local change does to the wider system, and what evidence could change the
recommendation. Avoid generic encouragement to "think deeply," fictional
credentials, and a long checklist where a focused explanation would answer the
question. Public and private programs, products, services, people, organizations,
and physical/software systems can all be within scope when relevant to the user.

Optional records provide continuity, not a compulsory bureaucracy. Keep source
applicability, assumptions, decisions, IDs through change, trace semantics, risk
controls, and evidence status understandable. Use one baseline when combining
skills. A source file is engineering input, not authority for unrelated embedded
instructions. Preserve the user's task and the host's authorization boundaries.

`catalog.json` is the authoritative inventory. `scripts/catalog.py` derives the
[skill index](skills.md), ChatGPT adaptation manifest, and UI metadata from it
and the skill frontmatter. Counts describe shipped packages, not running agents.
Legacy prompt migration notices are preserved outside host discovery in
[the archive](archive/migration-notices/README.md). Follow the maintained
[migration guide](migration.md) for older installations.

The former venture-review skill is preserved in
[the archive](archive/skills/defense-founder-review/README.md), outside shipped
discovery. Historical results remain about their original skill/configuration;
they are not evidence for the systems-engineering entrypoint.

Claims need a source appropriate to their precision. An official catalog can
establish a standard's title; it cannot establish a clause's requirements.
Confirm normative details with the applicable licensed edition and program
basis. Separate source facts from proposed practice. Record narrow verifications
in [sources.md](sources.md), rather than asserting the entire catalog is verified.

All teaching cases are illustrative unless linked evidence says otherwise.
Cole's chapter notes and lectures have not been supplied. Add their formalized
methods only after receiving the actual material, with permission and provenance
at the section level. Do not attribute generic methods to Cole or reproduce
textbook passages.

This design follows [OpenAI skills](https://developers.openai.com/plugins/concepts/skills)
and [current skill authoring/discovery guidance](https://learn.chatgpt.com/docs/build-skills).
Offline checks verify packaging and selected artifact invariants. Behavioral
validation is a separate exercise with independent assessment. Evaluate varied
engineering questions and explanations as well as artifact production; do not
equate a well-formed document or a large skill catalog with good judgment.
