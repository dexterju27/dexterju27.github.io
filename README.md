# Dexter Ju — personal website

Live at **https://dexterju.me/**. A lightweight, static research profile with
selected work, a searchable bibliography, background, contact links and the NYC
guide. No framework, analytics, external fonts or runtime API keys are required.

## Editing

- `_data/publications.json`: the bibliography and selected-work cards.
- `_data/scholar-audit.json`: provenance and the last Scholar comparison.
- `_data/publication-resources.json`: verified conference, presentation/video,
  official research-blog, code and dataset links. Resources are omitted when not verified.
- `_data/code-release-audit.json`: paper-to-repository evidence, archive status,
  license notes and coverage of all 22 works. Code/data links must match this audit.
- `tools/templates/`: homepage, contact page and shared layout.
- `assets/css/personal.css` and `assets/js/personal.js`: styling and enhancement.

After editing content, templates, or assets:

```sh
python3 tools/build_site.py
npm install
npm test
npm run dev
```

The builder writes `index.html`, `contact.html`, `contact/index.html` and
`sitemap.xml`. Commit these generated files along with the source changes.
CSS and JavaScript URLs include content hashes so a new page loads matching
assets instead of a cached older design.
GitHub Pages serves them as static files. The legacy `/contact` route remains
available. All publications and contact links work without JavaScript.

`npm test` includes structural accessibility checks. With the local server
running, open `http://127.0.0.1:8770/tests/browser-audit.html` for rendered axe,
responsive-overflow and tap-target checks, plus an interactive width/section
preview. Review any incomplete contrast checks manually. Tests and dependencies
are excluded from the published site.

Contact uses profile links only. Do not add an email address to the pages,
`mailto:` URLs, metadata or copy-button attributes.

The homepage is photo-free. Portrait files remain preserved in the repository,
but are excluded from GitHub Pages and are not referenced in page markup,
social-preview metadata or structured data. Do not reintroduce them without a
request. The original image and bachelor's thesis stay intact.

## Publication policy

The September 5, 2026 audit found 23 Scholar rows representing 22 distinct works.
The repeated BlenderBot 3 citation is one work, not two. Collective Microsoft AI
and Meta AI reports retain team authorship. Final proceedings/journal years are
used when available, with earlier preprint years noted. Source links and audit
notes are retained; no citation-count claims are embedded in the homepage.

Code links are shown for 14 verified releases and surfaced on four highlights.
FLORES-101 has a separate dataset link. Prefer paper-specific project folders or
README anchors, and preserve required release versions (e.g. ParlAI 1.4.1 for
multi-modal dialogue). A public code link does not imply an OSI-approved license,
released training data, or that an entire RL training pipeline is available.

## Keep the NYC guide independent

`/nyc/` is generated on Azure and published independently. **Do not regenerate,
replace or delete its files as part of a personal-site edit.** The homepage
builder does not write under `nyc/`. Pull/rebase before pushing if the daily NYC
publisher advanced the branch. Preserve `CNAME` and the Pages configuration.

## History and license

The old Markdown homepage and contact page remain recoverable in Git history.
The original site used Ankit Sultana's Researcher Jekyll template; its legacy
layout/Sass files and GNU GPL v3 license are preserved. The 2026 personal-page
layout and lightweight static builder are a new implementation.
