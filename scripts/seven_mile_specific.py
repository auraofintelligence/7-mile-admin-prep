from pathlib import Path
import csv, io, json

ORIGINAL = 'https://auraofintelligence.github.io/multi-site-Minjerribah-network/seven-mile.html'

def customise(doc, task, ref, docs, tasks, checklists, base, refs):
    extra_refs = [
        ('maker', 'Straddie Maker-Space Lab', 'https://auraofintelligence.github.io/straddie-makerspace-lab/', 'Repair, tool sharing, learning and material experiments. Its Dunwich / Goompi proposal is a separate location discussion, not an established 7-Mile facility.'),
        ('maker-proposal', 'Maker-Space: room and location proposal', 'https://auraofintelligence.github.io/straddie-makerspace-lab/proposal.html', 'Clean and dirty work zones, storage, access, neighbours and staged room options inform a smaller 7-Mile making brief.'),
        ('maker-tools', 'Maker-Space: compact tools and stewardship', 'https://auraofintelligence.github.io/straddie-makerspace-lab/tools.html', 'Tool walls, repair benches, parts libraries, shared ownership, induction and maintenance are adaptable practices.'),
        ('tip-loop', 'Straddie Tip Loop Lab', 'https://auraofintelligence.github.io/straddie-tip-loop-lab/', 'Offer, read, choose, teach and prove provides a model for consentful material recovery and outcome records.'),
        ('tip-loop-design', 'Tip Loop: lawful handover and recovery', 'https://auraofintelligence.github.io/straddie-tip-loop-lab/loop.html', 'Use permission, triage, secure storage and repair/reuse/parts/recycling pathways. No waste-centre access or operating partnership is inferred.'),
        ('tip-governance', 'Tip Loop: pilot governance', 'https://auraofintelligence.github.io/straddie-tip-loop-lab/governance.html', 'Repair and learning evidence is relevant. Older issuance, redemption and regenerative-asset financial language is superseded by the current instruction that C-Hours have no financial aspect.'),
        ('capsule', 'Straddie Capsule Surge Lab', 'https://auraofintelligence.github.io/straddie-capsule-surge-lab/', 'A separate site-neutral concept for visiting workers, shared facilities, local compute and civic rehearsal. Explore compatibility rather than assume relocation to 7-Mile.'),
        ('capsule-boundaries', 'Capsule Surge: location and operating boundaries', 'https://auraofintelligence.github.io/straddie-capsule-surge-lab/boundaries.html', 'The lab has no chosen site. Compute and health-support ideas need separate scope, service capacity and consent decisions.'),
    ]
    for rid, title, url, note in extra_refs:
        ref(rid, title, url, 'Project', note)
    ref('nntt', 'NNTT: search native title registers and applications', 'https://www.nntt.gov.au/search-the-registers', 'Planning', 'Locate claim, application, determination and agreement records relevant to the mapped area. No specific claim number or determination is asserted by this hub.')
    ref('ntv', 'NNTT: Native Title Vision', 'https://www.nntt.gov.au/assistance/geospatial/native-title-vision', 'Planning', 'Mapping input for a site-specific records search. The firebreak trace does not identify a claim boundary.')
    ref('food-business', 'Redland: starting a new food business', 'https://www.redland.qld.gov.au/Community-safety-and-health/Food-health-and-safety/Starting-a-new-food-business', 'Planning', 'Ask Council about design, fit-out and licensing for the proposed shared kitchen and actual food service model.')

    specs = [
        ('D31', '7-Mile site master brief and concept register', 'Land & approvals',
         'Turn the original Noonuccal-led living-community concept into a staged site brief with a traceable area and use register.',
         'Original page and working map; native title claim records; cultural direction; on-ground observations; proposed household and visitor uses',
         '15-acre site description versus 13.4-acre firebreak trace; 1.02 km measured path; site-use schedule; concept quantities and arithmetic; retained scrub and cultural exclusions; quiet living and vehicle separation; small-cluster layout options; stage and evidence register',
         'Keep described area separate from measured trace and surveyed boundary; distinguish buildings, pitches and people; preserve source figures as estimates; do not turn the concept into a commitment',
         'seven-mile, nntt, ntv', 'D01, D02, D03'),
        ('D32', 'Permanent community living and residency framework', 'Business & operations',
         'Plan permanent residents, medium-term residencies and short stays as three distinct parts of community life.',
         'Cultural direction; resident aspirations; family and accessibility needs; proposed stay lengths; permissions; entity responsibilities',
         'Permanent living purpose; resident and guest categories; allocation and eligibility choices; occupancy arrangement review; privacy and quiet areas; children and accessibility; resident contributions and service costs; arrival departure and dispute process; community versus commercial operator responsibilities',
         'Do not replace permanent living with visitor accommodation; no assumed resident eligibility or signed occupancy rights; voluntary contribution and C-Hours do not buy occupancy or replace wages',
         'seven-mile, redland-plan', 'D02, D03, D12, D31'),
        ('D33', 'Site clean-up and material sorting plan', 'Land & approvals',
         'Organise the clean-up, sorting and on-ground recording already identified in the original concept.',
         'Site walk and permitted access; material ownership; existing piles and structures; cultural exclusions; disposal options; crew skills',
         'Photographic and condition baseline; cultural no-disturbance areas; item owner and handover record; repair reuse parts recycle and disposal categories; unknown-material isolation and review; work sequence; transport and storage; daily close and outcome evidence',
         'No assumed permission to clear vegetation or take objects; unknown batteries chemicals and suspect materials get competent handling review; clean-up records do not authorise later building works',
         'seven-mile, tip-loop, tip-loop-design', 'D02, D03, D31'),
        ('D34', 'Existing dwelling and replacement-home transition brief', 'Land & approvals',
         'Evaluate repurposing the handmade dwelling after an expandable replacement home is established.',
         'Current occupants and agreed preferences kept private; dwelling condition; service connections; replacement-home specification; proposed shared uses',
         'Current use and condition; replacement-home option; private continuity of accommodation; relocation and commissioning sequence; shared-use alternatives; repair and accessibility requirements; services and fire review; operator and maintenance owner; decision and handover',
         'Do not describe relocation or repurposing as agreed; replacement suitability and permissions precede any displacement; record a retain repair or defer option',
         'seven-mile, redland-plan', 'D03, D31, D35'),
        ('D35', 'Modular buildings and staged procurement schedule', 'Land & approvals',
         'Test the proposed expandable buildings and standard containers against real uses, island delivery and service capacity.',
         'Original quantity schedule; household and studio needs; supplier dimensions and evidence; freight access; foundations; utility loads; actual quotes',
         '20 expandable 40-foot options at about 74 m2 each; 20 expandable 20-foot options at about 37 m2 each; 30 standard 20-foot options at about 15 m2 each; use and occupancy for each type; foundations and assembly; ferry freight unloading and lifting; ventilation shade and accessibility; cost and maintenance schedule; staged purchase or hire decision',
         '70 proposed structures is not 70 dwellings or a bed count; supplier dimensions replace rounded concept areas; no automatic exemption for containers or removable structures; no order is implied by a planning quantity',
         'seven-mile, redland-plan, business-plan', 'D03, D18, D31'),
        ('D36', 'Flexible visitor places and vehicle movement plan', 'Land & approvals',
         'Develop the tent, van, caravan, bus and house-truck options alongside sandy tracks and turning space.',
         'Original visitor-place mix; stay categories; vehicle dimensions; access observations; amenity capacity; proposed circulation and separation',
         '40 tent swag or small-van options at about 65 m2 each; 15 caravan or larger-rig options at about 90 m2 each; 10 bus or house-truck options at about 125 m2 each; spacing shade and drainage; arrival and unloading; parking and pedestrians; sandy-track options around 4 m width; turning and emergency movement; operating capacity by stage',
         '65 flexible places is not a people or beds limit; the roughly 800 m track equivalent is an area exercise not a surveyed road length; assess permanent vehicle living separately from visitor stays',
         'seven-mile, redland-plan', 'D18, D21, D31, D32'),
        ('D37', 'Shared kitchen cold storage and amenities operating brief', 'Business & operations',
         'Plan the shared kitchen, cold storage and three amenity blocks as serviced community facilities.',
         'Proposed meal and food sales model; actual users by stage; kitchen location; cold-chain loads; amenities and accessibility needs; utilities',
         'Shared kitchen and commercial service choices; roughly 350 m2 combined concept allowance; three amenity-block options; toilets showers laundry and accessibility; food-business questions; cold storage and outage response; cleaning and bookings; household and event access; paid roles consumables and maintenance',
         'An area allowance does not establish facility capacity; confirm food design and licensing pathway with Council for actual activities; keep private household cooking separate from public food service assumptions',
         'seven-mile, food-business, redland-plan', 'D18, D31, D32, D42'),
        ('D38', 'Food forest gardens and Tower Farm plan', 'Business & operations',
         'Bring the food forest, bush orchard, gardens, bush tucker nursery, Tower Farm and Seedling Hub into a practical growing programme.',
         'Cultural plant knowledge permissions; soil and water observations; species choices; growing skills; kitchen needs; seasonal labour; trial equipment costs',
         'Food forest and bush orchard concept around 18000 m2; gardens and bush tucker nursery around 6000 m2; Tower Farm and Seedling Hub around 1000 m2 beside the kitchen; soil and irrigation trials; authorised propagation and cultural knowledge; harvest and kitchen handoff; compost and pest practices; seasonal roster; staged yield and cost evidence',
         'No invented yields or species permissions; soil water and shade observations precede planting commitments; separate food forest orchard nursery and tower-system needs; tower production does not replace the broader gardens',
         'seven-mile, food-business', 'D02, D31, D42'),
        ('D39', 'Ceremony cultural grounds and gathering brief', 'Business & operations',
         'Plan ceremony grounds, yarning, teaching and gathering under the relevant Noonuccal cultural direction.',
         'Cultural decision process; approved public activities; private restricted areas; noise and privacy preferences; gathering needs; access',
         'Ceremony and cultural grounds concept around 8000 m2; yarning and teaching spaces; restricted and public boundaries; quiet hours and event scheduling; shade and accessible paths; host and cultural remuneration; recording permissions; visitor conduct; restoration after gatherings',
         'Do not invent ceremonies motifs names or authority; a mapped allowance is not an event attendance limit; cultural use is not automatically a saleable tourism product',
         'seven-mile, heritage, heritage-search', 'D02, D20, D26, D31'),
        ('D40', '7-Mile making repair and tool-sharing brief', 'Business & operations',
         'Define a suitable making and learning space at 7-Mile with practical links to the separate Maker-Space and Tip Loop proposals.',
         'Local making needs; repair skills; cultural direction; available tools; noise and dust separation; storage; maintenance stewards',
         'Small first workshop scope; clean learning and dirty work zones; repair intake and consent; tool ownership borrowing and induction; parts library and material rack; supervised learning rotations; dust power noise and fire review; consumables and maintenance; public outcome records',
         'The Dunwich Maker-Space is a separate proposal; avoid copying its full industrial equipment wish list into 7-Mile procurement; no waste-centre collection or free access to partner tools is assumed',
         'seven-mile, maker, maker-proposal, maker-tools, tip-loop-design', 'D25, D31, D33'),
        ('D41', 'Connected labs and service interface register', 'Relationships',
         'Record useful relationships with Maker-Space, Tip Loop and Capsule Surge without assuming shared sites, ownership or agreements.',
         'Linked public plans; proposed contacts; 7-Mile needs; transport distances; service costs; legal operators; scope and permissions',
         'Separate site and operator register; repair training and tool-loan possibilities; consentful recovered-material handover; visiting-worker and specialist-stay compatibility; optional local-compute brief; transport and scheduling; proposed agreement and responsibility matrix; source conflicts; confirm defer or decline choices',
         'Maker-Space Dunwich and site-neutral Capsule Surge are not established at 7-Mile; no clinical service compute rack or partner commitment is inferred; older financial C-Hour framing is excluded',
         'seven-mile, maker, tip-loop, tip-governance, capsule, capsule-boundaries, set-node', 'D12, D13, D31, D40'),
        ('D42', 'Commons water harvesting and site services plan', 'Land & approvals',
         'Coordinate commons, water harvesting and the service loads behind homes, gardens, kitchens and visitor places.',
         'On-ground ground-level and drainage observations; utilities evidence; household and guest scenarios; garden loads; kitchen and cold-storage equipment; access and outage needs',
         'Commons and water-harvesting concept around 8159 m2; potable and non-potable uses; roof catchments storage and irrigation; toilets showers laundry and wastewater; power cold chain and communications; shade and meeting space; drainage and rainfall response; service-load scenarios; maintenance and outage actions',
         'Raised dry ground described in the concept is not a flood or drainage assessment; no assumed creek extraction; no verified water yield wastewater capacity or available utility connection; use stage-specific demand rather than all concept structures at once',
         'seven-mile, redland-plan, capsule-boundaries', 'D03, D18, D31'),
        ('D43', 'Shared community life and stewardship handbook', 'Business & operations',
         'Make everyday life, welcoming, learning and stewardship work across residents, guests and cultural hosts.',
         'Resident preferences; cultural governance; activity calendar; staffing; kitchen and workshop arrangements; contributions; complaint contacts',
         'Welcome and plain-language community agreements; quiet living and visiting hours; shared cooking gardens tools and facilities; resident guest and host responsibilities; cultural gathering calendar; learning and paid-work pathways; voluntary C-Hour recognition; mediation and escalation; cleaning maintenance and review',
         'Community agreement does not substitute for occupancy or employment rights; no compulsory cultural participation; keep private household details private; C-Hours create no financial or occupancy entitlement',
         'seven-mile, maker, set-node', 'D12, D25, D26, D32, D37, D39'),
    ]
    for r in refs:
        if r['kind']=='Project' and r['id'] in {row[0] for row in extra_refs}|{'seven-mile'}:
            r['verification']='Project HTML reviewed from repository source on 10 October 2026'
        if r['id']=='seven-mile':
            r['note']='Original Noonuccal-led lived-community concept: permanent residents, medium-term residencies, short stays, ceremony, food growing, making and learning. Mapped into specific briefs and tasks; quantities remain a rough exercise.'

    for row in specs:
        doc(*row)

    additions = [
        ('T53','Capture the original site plan and founder corrections','Site planning','Prepare','D31','','Source register links every original concept section and records native title claim and non-financial C-Hour corrections.'),
        ('T54','Reconcile areas structure counts and flexible-place estimates','Site planning','Investigate','D31','T53','Area calculations show rounding; 15 acres and the 13.4-acre trace stay separate; structures and pitches are not treated as people capacity.'),
        ('T55','Sketch culturally directed clusters and retained areas','Site planning','Draft','D31','T02, T03, T54','Layout options separate ceremony quiet living growing work and vehicle movement; restricted areas remain private.'),
        ('T56','Record permanent resident medium-term and short-stay needs','Community living','Prepare','D32','T02, T53','Three use categories include household privacy accessibility and shared-service needs without publishing personal details.'),
        ('T57','Set resident allocation and occupancy arrangement questions','Community living','Decide','D32','T03, T19, T56','Allocation choices operator responsibility and occupancy questions are recorded for review; no rights or residents are invented.'),
        ('T58','Draft the permanent living and residency framework','Community living','Draft','D32','T57','Permanent living has its own plan rather than being folded into short-stay bookings.'),
        ('T59','Record existing materials structures and clean-up areas','Site preparation','Investigate','D33','T02, T03','An authorised site walk records conditions owners access and cultural exclusions before disturbance.'),
        ('T60','Plan material sorting reuse storage and disposal','Site preparation','Draft','D33','T59','Each stream has a permission handling owner storage and destination; unknown materials have a review pathway.'),
        ('T61','Carry out the authorised clean-up stage and record outcomes','Site preparation','Prepare','D33','T60','The agreed stage records actual permissions work undertaken items reused disposal evidence and remaining issues.'),
        ('T62','Record existing dwelling condition and shared-use options','Site preparation','Investigate','D34','T03, T56','Current occupant preferences remain private; retain repair repurpose and defer options are documented.'),
        ('T63','Plan the replacement-home and dwelling transition sequence','Site preparation','Draft','D34','T62, T66','Replacement suitability services permissions and accommodation continuity precede any proposed move.'),
        ('T64','Record a dwelling transition decision and handover conditions','Site preparation','Decide','D34','T63','Authorised decision names the chosen option evidence conditions and responsible people without assuming displacement.'),
        ('T65','Match expandable buildings and containers to actual uses','Buildings & places','Prepare','D35','T54, T56','The 20/20/30 concept mix is classified by household studio work storage or shared use; no bed count is inferred.'),
        ('T66','Check modular specifications delivery foundations and costs','Buildings & places','Investigate','D35','T28, T32, T65','Supplier evidence and quotes cover dimensions ferry freight access lifting assembly foundations services and maintenance.'),
        ('T67','Choose a staged modular purchase hire or defer schedule','Buildings & places','Decide','D35','T41, T66','The chosen stage has an asset owner real costs permissions and a procurement gate; full concept quantities are not an order.'),
        ('T68','Describe the tent van caravan bus and house-truck options','Buildings & places','Prepare','D36','T38, T54, T56','The 40/15/10 place mix records stay type footprints shade amenities and visitor-versus-resident use.'),
        ('T69','Test sandy tracks turning loops and pedestrian separation','Buildings & places','Investigate','D36','T32, T55, T68','Vehicle dimensions on-ground observations and emergency movement inform the layout; the 800 m equivalent stays an estimate.'),
        ('T70','Set stage-specific flexible-place capacity and arrival rules','Buildings & places','Draft','D36','T69','Capacity follows actual service and permission evidence; 65 places is not a people limit.'),
        ('T71','Specify shared kitchen cold storage and three amenity options','Shared facilities','Prepare','D37','T56, T65','The brief states actual household event and food-service needs and replaces area allowances with equipment and user scenarios.'),
        ('T72','Record kitchen design food-service and amenities responses','Shared facilities','Review','D37','T28, T71, T87','Written responses address the proposed service model accessible amenities utilities and cleaning responsibilities.'),
        ('T73','Draft kitchen cold-chain and amenities operating routines','Shared facilities','Draft','D37','T72','Bookings cleaning cold-chain outage actions consumables staffing and maintenance are assigned for the chosen stage.'),
        ('T74','Define food forest orchard garden and nursery trial areas','Growing & commons','Prepare','D38','T02, T55','Cultural plant permissions soil shade and water observations inform each distinct growing area.'),
        ('T75','Design a Tower Farm and Seedling Hub trial beside the kitchen','Growing & commons','Draft','D38','T71, T74, T87','The trial records method equipment water power crop choices costs and measured learning rather than invented yields.'),
        ('T76','Set seasonal growing harvest and kitchen handoff routines','Growing & commons','Draft','D38','T75','Roles irrigation compost pest practices harvest and food handoff support a small documented growing stage.'),
        ('T77','Record cultural directions for ceremony yarning and gathering','Culture & gatherings','Prepare','D39','T02, T55','Relevant cultural decision holders shape uses access and sensitive areas; restricted directions stay private.'),
        ('T78','Plan shade access quiet separation and gathering services','Culture & gatherings','Draft','D39','T32, T77','The roughly 8000 m2 concept area has a needs brief; attendance is assessed separately from area.'),
        ('T79','Agree gathering calendar host roles and recording permissions','Culture & gatherings','Decide','D39','T35, T45, T78','Cultural gatherings teaching and public offerings have distinct permissions host arrangements and scheduling.'),
        ('T80','Choose first making repair and tool-sharing activities','Making & learning','Decide','D40','T44, T53','A small 7-Mile workshop scope records users mentors and tools; the separate Dunwich proposal is identified.'),
        ('T81','Plan workshop zones storage induction and material intake','Making & learning','Draft','D40','T60, T80','Clean and dirty zones tool stewards borrowing and consentful material intake have practical routines.'),
        ('T82','Prepare a supervised repair and learning session','Making & learning','Prepare','D40','T43, T81','The session brief names mentors permitted tools safety arrangements costs and outcome records for review before running.'),
        ('T83','Map separate Maker-Space Tip Loop and Capsule Surge interfaces','Connected projects','Prepare','D41','T53','The register distinguishes proposed sites operators needs and source conflicts; no partnership or co-location is asserted.'),
        ('T84','Prepare proposed tool material training and specialist-stay terms','Connected projects','Draft','D41','T20, T81, T83','Draft interfaces identify permissions ownership transport service costs data choices and each party responsibility.'),
        ('T85','Record confirm defer or decline decisions for each interface','Connected projects','Decide','D41','T84','Only actual agreements are marked confirmed; compute and health-support ideas retain separate scope decisions.'),
        ('T86','Build household visitor kitchen garden and workshop load scenarios','Growing & commons','Prepare','D42','T32, T56, T65, T68, T71, T74, T80','Service demand distinguishes residents visitors food growing cold storage workshop use and optional compute.'),
        ('T87','Test water harvesting wastewater power and outage options','Growing & commons','Investigate','D42','T86','Options record site evidence quoted services maintenance potable/non-potable separation and staged capacity.'),
        ('T88','Draft commons and service commissioning schedule','Growing & commons','Draft','D42','T55, T87','Each chosen facility has a service owner commissioning evidence maintenance and an outage plan.'),
        ('T89','Draft everyday resident guest and host community agreements','Community living','Draft','D43','T58, T73, T79','Welcome quiet hours shared facilities responsibilities and cultural boundaries reflect distinct resident and guest needs.'),
        ('T90','Set voluntary stewardship learning and contribution routines','Community living','Decide','D43','T44, T76, T81, T89','Paid work voluntary contribution maintenance and training remain distinct; C-Hours create no financial or occupancy entitlement.'),
        ('T91','Rehearse shared-life routines and review the selected stage','Community living','Review','D43','T90','A tabletop rehearsal records welcome bookings meals tools complaints maintenance and actions for the selected stage.'),
    ]
    for row in additions:
        task(*row)

    extensions = {
        'D01': ('Permanent residents medium-term residencies and short stays from the original site', 'Noonuccal-led living community and retained space for culture food growing and making'),
        'D03': ('Original working firebreak map and source section', 'Native title register search and agreement evidence kept separate from the working map'),
        'D18': ('Use schedules D31 D32 D35 D36 D37 D39 and D40 for the selected stage', 'Separate permanent living flexible visitor places shared food service workshop and gathering questions'),
        'D19': ('Site master brief and staged service-load schedule D31 and D42', 'Expandable buildings dwelling transition visitor places kitchen amenities gardens and commons interface'),
        'D20': ('Ceremony and gathering brief D39 and workshop learning brief D40', 'Distinct cultural gatherings approved public offerings and learning sessions'),
        'D21': ('Permanent living framework D32 and flexible-place plan D36', 'Medium-term residency and short-stay inventory kept separate from permanent homes'),
        'D22': ('Staged modular kitchen growing workshop and utilities costs', 'Stage-level capital and ongoing service costs with no assumed sale of all concept capacity'),
        'D23': ('Shared-life handbook D43 and actual facility routines', 'Permanent resident versus guest rules and shared kitchen workshop and garden handoffs'),
        'D24': ('Dwelling modular vehicle workshop garden and food-service hazards for the selected stage', 'Resident and guest evacuation accessible movement cold-chain outage and repair session risks'),
        'D25': ('Growing kitchen workshop maintenance hosting and site-preparation roles', 'Try-one-skill learning rotations with actual mentoring and separate paid and voluntary roles'),
        'D28': ('Modular supplier evidence D35 and separate tool owners D40', 'Freight foundations services cold storage growing tools and maintenance by chosen stage'),
        'D29': ('Only the site-specific briefs relevant to the proposed first stage', 'Separate permanent-living activity and stay decisions with chosen-stage service commissioning evidence'),
        'D30': ('Original-plan mapping and source arithmetic register D31', 'Decisions to retain revise defer or decline original concept elements'),
    }
    by_doc = {d['id']: d for d in docs}
    for did, (inp, section) in extensions.items():
        by_doc[did]['inputs'].append(inp)
        by_doc[did]['sections'].append(section)
    by_doc['D03']['sources'] += ['seven-mile', 'nntt', 'ntv']
    by_doc['D21']['purpose'] = 'Plan medium-term residencies and short stays alongside a separate permanent community living framework.'
    by_task = {t['id']: t for t in tasks}
    by_task['T27']['title'] = 'Describe permanent living day activities residencies and short stays separately'
    by_task['T27']['acceptance'] = 'Each use category has its own numbers durations facilities and works description; permanent living remains part of the project.'
    by_task['T33']['acceptance'] = 'The chosen stage integrates site layout modular or visitor places shared services and cultural direction with relevant evidence.'
    by_task['T49']['acceptance'] = 'Evidence covers the exact first stage and its relevant site-specific briefs; later-stage works do not become blanket prerequisites.'
    for d in docs:
        d['prompt'] = base + '\nDOCUMENT: '+d['title']+'\nPURPOSE: '+d['purpose']+'\nINPUTS TO REQUEST: '+'; '.join(d['inputs'])+'\nDOCUMENT CONTENT: '+'; '.join(d['sections'])+'\nDOCUMENT-SPECIFIC REVIEW: '+'; '.join(d['checks'])+'\nREFERENCE IDS: '+', '.join(d['sources'])+'\nDEPENDENCIES: '+(', '.join(d['depends']) or 'No prerequisite beyond the source and decision registers.')+'\n'

    new_lists = [
        ('C09', 'Original plan and site layout', ['T53','T54','T55'], 'Read the concept, reconcile its estimates and shape small clusters around cultural direction.'),
        ('C10', 'Permanent living and shared community life', ['T56','T57','T58','T89','T90','T91'], 'Residents, medium-term guests and short-stay visitors have distinct arrangements and shared routines.'),
        ('C11', 'Clean-up and existing dwelling', ['T59','T60','T61','T62','T63','T64'], 'Record the site, sort materials and assess the dwelling transition with accommodation continuity.'),
        ('C12', 'Modular places tracks and services', ['T65','T66','T67','T68','T69','T70','T86','T87','T88'], 'Test the 20/20/30 structure options and 40/15/10 flexible places against actual access and service needs.'),
        ('C13', 'Kitchen amenities and food growing', ['T71','T72','T73','T74','T75','T76'], 'Connect shared cooking cold storage amenities food forest nursery and Tower Farm through a small first stage.'),
        ('C14', 'Culture making and learning', ['T77','T78','T79','T80','T81','T82'], 'Culturally directed gatherings and supervised making have different spaces permissions and mentors.'),
        ('C15', 'Connected labs and service agreements', ['T83','T84','T85'], 'Treat linked projects as distinct proposals and record each useful interface explicitly.'),
    ]
    for cid, title, ts, note in new_lists:
        checklists.append(dict(id=cid,title=title,tasks=ts,note=note))

    for d in docs:
        d['prompt'] += '\nREFERENCE LINKS:\n' + '\n'.join(r['title']+' - '+r['url'] for r in refs if r['id'] in d['sources']) + '\n'

    theme_rows = [
        ('living','Permanent living and residencies','Permanent residents, medium-term residencies and short stays are all part of the original Noonuccal-led concept.','hero',['D32','D43'],['T56','T57','T58','T89','T90','T91'],'C10','Community living'),
        ('layout','Site areas and clustered layout','About 15 acres described; 13.4 acres traced inside the firebreak; 1.02 km around the measured path. Small clusters retain scrub and room for shared life.','site-reference',['D31'],['T53','T54','T55'],'C09','Site planning'),
        ('cleanup','Clean-up and material sorting','Clean, sort and record the land before choosing what gets repaired reused moved or disposed of.','ground-notes',['D33'],['T59','T60','T61'],'C11','Site preparation'),
        ('dwelling','Existing dwelling transition','Consider shared use of the handmade dwelling after a suitable replacement expandable home is established.','ground-notes',['D34'],['T62','T63','T64'],'C11','Site preparation'),
        ('buildings','Expandable buildings and containers','20 expandable 40-foot, 20 expandable 20-foot and 30 standard 20-foot structure options require individual uses specifications and staged decisions.','capacity',['D35'],['T65','T66','T67'],'C12','Buildings & places'),
        ('places','Flexible visitor places and sandy tracks','40 tent swag or small-van, 15 caravan or larger-rig and 10 bus or house-truck options sit alongside sandy tracks and turning loops.','capacity',['D36'],['T68','T69','T70'],'C12','Buildings & places'),
        ('kitchen','Shared kitchen cold storage and amenities','A shared kitchen cold storage and three amenity blocks connect daily living gatherings and guests.','capacity',['D37'],['T71','T72','T73'],'C13','Shared facilities'),
        ('growing','Food forest orchard nursery and Tower Farm','Food forest bush orchard gardens bush tucker nursery and the Tower Farm and Seedling Hub have distinct growing plans.','capacity',['D38'],['T74','T75','T76'],'C13','Growing & commons'),
        ('culture','Ceremony and cultural grounds','Ceremony yarning teaching and gathering follow relevant Noonuccal direction, with room for restricted and public uses.','layout',['D39','D02'],['T77','T78','T79'],'C14','Culture & gatherings'),
        ('making','Making repair and learning','A suitable 7-Mile work area starts with useful repair tool sharing material sorting and supervised learning.','related-labs',['D40'],['T80','T81','T82'],'C14','Making & learning'),
        ('links','Separate labs and service interfaces','Maker-Space Tip Loop and Capsule Surge offer useful ideas and possible interfaces, each with its own site and operating choices.','related-labs',['D41','D13'],['T83','T84','T85'],'C15','Connected projects'),
        ('commons','Commons water harvesting and services','Commons water harvesting household loads gardens food service and shared facilities need one coordinated service plan.','capacity',['D42'],['T86','T87','T88'],'C12','Growing & commons'),
        ('stages','Stages and operating decisions','Work from cultural direction and on-ground records into a selected stage, with permanent living cultural activities and stays considered separately.','layout',['D19','D29','D30'],['T33','T49','T51'],'C08','Land & approvals'),
    ]
    themes = [dict(id=i,title=t,original=o,anchor=a,documents=ds,tasks=ts,checklist=c,stream=st,source=ORIGINAL+('#'+a if a!='hero' else '')) for i,t,o,a,ds,ts,c,st in theme_rows]
    estimates = [
        ('Site description','About 15 acres','Description, not the measured firebreak area','D31'),
        ('Working firebreak trace','13.4 acres; 1.02 km perimeter','Reference trace, not a surveyed or claim boundary','D31'),
        ('Structure options','20 × 74 m2; 20 × 37 m2; 30 × 15 m2','70 structures, with use and occupancy still to be specified','D35'),
        ('Shared roofs and facilities','About 350 m2; three amenity blocks','Kitchen cold storage and amenities combined allowance','D37'),
        ('Buildings before decks and shade','About 3023 m2 on the original page','Rounded listed components total 3020 m2; retain both until specifications replace them','D35'),
        ('Buildings studios and shared places','About 4700 m2','Broader footprint allowance, separate from roof area','D31'),
        ('Flexible visitor places','40 × 65 m2; 15 × 90 m2; 10 × 125 m2','65 places; component areas sum to 5200 m2, not an occupancy limit','D36'),
        ('Tracks and turning loops','About 3200 m2; around 4 m wide','About 800 m equivalent at that width, not a measured road','D36'),
        ('Ceremony and cultural grounds','About 8000 m2','Cultural direction and gathering needs determine use','D39'),
        ('Food forest and bush orchard','About 18000 m2','Growing concept allowance','D38'),
        ('Gardens and bush tucker nursery','About 6000 m2','Distinct from food forest and tower growing','D38'),
        ('Commons and water harvesting','About 8159 m2','Shared-space allowance; no water yield is implied','D42'),
        ('Tower Farm and Seedling Hub','About 1000 m2 beside the kitchen','Trial scope and utility needs remain to be specified','D38'),
        ('Culture growing and shared-life subtotal','41159 m2','8000 + 18000 + 6000 + 8159 + 1000','D31'),
        ('Whole footprint exercise','54259 m2','4700 + 5200 + 3200 + 41159; 13.4 acres converts to about 54228 m2, a roughly 31 m2 rounding difference','D31'),
    ]
    register = [dict(element=a,original=b,interpretation=c,document=d) for a,b,c,d in estimates]
    for d in docs:
        d['themes'] = [t['id'] for t in themes if d['id'] in t['documents']]
    provenance = dict(reviewed='2026-10-10',original=ORIGINAL,corrections=['Native title claim land context supplied by founder','No water views in site artwork','C-Hours have no financial aspect'],observations=['Original concept includes permanent residents','Ground described as flat dry raised and scrub-covered remains an observation rather than a drainage assessment','Maker-Space location discussion is Dunwich / Goompi','Capsule Surge has no nominated site','Older Tip Loop financial C-Hour language is superseded'])
    return dict(themes=themes,estimates=register,provenance=provenance)

def write_mapping(root, data):
    text = '# Original 7-Mile plan to administration map\n\nReviewed 10 October 2026. Original concept: '+ORIGINAL+'\n\nThe original plan includes permanent community living, medium-term residencies, short stays, ceremony, food growing, making and learning. Founder corrections take precedence over older source language.\n\n## Concept to work\n\n| Original element | Documents | Tasks | Checklist | Source section |\n| --- | --- | --- | --- | --- |\n'
    for t in data['themes']:
        text += '| '+t['title']+' | '+', '.join(t['documents'])+' | '+', '.join(t['tasks'])+' | '+t['checklist']+' | [Original]('+t['source']+') |\n'
    text += '\n## Working quantities\n\n| Element | Original figure | Interpretation | Document |\n| --- | --- | --- | --- |\n'
    for e in data['estimates']:
        text += '| '+e['element']+' | '+e['original']+' | '+e['interpretation']+' | '+e['document']+' |\n'
    text += '\n## Source corrections and interfaces\n\n7-Mile is on a native title claim. Specific claim records, mapped boundaries and existing agreements remain inputs. C-Hours have no financial aspect. Maker-Space, Tip Loop and Capsule Surge remain distinct proposals; no shared location, ownership, clinical service or compute installation is inferred.\n\nThe Tip Loop governance page contains older financial issuance and redemption language. This is excluded from 7-Mile drafting. The Capsule Surge model has no nominated site. The Maker-Space location proposal discusses Dunwich / Goompi.\n\n## Staging\n\nSource reading and needs briefs proceed alongside entity decisions. Site preparation follows actual permissions. Layout and service options inform the chosen first stage. Procurement follows evidence and funding decisions. Only briefs relevant to that stage enter its release pack; later concept works are not blanket prerequisites for a small cultural activity.\n'
    (root/'docs/ORIGINAL-PLAN-MAPPING.md').write_text(text)
    b = io.StringIO(); w = csv.DictWriter(b,fieldnames=['element','original','interpretation','document']); w.writeheader(); w.writerows(data['estimates'])
    (root/'estimates.csv').write_text(b.getvalue())
    (root/'concept-map.json').write_text(json.dumps({k:data[k] for k in ('themes','estimates','provenance')},indent=2)+'\n')
