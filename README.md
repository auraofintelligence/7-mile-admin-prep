# 7-Mile planning and administration

Public workbench: **https://seven-mile-planning-admin.auraofintelligence.chatgpt.site**

A focused establishment and operating preparation hub for an Indigenous-led 7-Mile project on Minjerribah / North Stradbroke Island, Queensland. It brings together a proposed not-for-profit and Indigenous-majority commercial entity, cultural activities and temporary accommodation/residencies.

## Included

- 38 responsive pages: eight main destinations and 30 individual document pages.
- 52 tasks with phases, dependencies, document links and completion evidence.
- 30 document briefs with inputs, content and review checklists, source links and individual AI master prompts.
- Eight establishment and readiness checklists.
- 32 references, including official template download links and comparison sources.
- 14 local, state and federal agency entries with remits and useful questions.
- Generated landlocked bushland hero artwork on every page and a generated favicon.
- Site tree, footer previous/next links and a floating return-to-top button.
- Browser-local task/checklist notes, working-note JSON export/import, and seeded CSV/JSON downloads.

## Current planning positions

This is a working plan, not a record of incorporation or approval. ORIC not-for-profit and commercial Pty Ltd are working options. Indigenous member control in a not-for-profit is distinct from equity ownership in a commercial company. Direct ownership versus a community corporation subsidiary remains open.

Drafting and accounting setup are handled in-house. QYAC-assisted review through regular contractors is a possibility subject to agreement. Ready Sustainable Employment and Training Cooperative (Ready S.E.T. Co-op) is the proposed administration, employment and training interface; legal identity and service scope are verified before contracting.

**C-Hours have no financial aspect.** No conversion, tradable value, financial backing, wage substitution or financial claim is included. The latest express correction overrides older financial material in the supplied source pack.

The site is landlocked. The artwork is generated concept art, not photography of the actual property. Lot/plan, tenure, survey, approvals and occupancy capacity remain evidence tasks. Temporary structures are not assumed exempt from approvals.

## Files and maintenance

`dist/` contains the deployable static site. `scripts/build-content.py` is the source of planning content, prompts and CSV exports. `scripts/build-pages.py` creates the page shells. `dist/app.js` contains the interactive workbench; `dist/styles.css` its visual system. `docs/prompts/` provides readable Markdown briefs for all 30 documents. `docs/DECISIONS.md` records current choices and gaps.

```sh
python scripts/build-content.py
python scripts/build-pages.py
python scripts/validate.py
node --check dist/app.js
```

No installation or framework build is required. Serve `dist/` with any static web host. The public Site is deployed separately; a GitHub commit does not automatically update it. Future changes are validated, pushed and deployed as a matching Site version.

## Optional GitHub Pages mirror

GitHub Pages is not enabled in the initial repository metadata. To use an additional GitHub Pages URL, open repository **Settings → Pages**, select **Deploy from a branch**, choose `main` and `/ (root)`, then Save. The root landing page redirects to `dist/index.html`. This repository does not claim that mirror is live until GitHub confirms deployment.

## Working notes and public records

Task status, owner notes and document checklist ticks save in the visitor's browser. They do not write back to GitHub, update the public plan or sync between devices. Export from the Task register and import that backup elsewhere. Status changes approved for public release are edited in the source and reviewed before deployment.

Signed consents, identity details, private financial records, confidential reviews and restricted cultural material stay out of this public repository. The source attachment filenames and relevance notes are recorded on the Decisions page; raw attachments are not republished.

## Reference verification

Official pages and direct download locations were located on 10 October 2026. The linked binary templates were not opened during this build. Keep their landing pages as fallbacks, check the current version and confirm each precedent matches the legal structure. Financial thresholds, fees, licences and programme eligibility are verified again when used.

## Reuse

No new broad licence over cultural knowledge or project material is granted by this repository. Reference documents retain their publishers' terms. A licence and any intended reuse permissions remain a founding decision.
