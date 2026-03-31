# ChatGPT Custom GPT Install Guide

## Creating a Custom GPT per Agent

1. Go to [chat.openai.com](https://chat.openai.com) and click **Explore GPTs** > **Create**.

2. Open the agent markdown file (e.g., `agents/aerospace-systems-engineer.md`).

3. Use the frontmatter to fill in the GPT configuration:
   - **Name**: Use the `name` field (e.g., "Aerospace Systems Engineer")
   - **Description**: Use the `description` field
   - **Profile Picture**: Use the `emoji` field as inspiration or upload a custom image

4. Copy the entire markdown content (everything below the frontmatter `---` closing delimiter) and paste it into the **Instructions** field.

5. Under **Conversation Starters**, add domain-relevant prompts, e.g.:
   - "Review this requirements document against ARP4754A"
   - "Generate DO-178C certification evidence for this module"

6. Save and publish (privately or to your team).

## Batch Setup

Use `platform/chatgpt/gpt-manifest.json` as a reference for all four agents. It contains the name, description, emoji, and source file for each agent.

## Defense Founder Review

For the defense domain, create an additional GPT using `skills/defense-founder-review/SKILL.md` as Instructions. This provides a Palmer Luckey-style acquisition review persona.

## Tips

- Keep the full markdown body as Instructions; ChatGPT handles markdown natively.
- Strip the YAML frontmatter before pasting (everything between the `---` delimiters).
- For a quick strip: `sed '1{/^---$/!q;};1,/^---$/d' agents/aerospace-systems-engineer.md`
