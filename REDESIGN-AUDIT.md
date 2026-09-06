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
- Verify all 22 bibliography entries, four featured projects, search, filters,
  empty/reset behavior, no-JS readability, links, contact compatibility and SEO.
- Review at desktop, 390px and 320px. Check no page-width overflow and no clipped
  navigation, headings, photo or publication controls.
- Only commit personal-site files. Preserve every `nyc/` artifact and `CNAME`;
  verify Pages deployment and both the homepage and NYC route after release.

## Validation completed

`npm test` passes: 22 unique records, four additions, collective authorship,
search/topic/year filters, empty/reset states, copy-email success/fallback,
canonical/description metadata, local assets, safe outbound links and no-JS
readability. Real-browser review covered 1512px, 390px and 320px widths with no
horizontal page overflow. A narrow contact-heading wrap was corrected. No
browser console errors were observed. The local `/contact/` and `/nyc/` routes
both returned HTTP 200.
