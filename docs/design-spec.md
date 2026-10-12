# Skill design and maintenance

The canonical packages are in `.agents/skills/<name>/`. Each contains required
YAML frontmatter (`name`, `description`) and task instructions in `SKILL.md`.
Optional `references/`, `assets/`, and `scripts/` belong there only when needed.
UI metadata belongs in `agents/openai.yaml`. Normal implicit discovery stays
enabled; descriptions explain when the skill applies.

Task skills develop or review artifacts. Domain skills add analysis boundaries,
domain-specific questions, and evidence expectations. The founder-review skill
supports product strategy. They can be combined for a user goal, without a
fixed number of skills, mandatory stage order, or persona roleplay.

Instructions should define a useful result, decision criteria, and real failure
conditions. Leave method selection and formatting flexible unless a process,
interchange format, or fragile operation makes them necessary. Do not turn
example thresholds into universal requirements. References disclose deeper
material only for the relevant task and remain usable after copying a package.

`catalog.json` is the authoritative inventory. `scripts/catalog.py` derives the
[skill index](skills.md), ChatGPT adaptation manifest, and UI metadata from it
and the skill frontmatter. Counts describe shipped packages, not running agents.
Legacy files in `agents/` link to the replacement domain packages.

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
validation is a separate exercise with independent assessment.
