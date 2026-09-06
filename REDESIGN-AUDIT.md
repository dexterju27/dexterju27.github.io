# Personal-site redesign — September 5, 2026

## Findings addressed

- The previous homepage was a long, single-column biography/publication list
  with almost no direct paper links, no topic/year search and a separate sparse
  contact page.
- The 18,881,005-byte portrait lacked alt text. The new responsive WebP versions
  are 49,222 and 138,614 bytes; the original remains untouched.
- Site configuration had a malformed, outdated canonical URL. Static pages now
  supply correct canonical URLs, descriptions, social metadata and Person JSON-LD.
- The main content is readable without JavaScript. Filters, status messages,
  reduced-motion support, focus indicators and skip navigation improve usability.

## Publication reconciliation

The public Scholar profile `YW5jp5QAAAAJ` was read, including all 23 rows (Show
more was disabled). Four works absent from the previous 18-work website were
added: MAI-Thinking-1 (2026), the Llama 4 release report (2025), Open-domain
conversational agents: Current progress… (2020), and Growing Up Together (2019).

The duplicate trailing-year BlenderBot 3 citation was not added a second time.
Team authorship remains explicit. Paper destinations were resolved from Scholar
and Crossref, including ACL Anthology and NeurIPS proceedings. arXiv identifiers
and the new official Microsoft/Meta report pages were checked. Scholar itself
was not edited. The official MAI model introduction has
2026 publication/update dates, resolving an inconsistent 2025 clustered citation.

Domain Regeneration now links to Findings of ACL 2025; Karen Ullrich's name was
corrected against the proceedings metadata. Final conference/journal years and
earlier preprint dates are differentiated instead of duplicating works.

## Preservation and release gates

- Preserve current Microsoft AI/Meta/FAIR biography, original public contact
  destinations, education, portrait source and HELLA thesis ownership statement.
- Do not infer job start dates, individual leadership of team reports, or new
  personal facts. The NYC guide is a clearly labeled personal project.
- Verify all 22 bibliography entries, five featured projects, search, filters,
  empty/reset behavior, no-JS readability, links, contact compatibility and SEO.
- Review at desktop, 390px and 320px. Check no page-width overflow and no clipped
  navigation, headings, photo or publication controls.
- Only commit personal-site files. Preserve every `nyc/` artifact and `CNAME`;
  verify Pages deployment and both the homepage and NYC route after release.

## Validation completed

`npm test` passes: 22 unique records, four additions, collective authorship,
search/topic/year filters, empty/reset states, email-privacy regressions,
canonical/description metadata, local assets, safe outbound links and no-JS
readability. Real-browser review covered 1512px, 390px and 320px widths with no
horizontal page overflow. A narrow contact-heading wrap was corrected. No
browser console errors were observed. The local `/contact/` and `/nyc/` routes
both returned HTTP 200.

## Follow-up content and privacy updates

The user requested a photo-free homepage. The intro now uses a two-column text
layout that stacks on smaller screens. Photo markup, social-image tags and the
Person image field were removed. Original/optimized portrait files are retained
in Git but excluded from Pages; no files or history were deleted.

The user corrected the previous Meta affiliation to Meta Superintelligence Labs
(MSL); biography, background and page descriptions now use that name. Collective
publication authorship remains Meta AI where that is the report's credit.

The live pages no longer contain an email address, mailto link or copy-email
button. Contact uses the existing public profile links; older Git history was
not rewritten.

Llama 4 is included in the five highlighted works. Its highlight describes the
model family and the user's stated contribution to reinforcement learning and
reasoning, not the release announcement. The bibliography retains Meta AI's
collective report authorship. To the Globe is explicitly
labeled agentic research. Staircase Attention adds only one requested sentence
making the chronology explicit: looped-transformer ideas were explored in the
2021 preprint. This does not claim first-ever priority over all recurrent models.

Every bibliography entry now has a clearly labeled paper/report destination.
The resource audit covers all 22 works: eight ACL Anthology pages, four public
presentation videos, NeurIPS and ICML presentation pages, and verified official
Meta/Microsoft posts or research records where found. Unrelated search results
were not used as substitute blog links. Meta research records are labeled
separately from blog posts. Videos are linked, not embedded or preloaded.

## Final design and accessibility refinement

- Kept the existing warm neutral palette, serif headings and simple line motifs.
  The five highlights use a full-width lead card and two balanced pairs.
- Increased publication authors and resource labels to 12px, card descriptions
  to 13px, and mobile form inputs to 16px. Phone publication rows put the year
  and venue above the title rather than squeezing text beside a narrow column.
- Publication resources, topic filters and visible navigation links have at
  least 44px-high targets. Removed the redundant outbound arrow from each paper;
  the title and labeled resources remain linked.
- Resetting filters returns keyboard focus to search. Card focus outlines remain
  visible, and print styling hides the empty-search message while showing all
  publications. Removed unused email/copy/toast styling.

Validation: `npm test` passes, including structural axe checks for the homepage
and contact page, no-JS content and privacy checks. `npm audit` reports zero
known dependency vulnerabilities. `tests/browser-audit.html` runs real rendered
axe, overflow and control-size checks at 1512, 768, 390 and 320px on both routes:
zero reported violations, horizontal overflow or undersized tested controls.
Visual review covered desktop highlights/publications, phone search/results and
the narrow contact layout.

The rendered audit marks decorative arrow glyphs and the 320px translucent map
background for manual contrast review. The map paragraph's text contrast is
7.78:1 against the base background and at least 4.94:1 even against the brightest
16%-opacity map overlay; arrows are decorative and accompany text labels.
These automated checks are not a claim of complete WCAG certification.

The browser-audit harness and axe dependency are development-only and excluded
from GitHub Pages. There are still no analytics, external fonts, runtime API
keys, embedded videos, or exposed email addresses in the personal pages.
