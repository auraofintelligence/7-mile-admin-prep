# 7-Mile planning and administration

Public workbench: **https://auraofintelligence.github.io/7-mile-admin-prep/**

A focused establishment and operating preparation hub for an Indigenous-led 7-Mile project on Minjerribah / North Stradbroke Island, Queensland. It brings together a proposed not-for-profit and Indigenous-majority commercial entity, permanent community living, cultural activities, food growing, making, medium-term residencies and short stays.

## Included

- 52 responsive pages: nine main destinations and 43 individual document pages.
- 91 tasks with phases, dependencies, document links and completion evidence.
- 43 document briefs with inputs, content and review checklists, source links and individual AI master prompts.
- 15 establishment and readiness checklists.
- 43 references, including official template download links and comparison sources.
- 14 local, state and federal agency entries with remits and useful questions.
- Generated landlocked bushland hero artwork on every page and a generated favicon.
- Site tree, footer previous/next links and a floating return-to-top button.
- Browser-local task/checklist notes, working-note JSON export/import, and seeded CSV/JSON downloads.

## Original plan customisation

The Original plan page maps 13 elements of the existing [7-Mile concept](https://auraofintelligence.github.io/multi-site-Minjerribah-network/seven-mile.html) into documents, tasks and checklists. It preserves permanent living, small-cluster layout, the proposed expandable-building and flexible-place mixes, existing dwelling transition, clean-up, shared kitchen and amenities, ceremony grounds, food forest, orchard, nursery, Tower Farm, commons and water harvesting.

`docs/ORIGINAL-PLAN-MAPPING.md` records the source-to-work mapping and quantity checks. `scripts/seven_mile_specific.py` maintains the customisation. Concept estimates remain separate from actual procurement, surveyed boundaries and operating capacity. The original rounded figures total about 54,259 m2 against about 54,228 m2 for 13.4 acres; the difference is visible rather than silently adjusted.

Maker-Space, Tip Loop and Capsule Surge are related proposals with distinct site and operator choices. Their interfaces are explored in D41; no co-location or partnership is assumed. Older financial C-Hour text on the Tip Loop site is excluded.

## Current planning positions

This is a working plan, not a record of incorporation or approval. ORIC not-for-profit and commercial Pty Ltd are working options. Indigenous member control in a not-for-profit is distinct from equity ownership in a commercial company. Direct ownership versus a community corporation subsidiary remains open.

Drafting and accounting setup are handled in-house. QYAC-assisted review through regular contractors is a possibility subject to agreement. Ready Sustainable Employment and Training Cooperative (Ready S.E.T. Co-op) is the proposed administration, employment and training interface; legal identity and service scope are verified before contracting.

**C-Hours have no financial aspect.** No conversion, tradable value, financial backing, wage substitution or financial claim is included. The latest express correction overrides older financial material in the supplied source pack.

The site is landlocked. The artwork is generated concept art, not photography of the actual property. 7-Mile is on a native title claim. Claim records, mapped boundaries, cultural permissions, existing agreements, survey, approvals and occupancy capacity are recorded in the land evidence pack. Temporary structures are not assumed exempt from approvals.

## Files and maintenance

The repository root contains the GitHub Pages site: HTML pages, `app.js`, `styles.css`, planning data, downloads and `assets/`. `scripts/build-content.py` is the source of planning content, prompts and CSV exports. `scripts/build-pages.py` creates the page shells, canonical URLs and sitemap. `docs/prompts/` provides readable Markdown briefs for all 43 documents. `docs/DECISIONS.md` records current choices and gaps.

```sh
python scripts/build-content.py
python scripts/build-pages.py
python scripts/validate.py
node --check app.js
node scripts/test-routing.cjs
node scripts/test-planning.cjs
```

No installation, framework or external hosting service is required. GitHub Pages publishes the static files from this repository. Run the generators after content changes, run the checks, then commit the generated files alongside the source changes.

## GitHub Pages publishing

GitHub Pages is the only intended public host. In repository **Settings → Pages**, the publishing source is **Deploy from a branch → main → / (root)**. GitHub builds and deploys changes pushed to that source. The root `index.html` is the actual home page, not a redirect to another hosting platform or build directory.

All internal links and assets are relative so they work under the `/7-mile-admin-prep/` project path. `.nojekyll` keeps the site static. `sitemap.xml`, `robots.txt` and page canonical URLs use the GitHub Pages address. The previous `/dist/*.html` paths forward to their matching root pages, preserving query strings and fragments.

This repository has no dependency on ChatGPT Sites and is not to be published there. A hosting-provider change requires an explicit user request.

## Working notes and public records

Task status, owner notes and document checklist ticks save in the visitor's browser. They do not write back to GitHub, update the public plan or sync between devices. Export from the Task register and import that backup elsewhere. Status changes approved for public release are edited in the source and reviewed before deployment.

Signed consents, identity details, private financial records, confidential reviews and restricted cultural material stay out of this public repository. The source attachment filenames and relevance notes are recorded on the Decisions page; raw attachments are not republished.

## Reference verification

Official pages and direct download locations were located on 10 October 2026. The linked binary templates were not opened during this build. Keep their landing pages as fallbacks, check the current version and confirm each precedent matches the legal structure. Financial thresholds, fees, licences and programme eligibility are verified again when used.

## Reuse

No new broad licence over cultural knowledge or project material is granted by this repository. Reference documents retain their publishers' terms. A licence and any intended reuse permissions remain a founding decision.
