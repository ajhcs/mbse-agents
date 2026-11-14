"""Portable documentation build. Optional dependency: requirements-docs.txt."""
from __future__ import annotations

import argparse
import base64
from dataclasses import dataclass
import hashlib
import html
from html.parser import HTMLParser
import json
import mimetypes
from pathlib import Path
import re
import textwrap
from urllib.parse import unquote, urlsplit

from catalog import ROOT

EXCLUDED = ("docs/archive/", "docs/superpowers/", "evals/archive/", "evals/runs/")
EXCLUDED_FILES = {"evals/rubrics.json", "evals/benchmark/keys.json",
                  "docs/evidence/documentation-qualification.json",
                  "docs/evidence/repository-qualification.json"}
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".csv", ".sysml", ".toml", ".mmd"}
NAVIGATION = (
    ("Get started", (("README.md", "Overview"), ("platform/plugin/install.md", "Plugin installation"),
                     ("platform/codex/install.md", "Selected skills"),
                     ("docs/getting-started.md", "First result"))),
    ("Engineering work", (("docs/workflows.md", "Task workflows"), ("docs/skills.md", "Skill catalog"),
                          ("examples/historical/README.md", "Historical gallery"),
                          ("examples/README.md", "Teaching examples"))),
    ("Assessment", (("docs/benchmark.md", "Engineering judgment benchmark"),
                    ("docs/evaluation.md", "Evaluation and evidence"), ("docs/sources.md", "Source basis"))),
    ("Using the library", (("docs/models.md", "Model selection"), ("docs/SUBMISSIONS.md", "Distribution"),
                           ("CONTRIBUTING.md", "Support and contributions"))),
    ("Review records", (("docs/release-report.md", "Release qualification"),
                        ("evals/evidence/README.md", "Observed task evidence"),
                        ("docs/review/README.md", "Review history"))),
)


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def excluded(relative: str) -> bool:
    if relative in EXCLUDED_FILES or any(relative.startswith(prefix) for prefix in EXCLUDED):
        return True
    if relative.startswith("evals/evidence/"):
        parts = Path(relative).parts
        if any(part in {".agents", "skills", "preparation-v1"} for part in parts[2:-1]):
            return True
        # Preserved inputs are provenance, not another current skill catalog or
        # a public answer-key surface. Actual responses and assessments remain.
        name = re.sub(r"\.(?:json|ya?ml|md|txt)(?:\.txt)?$", "", parts[-1].lower())
        if name in {"keys", "answer-key", "answer-keys", "reviewer-key", "reviewer-keys",
                    "rubric", "rubrics", "keys-snapshot", "review-guide-snapshot"}:
            return True
        if name.startswith(("rubric-snapshot", "rubrics-snapshot", "reviewer-key-snapshot",
                            "reviewer-keys-snapshot", "answer-key-snapshot", "answer-keys-snapshot")):
            return True
    return False


def document_id(relative: str) -> str:
    readable = re.sub(r"[^a-z0-9]+", "-", relative.lower()).strip("-")
    return readable + "-" + digest(relative.encode())[:8]


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    return re.sub(r"<picture>.*?</picture>", "", text, flags=re.S)


def source_text(path: Path) -> str:
    return clean_text(path.read_text(encoding="utf-8"))


class References(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.links.append(value)
            if key == "id" and value:
                self.ids.add(value)


def local_target(root: Path, source: Path, value: str) -> tuple[Path, str] | None:
    parsed = urlsplit(html.unescape(value))
    if parsed.scheme or parsed.netloc:
        return None
    raw = unquote(parsed.path)
    candidate = source.parent / raw if raw else source
    target = candidate.resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"{source.relative_to(root)}: link leaves repository: {value}")
    generated_aliases = {"docs/site/index.html": "README.md", "docs/preview.html": "docs/review/README.md"}
    relative = target.relative_to(root.resolve()).as_posix()
    if relative in generated_aliases:
        target = root / generated_aliases[relative]
    if target.is_dir():
        target = target / "README.md"
    if not target.is_file():
        raise ValueError(f"{source.relative_to(root)}: missing linked file: {value}")
    if candidate.is_symlink():
        raise ValueError(f"{source.relative_to(root)}: symlink is not a documentation source: {value}")
    return target, unquote(parsed.fragment)


@dataclass
class Document:
    relative: str
    path: Path
    title: str
    body: str
    anchors: set[str]

    @property
    def id(self):
        return document_id(self.relative)


def collect_documents(root: Path, markdown_module) -> tuple[dict[str, Document], dict[str, bytes]]:
    """Collect public reading sources and local links, excluding reviewer keys."""
    root = root.resolve()
    sources: dict[str, bytes] = {"catalog.json": (root / "catalog.json").read_bytes()}
    seeds = [root / name for name in ("README.md", "CONTRIBUTING.md", "CHANGELOG.md")]
    for folder in ("docs", "examples", "platform", "evals/evidence"):
        seeds.extend((root / folder).rglob("*.md"))
    seeds.extend((root / "evals/benchmark").glob("*.md"))
    for item in json.loads(sources["catalog.json"])["skills"]:
        seeds.extend((root / item["path"]).rglob("*.md"))
    queue = sorted({p.resolve() for p in seeds if p.is_file()})
    documents: dict[str, Document] = {}
    while queue:
        path = queue.pop(0)
        relative = path.relative_to(root).as_posix()
        if (excluded(relative) or relative.startswith("docs/site/") or
                path.name in {"AGENTS.md", "CLAUDE.md"} or relative in documents):
            continue
        raw = sources.setdefault(relative, path.read_bytes())
        if path.suffix == ".md":
            text = clean_text(raw.decode("utf-8"))
            match = re.search(r"^#\s+(.+)$", text, re.M)
            title = match.group(1).strip() if match else path.stem
            body = markdown_module.markdown(text, extensions=["tables", "fenced_code", "toc"])
        else:
            title = path.name
            escaped = html.escape(raw.decode("utf-8"))
            # Keep preserved source whitespace in the decoded reading view
            # without introducing trailing whitespace in generated HTML.
            escaped = re.sub(r"[ \t]+(?=\r?$)",
                             lambda match: "".join("&#32;" if char == " " else "&#9;" for char in match[0]),
                             escaped, flags=re.M)
            body = f"<h1>{html.escape(title)}</h1><pre><code>{escaped}</code></pre>"
        parsed = References()
        parsed.feed(body)
        documents[relative] = Document(relative, path, title, body, parsed.ids)
        for value in parsed.links:
            resolved = local_target(root, path, value)
            if resolved is None:
                continue
            target, _ = resolved
            target_relative = target.relative_to(root).as_posix()
            if excluded(target_relative):
                continue
            sources.setdefault(target_relative, target.read_bytes())
            if target.suffix in TEXT_SUFFIXES or target.name == "LICENSE":
                queue.append(target)
            elif target.suffix.lower() not in {".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}:
                raise ValueError(f"Unsupported documentation asset: {target_relative}")
    return documents, sources


class Rewrite(HTMLParser):
    """Retain fragments and namespace IDs when bundling independent documents."""
    def __init__(self, root: Path, document: Document, documents: dict[str, Document]):
        super().__init__(convert_charrefs=False)
        self.root, self.document, self.documents = root, document, documents
        self.output: list[str] = []

    def start(self, tag, attrs, closing=""):
        rewritten = []
        for key, value in attrs:
            if value is not None and key == "id":
                value = self.document.id + "--" + value
            elif value is not None and key in {"aria-labelledby", "aria-describedby"}:
                value = " ".join(self.document.id + "--" + token for token in value.split())
            elif value is not None and "url(#" in value:
                value = re.sub(r"url\(#([^)]+)\)", lambda match: "url(#" + self.document.id + "--" + match.group(1) + ")", value)
            elif value is not None and key in {"href", "src"}:
                resolved = local_target(self.root, self.document.path, value)
                if resolved:
                    target, fragment = resolved
                    relative = target.relative_to(self.root).as_posix()
                    if excluded(relative):
                        value = "https://github.com/ajhcs/mbse-agents/blob/main/" + relative
                        if fragment:
                            value += "#" + fragment
                    elif relative in self.documents and key == "href":
                        other = self.documents[relative]
                        if fragment and fragment not in other.anchors:
                            raise ValueError(f"{self.document.relative}: unresolved heading: {relative}#{fragment}")
                        value = "#" + other.id + ("--" + fragment if fragment else "")
                    else:
                        mime = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
                        value = f"data:{mime};base64," + base64.b64encode(target.read_bytes()).decode("ascii")
            rewritten.append(key if value is None else f'{key}="{html.escape(value, quote=True)}"')
        self.output.append("<" + tag + (" " if rewritten else "") + " ".join(rewritten) + closing + ">")

    def handle_starttag(self, tag, attrs):
        self.start(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        self.start(tag, attrs, "/")

    def handle_endtag(self, tag):
        self.output.append(f"</{tag}>")

    def handle_data(self, data):
        self.output.append(data)

    def handle_entityref(self, name):
        self.output.append(f"&{name};")

    def handle_charref(self, name):
        self.output.append(f"&#{name};")

    def handle_comment(self, data):
        self.output.append(f"<!--{data}-->")


def architecture_graph(text: str) -> dict:
    """Read a bounded LR graph; refuse unsupported statements or missing nodes.

    This is a source-derived logical graph, not a SysML parser or simulation.
    """
    blocks = re.findall(r"```mermaid\s*\n(.*?)```", text, re.S)
    if len(blocks) != 1:
        raise ValueError("Each diagram source must contain exactly one Mermaid graph")
    lines = [line.strip() for line in blocks[0].splitlines() if line.strip()]
    if not lines or lines[0] != "flowchart LR":
        raise ValueError("Source-derived diagram renderer supports flowchart LR only")
    node = r"([A-Za-z][A-Za-z0-9_]*)(?:\[([^\]]+)\])?"
    pattern = re.compile(node + r"\s*-->\|([^|]+)\|\s*" + node + r"$")
    nodes: dict[str, str] = {}
    edges = []
    def remember(key, label):
        if label is not None:
            label = json.loads(label) if label.startswith('"') else label
            if key in nodes and nodes[key] != label:
                raise ValueError(f"Conflicting graph label: {key}")
            nodes[key] = label

    for line in lines[1:]:
        declaration = re.fullmatch(node, line)
        if declaration and declaration.group(2):
            remember(*declaration.groups())
            continue
        match = pattern.fullmatch(line)
        if not match:
            raise ValueError(f"Unsupported source graph statement: {line}")
        start, start_label, label, end, end_label = match.groups()
        for key, name in ((start, start_label), (end, end_label)):
            remember(key, name)
        edges.append({"from": start, "to": end, "label": label})
    if not nodes or not edges:
        raise ValueError("Source graph needs named participants and labeled relations")
    if any(edge[key] not in nodes for edge in edges for key in ("from", "to")):
        raise ValueError("Worked architecture has an undefined graph endpoint")
    return {"kind": "source-derived-logical-flow", "nodes": nodes, "edges": edges}


def architecture_svg(graph: dict, title="Cold-storage alarm logical architecture", prefix="architecture") -> str:
    """Derive a deterministic layered SVG with every participant and edge label."""
    nodes, edges = graph["nodes"], graph["edges"]
    ranks = {key: 0 for key in nodes}
    for _ in range(len(nodes)):
        changed = False
        for edge in edges:
            proposed = ranks[edge["from"]] + 1
            if ranks[edge["to"]] < proposed:
                ranks[edge["to"]], changed = proposed, True
        if not changed:
            break
    else:
        raise ValueError("Worked architecture graph contains a cycle")
    levels = {rank: [key for key in nodes if ranks[key] == rank] for rank in sorted(set(ranks.values()))}
    lines = {}
    for key, label in nodes.items():
        identifier, _, name = label.partition(" ")
        if re.fullmatch(r"[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+", identifier):
            lines[key] = [identifier] + textwrap.wrap(name, width=22, break_long_words=False, break_on_hyphens=False)
        else:
            lines[key] = textwrap.wrap(label, width=22, break_long_words=False, break_on_hyphens=False)
    node_width = max(220, 32 + 9 * max(len(line) for values in lines.values() for line in values))
    node_height = max(72, 24 * max(map(len, lines.values())) + 24)
    step = node_width + 200
    has_long_edge = any(ranks[e["to"]] - ranks[e["from"]] > 1 for e in edges)
    width = (len(levels) - 1) * step + node_width + 60
    height = max(len(keys) for keys in levels.values()) * 170 + (130 if has_long_edge else 70)
    positions = {}
    for rank, keys in levels.items():
        for index, key in enumerate(keys):
            positions[key] = (30 + rank * step, (height - len(keys) * 170) / 2 + index * 170 + 40)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{prefix}-title {prefix}-description">',
             f'<title id="{prefix}-title">{html.escape(title)}</title>',
             f'<desc id="{prefix}-description">All participants and directed labeled relations from the authored source graph. This is a logical presentation, not formal SysML or executed behavior.</desc>',
             f'<defs><marker id="{prefix}-arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>']
    direct = [edge for edge in edges if ranks[edge["to"]] - ranks[edge["from"]] == 1]
    outgoing = {key: sorted((edge for edge in edges if edge["from"] == key),
                            key=lambda edge: positions[edge["to"]][1]) for key in nodes}
    incoming = {key: sorted((edge for edge in edges if edge["to"] == key),
                            key=lambda edge: positions[edge["from"]][1]) for key in nodes}
    for edge in edges:
        x1, y1 = positions[edge["from"]]
        x2, y2 = positions[edge["to"]]
        source_edges, target_edges = outgoing[edge["from"]], incoming[edge["to"]]
        source_port = node_height * (source_edges.index(edge) + 1) / (len(source_edges) + 1)
        target_port = node_height * (target_edges.index(edge) + 1) / (len(target_edges) + 1)
        start, end = (x1 + node_width, y1 + source_port), (x2, y2 + target_port)
        if edge in direct:
            middle = (start[0] + end[0]) / 2
            route = f"M{start[0]},{start[1]} L{middle},{start[1]} L{middle},{end[1]} L{end[0]},{end[1]}"
            outer_y = max((start[1], end[1]), key=lambda value: abs(value - height / 2))
            label_y = outer_y - 27 if outer_y <= height / 2 else outer_y + 31
        else:
            # Leave through free side corridors before taking an outer rail.
            # Vertical travel through the source column can cross a peer node.
            above = y1 + node_height / 2 <= height / 2
            rail = 45 if above else height - 45
            exit_x, entry_x = start[0] + 12, end[0] - 12
            middle = (start[0] + end[0]) / 2
            route = f"M{start[0]},{start[1]} L{exit_x},{start[1]} L{exit_x},{rail} L{entry_x},{rail} L{entry_x},{end[1]} L{end[0]},{end[1]}"
            label_y = rail - 27 if above else rail + 18
        identifier, _, description = edge["label"].partition(" ")
        parts.append(f'<g data-from="{html.escape(edge["from"])}" data-to="{html.escape(edge["to"])}" data-interface="{html.escape(identifier)}"><path d="{route}" fill="none" stroke="white" stroke-width="7"/><path d="{route}" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#{prefix}-arrow)"/>')
        parts.append(f'<text x="{middle}" y="{label_y}" text-anchor="middle" fill="#172554" font-family="system-ui,sans-serif" font-size="14"><tspan x="{middle}">{html.escape(identifier)}</tspan><tspan x="{middle}" dy="18">{html.escape(description)}</tspan></text></g>')
    for key, label in nodes.items():
        x, y = positions[key]
        center = x + node_width / 2
        baseline = y + node_height / 2 - (len(lines[key]) - 1) * 12 + 6
        parts.append(f'<g data-node="{html.escape(key)}" aria-label="{html.escape(label)}"><rect x="{x}" y="{y}" width="{node_width}" height="{node_height}" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/><text x="{center}" y="{baseline}" text-anchor="middle" fill="#172554" font-family="system-ui,sans-serif" font-size="17">')
        for index, line in enumerate(lines[key]):
            parts.append(f'<tspan x="{center}" dy="{24 if index else 0}">{html.escape(line)}</tspan>')
        parts.append("</text></g>")
    return "".join(parts) + "</svg>\n"


STYLE = """
:root{color-scheme:light}*{box-sizing:border-box}body{margin:0;background:#f5f7fa;color:#1f2937;font:16px/1.6 system-ui,sans-serif}header{padding:24px 32px;background:#172554;color:white;border-bottom:5px solid #3b82f6}header strong{font-size:26px}header p{margin:8px 0 0;color:#dbeafe}.layout{display:grid;grid-template-columns:255px minmax(0,1fr);max-width:1440px;margin:auto}nav{padding:24px 16px;position:sticky;top:0;max-height:100vh;overflow:auto}nav h2{font-size:13px;text-transform:uppercase;letter-spacing:.04em;margin:20px 10px 5px;color:#475569}nav a{display:block;padding:6px 10px;border-radius:6px;font-size:14px;text-decoration:none;color:#1e40af}nav a:hover,nav a:focus,nav a[aria-current]{background:#dbeafe}main{padding:28px 36px;min-width:0}article{background:white;border:1px solid #dbe3ee;border-radius:12px;padding:30px;margin-bottom:30px}article[hidden]{display:none}h1{font-size:29px;line-height:1.3;color:#172554}h2{font-size:22px;margin-top:30px}a{color:#1d4ed8}table{border-collapse:collapse;width:100%;display:block;overflow:auto;font-size:14px}th,td{padding:10px;border:1px solid #dbe3ee;vertical-align:top}th{background:#eff6ff;text-align:left}td:first-child{white-space:nowrap}pre{overflow:auto;background:#172554;color:#e0f2fe;padding:18px;border-radius:8px}code{font:13px/1.5 ui-monospace,Consolas,monospace;word-break:break-word}blockquote{margin:20px 0;border-left:4px solid #3b82f6;padding:1px 16px;background:#eff6ff}.source{color:#64748b;font-size:12px;border-bottom:1px solid #e2e8f0;padding-bottom:12px}.diagram{overflow:auto}.diagram svg{display:block;max-width:none;height:auto}.badge{display:inline-block;background:#dbeafe;color:#172554;border-radius:20px;padding:3px 12px;font-size:13px;margin:8px 8px 0 0}.toolbar{display:flex;gap:12px;margin:0 0 16px}.toolbar button{background:white;border:1px solid #94a3b8;border-radius:5px;padding:7px 12px;color:#172554;cursor:pointer}.build-note{font-size:12px;color:#475569;word-break:break-all}img{max-width:100%}@media(max-width:800px){.layout{display:block}nav{position:static;max-height:260px;border-bottom:1px solid #cbd5e1}main{padding:16px}article{padding:20px}header{padding:22px}}@media print{nav,header,.toolbar,.build-note{display:none}.layout{display:block}main{padding:0}article{border:0;padding:0;break-before:page}article:first-child{break-before:auto}body.print-all article[hidden]{display:block!important}.diagram{overflow:visible}.diagram svg{width:100%;max-width:100%;height:auto}pre,table{overflow:visible;white-space:pre-wrap}}
"""

SCRIPT = """
const documents = [...document.querySelectorAll('article[data-document]')];
function selectDocument() {
  let target;
  try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch (_) {}
  const active = (target && target.closest('article[data-document]')) || document.getElementById(document.body.dataset.start);
  documents.forEach(item => { item.hidden = item !== active; });
  document.querySelectorAll('nav a').forEach(link => {
    if (link.hash === '#' + active.id) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  });
  document.title = active.dataset.title + ' · MBSE Agents';
  if (target) requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
}
addEventListener('hashchange', selectDocument);
selectDocument();
document.getElementById('print-selected').onclick = () => { document.body.classList.remove('print-all'); print(); };
document.getElementById('print-all').onclick = () => { document.body.classList.add('print-all'); print(); };
addEventListener('afterprint', () => document.body.classList.remove('print-all'));
"""


def build_outputs(root: Path = ROOT) -> dict[str, bytes]:
    try:
        import markdown
    except ImportError as error:
        raise RuntimeError("Documentation build needs the optional dependencies in requirements-docs.txt") from error
    root = root.resolve()
    documents, sources = collect_documents(root, markdown)
    outputs: dict[str, bytes] = {}
    architecture = "examples/worked/cold-storage-alarm/architecture.md"
    for relative, document in documents.items():
        if relative != architecture and not relative.startswith("examples/historical/"):
            continue
        figure_number = 0
        def render_graph(match):
            nonlocal figure_number
            figure_number += 1
            source = "```mermaid\n" + html.unescape(match.group(1)) + "\n```"
            graph = architecture_graph(source)
            name = "cold-storage-architecture" if relative == architecture else document.id + f"-figure-{figure_number}"
            svg = architecture_svg(graph, document.title, f"figure-{figure_number}")
            graph.update(source=relative, source_locator=f"Mermaid block {figure_number}", source_sha256=digest(sources[relative]))
            graph_bytes = (json.dumps(graph, indent=2) + "\n").encode()
            outputs[f"docs/site/assets/{name}.svg"] = svg.encode()
            outputs[f"docs/site/assets/{name}.json"] = graph_bytes
            downloads = ('<p class="source">Source-derived logical flow · '
                         f'<a download="{name}.svg" href="data:image/svg+xml;base64,' +
                         base64.b64encode(svg.encode()).decode() + '">Editable SVG</a> · '
                         f'<a download="{name}.json" href="data:application/json;base64,' +
                         base64.b64encode(graph_bytes).decode() + '">Source graph</a></p>')
            return '<div class="diagram">' + svg + '</div>' + downloads
        document.body = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>', render_graph, document.body, flags=re.S)
    for relative in ("catalog.json", "requirements-docs.txt", "config/model-profiles.json",
                     "examples/historical/catalog.json", "evals/benchmark/items.json"):
        if (root / relative).is_file():
            sources.setdefault(relative, (root / relative).read_bytes())
    for filename in ("documentation.py", "render_preview.py"):
        sources["scripts/" + filename] = Path(__file__).with_name(filename).read_bytes()
    source_hashes = {key: digest(value) for key, value in sorted(sources.items())}
    snapshot = digest(json.dumps(source_hashes, sort_keys=True, separators=(",", ":")).encode())
    counts = {"skills": len(json.loads(sources["catalog.json"])["skills"]), "documents": len(documents)}
    for relative, field, key in (("examples/historical/catalog.json", "cases", "historical_cases"),
                                 ("evals/benchmark/items.json", "items", "benchmark_items")):
        if (root / relative).is_file():
            record = json.loads(sources[relative])
            counts[key] = len(record if isinstance(record, list) else record.get(field, []))
    nav = []
    for group, links in NAVIGATION:
        available = [(documents[path], title) for path, title in links if path in documents]
        if available:
            nav.append(f"<h2>{html.escape(group)}</h2>")
            nav.extend(f'<a href="#{doc.id}">{html.escape(title)}</a>' for doc, title in available)
    articles = []
    for relative, doc in sorted(documents.items()):
        rewriter = Rewrite(root, doc, documents)
        rewriter.feed(doc.body)
        articles.append(f'<article id="{doc.id}" data-document="{html.escape(relative)}" data-title="{html.escape(doc.title, quote=True)}"><p class="source">Source: {html.escape(relative)}</p>' + "".join(rewriter.output) + "</article>")
    if "README.md" not in documents:
        raise ValueError("Documentation requires README.md")
    badges = f'<span class="badge">{counts["skills"]} skills</span>'
    for key, label in (("historical_cases", "historical cases"), ("benchmark_items", "benchmark questions")):
        if key in counts:
            badges += f'<span class="badge">{counts[key]} {label}</span>'
    for output, title, start in (("docs/site/index.html", "MBSE Agents", "README.md"),
                                 ("docs/preview.html", "MBSE Agents · review packet", "docs/review/README.md")):
        active = documents.get(start, documents["README.md"])
        page = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width, initial-scale=1">'
                f'<title>{title}</title><style>{STYLE}</style></head><body data-start="{active.id}">'
                f'<header><strong>{title}</strong><p>Understand systems, develop connected artifacts, and examine the evidence.</p>{badges}</header>'
                '<div class="layout"><nav aria-label="Documentation">' + "".join(nav) + '</nav><main>'
                '<div class="toolbar"><button id="print-selected" type="button">Print this document</button><button id="print-all" type="button">Print whole packet</button></div>'
                f'<p class="build-note">Source snapshot SHA-256: {snapshot}</p>' + "".join(articles) +
                '</main></div><script>' + SCRIPT + '</script></body></html>\n')
        outputs[output] = page.encode()
    manifest = {"schema_version": 1, "generator": "scripts/render_preview.py", "markdown_version": markdown.__version__,
                "source_snapshot_sha256": snapshot, "counts": counts, "sources": source_hashes,
                "outputs": {path: digest(data) for path, data in sorted(outputs.items())},
                "limits": ["Source/byte freshness is not engineering acceptance or model-quality evidence.",
                           "Reviewer keys and historical planning archives remain outside the documentation bundle."]}
    outputs["docs/site/build-manifest.json"] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    for relative, original in sources.items():
        location = root / relative
        if relative in {"scripts/documentation.py", "scripts/render_preview.py"}:
            location = Path(__file__).with_name(Path(relative).name)
        if not location.is_file() or location.read_bytes() != original:
            raise ValueError(f"Documentation source changed during build: {relative}")
    return outputs


def stale_outputs(outputs: dict[str, bytes], root: Path = ROOT) -> list[str]:
    stale = [relative for relative, expected in outputs.items()
             if not (root / relative).is_file() or (root / relative).read_bytes() != expected]
    for path in sorted((root / "docs/site").rglob("*")):
        if path.is_file() and path.relative_to(root).as_posix() not in outputs:
            stale.append("unexpected " + path.relative_to(root).as_posix())
    return stale


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed outputs differ; never write")
    args = parser.parse_args()
    try:
        outputs = build_outputs()
        stale = stale_outputs(outputs)
        if args.check:
            if stale:
                parser.exit(1, "Stale documentation: " + ", ".join(stale) + "\n")
            print("Documentation and source-linked diagram current")
        else:
            for relative, data in outputs.items():
                target = ROOT / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            print(f"Built {len(outputs)} documentation files; public entrypoint: docs/site/index.html")
    except (OSError, ValueError, RuntimeError) as error:
        parser.exit(1, f"Documentation build failed: {error}\n")
