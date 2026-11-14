# Distribution and discovery

Start with the repository's [skill catalog](skills.md) and [installation guide](../platform/codex/install.md).
The catalog and examples describe shipped content. They make no marketplace,
model-quality, certification, or vendor-compatibility claim.

For broader distribution, follow [OpenAI plugin packaging](https://developers.openai.com/plugins)
and check the current submission requirements. This repository has not been
submitted to a plugin directory. Do not publish or contact external communities
without a concrete release and the maintainer's publication direction.

## Static documentation

The [public reading entrypoint](site/index.html) covers installation, a supplied
first task, workflows, historical cases, teaching examples and the judgment
benchmark. The separate [review packet](preview.html) opens the dated assessment
records. Their selected reading content and local images are bundled in HTML;
external primary-source links still require network access.

Build with the optional pinned dependencies in `requirements-docs.txt`, then
run `python3 scripts/render_preview.py --check`. Publish the complete `docs/site`
directory only after release review. Its manifest binds source and output hashes;
it does not constitute a deployment receipt, model-quality result or engineering
approval. See [build and review details](review/README.md).
