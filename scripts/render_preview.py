"""Build a self-contained review preview. Optional dependency: Python-Markdown."""
from pathlib import Path
import argparse
import html
import json
import re
import sys

from catalog import ROOT, entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/preview.html")
    args = parser.parse_args()
    try:
        import markdown
    except ImportError:
        parser.exit(1, "Preview regeneration needs the optional Python-Markdown package. The checked-in HTML can be viewed without it.\n")
    pages = [("start", "Start here", ROOT / "README.md"),
             ("workflows", "Task workflows", ROOT / "docs/workflows.md"),
             ("models", "Model upgrades", ROOT / "docs/models.md"),
             ("installation", "Install and discover", ROOT / "platform/codex/install.md")]
    pages += [(s["name"], s["display_name"], ROOT / s["path"] / "SKILL.md") for s in entries()]
    worked = ROOT / "examples/worked/cold-storage-alarm"
    pages += [("walkthrough", "Executed walkthrough", worked / "README.md"),
              ("brief", "Stakeholder brief", worked / "brief.md"),
              ("requirements", "Linked requirements", worked / "requirements.md"),
              ("architecture", "Allocated architecture", worked / "architecture.md"),
              ("verification", "Verification and results", worked / "verification.md"),
              ("sources", "Source corrections", ROOT / "docs/sources.md"),
              ("evaluation", "Evaluation boundaries", ROOT / "docs/evaluation.md"),
              ("contribute", "Requests and contributions", ROOT / "CONTRIBUTING.md")]
    exercise = ROOT / "evals/evidence/ho01/outputs"
    if exercise.exists():
        pages += [("ho01-guide", "Fresh skill exercise", exercise / "00-review-guide.md"),
                  ("ho01-requirements", "Exercise requirements", exercise / "01-requirements.md"),
                  ("ho01-architecture", "Exercise architecture", exercise / "02-architecture.md"),
                  ("ho01-verification", "Exercise evidence plan", exercise / "03-verification-plan.md"),
                  ("ho01-checks", "Exercise document checks", exercise / "05-artifact-checks.md")]
    included = {path.resolve(): key for key, _, path in pages}
    nav = []
    sections = []
    for key, title, path in pages:
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
        # Remove the repository logo wrapper; this preview renders authored repository documents.
        text = re.sub(r"<picture>.*?</picture>", "", text, flags=re.S)
        body = markdown.markdown(text, extensions=["tables", "fenced_code"])

        def link(match):
            value = match.group(1)
            if re.match(r"[a-zA-Z]+:", value) or value.startswith("#"):
                return match.group(0)
            target = (path.parent / value.split("#")[0]).resolve()
            href = "#" + included[target] if target in included else Path(__import__("os").path.relpath(target, args.output.parent)).as_posix()
            return f'href="{html.escape(href, quote=True)}"'

        body = re.sub(r'href="([^"]+)"', link, body)
        if key == "verification":
            record = json.loads((worked / "evidence/results.json").read_text(encoding="utf-8"))
            body += '<h2>Actual saved reference-model observations</h2><table><thead><tr><th>Procedure</th><th>Result</th><th>Observed</th></tr></thead><tbody>'
            for row in record["results"]:
                body += f'<tr><td>{html.escape(row["verification"])}</td><td>{html.escape(row["result"])}</td><td><code>{html.escape(json.dumps(row["observed"]))}</code></td></tr>'
            body += '</tbody></table><p>Scope: sampled reference model. Hardware acceptance and comparative model evaluation remain open.</p>'
        if key == "architecture":
            body = re.sub(r'<pre><code class="language-mermaid">.*?</code></pre>', "", body, flags=re.S)
            body = '''<svg viewBox="0 0 900 250" role="img" aria-label="Sensor adapter sends input to evaluator; evaluator drives annunciator and event recorder">
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>
<g fill="#eff6ff" stroke="#2563eb" stroke-width="2"><rect x="20" y="85" width="200" height="70" rx="10"/><rect x="335" y="85" width="210" height="70" rx="10"/><rect x="665" y="20" width="215" height="70" rx="10"/><rect x="665" y="165" width="215" height="70" rx="10"/></g>
<g stroke="#2563eb" stroke-width="2" fill="none" marker-end="url(#arrow)"><path d="M220,120 L335,120"/><path d="M545,105 L665,55"/><path d="M545,135 L665,200"/></g>
<g fill="#172554" font-size="19" text-anchor="middle"><text x="120" y="112">COMP-01</text><text x="120" y="140">Sensor adapter</text><text x="440" y="112">COMP-02</text><text x="440" y="140">Evaluator</text><text x="772" y="47">COMP-03</text><text x="772" y="75">Annunciator</text><text x="772" y="192">COMP-04</text><text x="772" y="220">Event recorder</text></g></svg>''' + body
        nav.append(f'<a href="#{key}">{html.escape(title)}</a>')
        source = path.relative_to(ROOT).as_posix()
        sections.append(f'<section id="{key}" aria-label="{html.escape(title)}"><p class="source">Rendered from {html.escape(source)}</p>{body}</section>')
    page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>MBSE Agents — review preview</title><style>
:root{color-scheme:light}*{box-sizing:border-box}body{margin:0;background:#f5f7fa;color:#1f2937;font:16px/1.6 system-ui,sans-serif}header{padding:26px 32px;background:#172554;color:white;border-bottom:5px solid #3b82f6}header p{margin:8px 0 0;color:#dbeafe}header strong{font-size:26px}.layout{display:grid;grid-template-columns:255px minmax(0,1fr);max-width:1440px;margin:auto}nav{padding:24px 16px;position:sticky;top:0;max-height:100vh;overflow:auto}nav a{display:block;padding:6px 10px;border-radius:6px;font-size:14px;text-decoration:none;color:#1e40af}nav a:hover,nav a:focus{background:#dbeafe}main{padding:28px 36px;min-width:0}section{background:white;border:1px solid #dbe3ee;border-radius:12px;padding:30px;margin-bottom:30px;scroll-margin-top:16px}h1{font-size:29px;line-height:1.3;color:#172554}h2{font-size:22px;margin-top:30px}a{color:#1d4ed8}table{border-collapse:collapse;width:100%;display:block;overflow:auto;font-size:14px}th,td{padding:10px;border:1px solid #dbe3ee;vertical-align:top}th{background:#eff6ff;text-align:left}td:first-child{white-space:nowrap}pre{overflow:auto;background:#172554;color:#e0f2fe;padding:18px;border-radius:8px}code{font:13px/1.5 ui-monospace,Consolas,monospace;word-break:break-word}blockquote{margin:20px 0;border-left:4px solid #3b82f6;padding:1px 16px;background:#eff6ff}.source{color:#64748b;font-size:12px;border-bottom:1px solid #e2e8f0;padding-bottom:12px}svg{width:100%;height:auto}section:not(:target){display:none}section#start{display:block}body:has(section:target) section#start:not(:target){display:none}.badge{display:inline-block;background:#dbeafe;color:#172554;border-radius:20px;padding:3px 12px;font-size:13px;margin:8px 8px 0 0}@media(max-width:800px){.layout{display:block}nav{position:static;max-height:260px;border-bottom:1px solid #cbd5e1}main{padding:16px}section{padding:20px}header{padding:22px}}@media print{nav,header{display:none}.layout{display:block}section,section:not(:target){display:block!important;break-before:page}main{padding:0}}
</style></head><body><header><strong>MBSE Agents · engineering artifacts</strong><p>Skills, linked workflows, primary-source corrections, and reproducible evidence.</p><span class="badge">13 skill packages</span><span class="badge">6 executed model procedures</span><span class="badge">No comparative Sol/Astra evaluation</span></header><div class="layout"><nav aria-label="Review sections">'''
    page += "".join(nav) + '</nav><main>' + "".join(sections) + '</main></div></body></html>\n'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding="utf-8", newline="\n")
    print(args.output)


if __name__ == "__main__":
    main()
