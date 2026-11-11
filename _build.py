#!/usr/bin/env python3
"""Generate the static site pages for fisherswaterdamage.com
Run:  python3 _build.py   (then ./replace_phone.sh once the tracking number exists)"""
from pathlib import Path
from _sitekit import Site, PHONE_DISP, PHONE_TEL, CALL

ROOT = Path(__file__).resolve().parent

CONFIG = {
    "domain": "fisherswaterdamage.com",
    "brand": "Fishers Water Damage",
    "logo_sub": "Local referral connection",
    "city": "Fishers",
    "state": "Indiana",
    "geo_region": "US-IN",
    "topbar": "Free referral line for Fishers &amp; Hamilton County homeowners",
    "footer_blurb": "A free referral service that helps homeowners in Fishers and nearby Hamilton County communities connect with independent, licensed water damage, basement, mold, fire, and sewage cleanup providers.",
    "schema_areas": ["Noblesville", "Carmel", "McCordsville", "Fortville", "Indianapolis"],
    "law_state": "New Mexico",
    "year": 2026,
    "services": [
        {"file": "flooded-basement-cleanup.html", "name": "Flooded Basement &amp; Sump Pump", "nav": "Flooded Basement &amp; Sump Pump", "icon": "🏚️"},
        {"file": "water-damage-restoration.html", "name": "Water Damage Restoration", "nav": "Water Damage Restoration", "icon": "🌊"},
        {"file": "storm-roof-leak-damage.html", "name": "Storm &amp; Roof Leak Damage", "nav": "Storm &amp; Roof Leaks", "icon": "⛈️"},
        {"file": "burst-frozen-pipes.html", "name": "Burst &amp; Frozen Pipes", "nav": "Burst &amp; Frozen Pipes", "icon": "🧊"},
        {"file": "sewage-backup-cleanup.html", "name": "Sewage Backup Cleanup", "nav": "Sewage Backup Cleanup", "icon": "🚽"},
        {"file": "mold-remediation.html", "name": "Mold Remediation", "nav": "Mold Remediation", "icon": "🦠"},
        {"file": "fire-smoke-damage.html", "name": "Fire &amp; Smoke Damage", "nav": "Fire &amp; Smoke Damage", "icon": "🔥"},
    ],
}

site = Site(CONFIG, ROOT)

# ======================= HOME =======================
home_faqs = [
    ("Are you a water damage company?",
     "No. This is a free referral line. We try to connect you with an independent, licensed provider who handles your type of problem, from a wet basement to sewage, mold, or fire and smoke damage."),
    ("My sump pump failed during a storm. Can I call at night?",
     "Yes, call any time. Many restoration companies run emergency crews after hours, and we will try to reach one that serves your address. We cannot guarantee a provider is available at every hour."),
    ("Which areas do you cover?",
     "Fishers (ZIP codes 46037, 46038, and the Fishers part of 46040) plus nearby Noblesville, Carmel, McCordsville, Fortville, Ingalls, and the northeast side of Indianapolis. Coverage depends on which providers are available when you call."),
    ("What kinds of problems can I call about?",
     "Flooded or wet basements, sump pump failures, storm and roof leaks, burst or frozen pipes, sewage backups through floor drains, mold after water damage, and fire or smoke damage."),
    ("Does it cost anything to call?",
     "No. There is no charge to call. Any inspection or repair costs are between you and the independent provider you decide to hire."),
    ("Will my insurance cover a wet basement?",
     "It depends on your policy and the cause. Many standard policies only cover sump pump or drain backup if you added that coverage, and outside flooding usually needs separate flood insurance. Check with your agent."),
]

svc_cards = [
    ("🏚️", "Flooded Basement &amp; Sump Pump", "Sump pump quit, window well filled, or water seeping in after heavy rain.", "flooded-basement-cleanup.html"),
    ("🌊", "Water Damage Restoration", "Water heater, washer hose, or supply line failures that soaked floors and walls.", "water-damage-restoration.html"),
    ("⛈️", "Storm &amp; Roof Leak Damage", "Wind-damaged shingles, fallen limbs, and storm water through the ceiling.", "storm-roof-leak-damage.html"),
    ("🧊", "Burst &amp; Frozen Pipes", "Indiana cold snaps can split pipes in exterior walls, garages, and crawl spaces.", "burst-frozen-pipes.html"),
    ("🚽", "Sewage Backup Cleanup", "Floor drain or ejector pit backups in the basement need careful cleanup.", "sewage-backup-cleanup.html"),
    ("🦠", "Mold Remediation", "Musty finished basement or growth behind drywall after a leak.", "mold-remediation.html"),
    ("🔥", "Fire &amp; Smoke Damage", "Soot, smoke odor, and the water left behind after a fire is put out.", "fire-smoke-damage.html"),
]
cards_html = "\n".join(f'''          <article class="card">
            <div class="icon" aria-hidden="true">{i}</div>
            <h3>{t}</h3>
            <p>{d}</p>
            <a class="more" href="{h}">Learn more →</a>
          </article>''' for i, t, d, h in svc_cards)

home_schema_site = {
    "@context": "https://schema.org", "@type": "WebSite",
    "name": CONFIG["brand"], "url": site.url(),
    "description": "Free referral service connecting Fishers, Indiana homeowners with independent water damage, flooded basement, sewage, mold, and fire restoration providers.",
}
home_schema_org = {
    "@context": "https://schema.org",
    **site.org(),
    "areaServed": site.area_served(),
    "knowsAbout": ["Flooded basement cleanup", "Sump pump failure water damage", "Water damage restoration",
                   "Storm and roof leak water damage", "Frozen pipe water damage", "Sewage backup cleanup",
                   "Mold remediation", "Fire and smoke damage restoration"],
    "hasOfferCatalog": {
        "@type": "OfferCatalog", "name": "Referral services",
        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"].replace("&amp;", "&"), "url": site.url(s["file"])}} for s in CONFIG["services"]],
    },
}

home = (site.head("Fishers Water Damage & Flooded Basement Help | Call Any Time",
                  "Flooded basement, sump pump failure, burst pipe, sewage, mold, or fire damage in Fishers, IN? Call free to reach independent local restoration pros.",
                  "", [home_schema_site, home_schema_org, site.faq_schema(home_faqs)])
        + site.header("index.html")
        + f'''  <main>
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <div class="hero-badge">Fishers · Geist · Noblesville · Carmel · McCordsville</div>
          <h1>Water in your Fishers basement? Get connected to local help.</h1>
          <p class="lead">Sump pump quit in a storm, a pipe split in the cold, or sewage came up the floor drain? We are a free referral line that connects you with an independent, licensed restoration provider in Hamilton County.</p>
          <div class="hero-actions">
            <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">📞 Call {PHONE_DISP}</a>
            <a class="btn btn-secondary btn-lg" href="#services">See what we cover</a>
          </div>
          <p class="hero-note">No charge to call, day or night. Which providers can respond depends on the hour and your location. We do not perform restoration work ourselves.</p>
        </div>
        <aside class="hero-card" aria-label="Common reasons to call">
          <h2>Why Fishers homeowners call</h2>
          <ul>
            <li>Sump pump failed and the finished basement is wet</li>
            <li>Power went out in a thunderstorm and water came in</li>
            <li>Sewage or dirty water up through the floor drain</li>
            <li>Pipe burst during a cold snap</li>
            <li>Storm damage and a leaking ceiling</li>
            <li>Musty basement smell or visible mold</li>
          </ul>
        </aside>
      </div>
    </section>

    <section class="emergency-band" aria-label="Emergency help">
      <div class="container emergency-inner">
        <div>
          <h2>Basement filling up right now? Call any time, day or night.</h2>
          <p>Stay out of standing water if outlets, cords, or the furnace are close to it. If you can do it safely, check whether the sump pump has power. Then call. Many restoration companies run 24/7 emergency crews, and we will try to connect you with one.</p>
        </div>
        <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">🚨 Emergency: {PHONE_DISP}</a>
      </div>
    </section>

    <section class="section section-alt" id="services">
      <div class="container">
        <div class="section-head">
          <h2>What we can refer you for</h2>
          <p>One number for basement, water, sewage, mold, and fire damage in and around Fishers.</p>
        </div>
        <div class="card-grid card-grid-3">
{cards_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2>How it works</h2>
          <p>No forms. No obligation.</p>
        </div>
        <div class="steps">
          <div class="step">
            <h3>Call and describe it</h3>
            <p>Where the water is, where it came from, and your neighborhood or ZIP code.</p>
          </div>
          <div class="step">
            <h3>Get connected</h3>
            <p>We try to put you through to an independent provider who handles that type of damage in Hamilton County.</p>
          </div>
          <div class="step">
            <h3>Make your own call</h3>
            <p>Ask about pumping, drying, cleanup, and insurance documentation. Whether to hire them is your decision.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2>Why basements around Fishers take on water</h2>
          <p>It is not just bad luck. The ground here holds water.</p>
        </div>
        <div class="card-grid card-grid-3">
          <div class="card">
            <h3>Clay soil and high groundwater</h3>
            <p>Hamilton County sits on dense glacial clay. Neighboring Carmel’s engineering department notes that most local soils drain very poorly and have seasonal high water tables, so basements commonly flood when the ground is saturated.</p>
          </div>
          <div class="card">
            <h3>Sump pumps do the heavy lifting</h3>
            <p>Many Fishers basements depend on a sump pump to move groundwater away. When the pump wears out, the float sticks, or the power goes out, water rises fast.</p>
          </div>
          <div class="card">
            <h3>Spring and summer storms</h3>
            <p>Central Indiana thunderstorms can bring heavy rain and wind at the same time, often knocking out power right when a sump pump is needed most.</p>
          </div>
          <div class="card">
            <h3>Finished basements</h3>
            <p>Carpet, drywall, and a basement bedroom or office turn a little water into a big cleanup, and they can hide moisture until it smells musty.</p>
          </div>
          <div class="card">
            <h3>Rivers and the reservoir</h3>
            <p>The White River forms Fishers’ western edge and Geist Reservoir borders the east side, with Fall Creek feeding it. Homes near the water can check flood zones on FEMA’s map service.</p>
          </div>
          <div class="card">
            <h3>Freeze and thaw</h3>
            <p>Indiana winters bring hard freezes. Pipes in exterior walls, garages, and crawl spaces can split, and the leak often shows up when it warms back up.</p>
          </div>
        </div>
        <p class="source-note">Sources: Hamilton County Soil &amp; Water Conservation District, “Building With the Land”; City of Carmel engineering FAQ on basement flooding; City of Fishers mapping.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2>Areas we focus on</h2>
          <p>Fishers and nearby Hamilton, Hancock, and Marion County communities.</p>
        </div>
        <ul class="area-list">
          <li>Fishers</li>
          <li>Geist</li>
          <li>Saxony</li>
          <li>Britton Falls</li>
          <li>Brooks Landing</li>
          <li>Noblesville</li>
          <li>Carmel</li>
          <li>McCordsville</li>
          <li>Fortville</li>
          <li>Northeast Indianapolis</li>
        </ul>
        <p><a href="service-areas.html">Full service area details →</a></p>
      </div>
    </section>

    <section class="section section-alt" id="faq">
      <div class="container">
        <div class="section-head">
          <h2>Frequently asked questions</h2>
        </div>
        <div class="faq">
{site.faq_html(home_faqs)}
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Get the water out and the drying started</h2>
        <p>Call the free Fishers referral line. We will try to connect you with an independent local provider.</p>
        <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
      </div>
    </section>
  </main>
'''
        + site.footer())
site.raw_page("index.html", home, "monthly", "1.0")

# ======================= SERVICE PAGES =======================
site.service_page({
    "file": "flooded-basement-cleanup.html",
    "title": "Flooded Basement & Sump Pump Failure Cleanup | Fishers, IN",
    "meta": "Sump pump failure or flooded basement in Fishers, IN? Call free to connect with independent providers who pump out water and dry finished basements.",
    "crumb": "Flooded Basement &amp; Sump Pump",
    "h1": "Flooded Basement &amp; Sump Pump Failure Cleanup in Fishers",
    "lead": "In a home with a basement, that is where the water ends up. We connect you with independent providers who remove the water, pull wet carpet and drywall, and dry the space before mold sets in.",
    "schema_name": "Flooded Basement and Sump Pump Failure Cleanup Referral",
    "service_type": "Flooded basement water removal and cleanup",
    "schema_desc": "Free referral for flooded basement and sump pump failure cleanup in Fishers, Indiana.",
    "side_h": "Water in the basement?",
    "side_p": "Keep away from wet outlets and the furnace. Call us.",
    "prio": "0.9",
    "body": '''          <p>Central Indiana ground is mostly dense clay left behind by glaciers. It soaks up spring rain and holds it, and the water table rises. The City of Carmel, right across the White River, puts it plainly in its engineering FAQ: most local soils drain very poorly, have seasonal high water tables, and it is common for basements to flood when the soil is saturated. Fishers basements face the same ground.</p>

          <h2>How Fishers basements usually flood</h2>
          <ul>
            <li><strong>The sump pump fails.</strong> Pumps wear out, floats stick, and check valves fail. A pump that has run for years without attention can quit on the wettest night of the year.</li>
            <li><strong>The power goes out.</strong> A strong thunderstorm can cut power just as the pit fills. Without a battery backup, the pump stops.</li>
            <li><strong>The pump can’t keep up.</strong> In long, heavy rain, a small pump or a frozen or clogged discharge line can be overwhelmed.</li>
            <li><strong>Window wells fill up</strong> with rain or debris and leak through the window.</li>
            <li><strong>Seepage</strong> through cracks in the wall or the joint where the wall meets the floor.</li>
            <li><strong>Inside sources:</strong> a water heater, water softener, or washer in the basement. See <a href="water-damage-restoration.html">water damage restoration</a>.</li>
            <li><strong>Floor drain or ejector pit backups.</strong> That water should be treated as sewage; see <a href="sewage-backup-cleanup.html">sewage backup cleanup</a>.</li>
          </ul>

          <h2>Safety first</h2>
          <p>Do not step into standing water if outlets, cords, the furnace, or the electrical panel are wet or close to it. If you cannot reach the breaker without stepping in water, wait for a professional or call your electric utility. Have gas appliances that were under water checked before you use them again.</p>

          <h2>What the cleanup usually looks like</h2>
          <ol>
            <li>Pump out standing water and extract the carpet.</li>
            <li>Remove wet carpet pad, which rarely dries well in place.</li>
            <li>Cut out the bottom of wet drywall (often called a “flood cut”) and pull wet insulation.</li>
            <li>Dry the slab, framing, and remaining materials with dehumidifiers and air movers, checking moisture daily.</li>
            <li>Look at the sump pit, pump, and discharge line, and point you to a plumber or waterproofing company if they need work.</li>
          </ol>

          <h2>Sump pump tips from Hamilton County</h2>
          <p>The Hamilton County Soil and Water Conservation District recommends a battery backup and an alarm for sump pumps that sit inside a basement, and check valves to keep water from flowing back during heavy rain. It also says sump pumps should carry only groundwater and storm water to a storm drain, while floor drains and other sewage need a separate ejector pump tied to the sanitary sewer. The county surveyor’s office notes that most newer subdivisions provide a sump outlet for each lot.</p>
          <ul>
            <li>Test the pump every few months by pouring water into the pit.</li>
            <li>Add a battery backup or a water-powered backup pump.</li>
            <li>Install a high-water alarm so you hear about trouble early.</li>
            <li>Keep the discharge line clear and free of ice in winter.</li>
          </ul>

          <h2>Get a referral</h2>
          <p>Call {CALL}. Tell us how deep the water is, whether the basement is finished, and whether it could be from a drain backup. We will try to connect you with an independent provider who serves your part of Fishers.</p>
          <p class="source-note">Sources: City of Carmel engineering FAQ; Hamilton County SWCD “Building With the Land”; Hamilton County Surveyor FAQ.</p>
''',
    "faqs": [
        ("Is a sump pump failure covered by insurance?",
         "Often only if your policy has a water backup or sump overflow endorsement. Standard policies typically exclude it, and outside flooding usually needs separate flood insurance. Check with your agent."),
        ("How long does it take to dry a basement?",
         "It depends on how much water there was and what got wet. Providers measure moisture each day and remove equipment once materials are back to normal readings."),
    ],
})

site.service_page({
    "file": "water-damage-restoration.html",
    "title": "Water Damage Restoration Referral | Fishers, IN",
    "meta": "Water heater, washer, or supply line leak in your Fishers home? Call free to reach independent water damage restoration providers in Hamilton County.",
    "crumb": "Water Damage Restoration",
    "h1": "Water Damage Restoration in Fishers",
    "lead": "When an appliance or plumbing line lets go, the water heads for the lowest point, which in most Fishers homes is the basement. Our free line connects you with independent providers who extract the water and dry the structure.",
    "schema_name": "Water Damage Restoration Referral",
    "service_type": "Water damage restoration",
    "schema_desc": "Free referral connecting Fishers, Indiana homeowners with independent water damage restoration providers.",
    "prio": "0.9",
    "body": '''          <p>Fishers grew quickly over the past few decades, and many homes from that growth now have original water heaters, washing machine hoses, toilet supply lines, and dishwashers reaching the end of their life. A second-floor laundry room is convenient until a hose bursts and the water comes through the kitchen ceiling below.</p>

          <h2>Common sources of indoor water damage</h2>
          <ul>
            <li>Water heaters leaking or failing, often in the basement or a utility closet</li>
            <li>Washing machine hoses, especially in upstairs laundry rooms</li>
            <li>Refrigerator ice maker lines and dishwasher connections</li>
            <li>Toilet supply lines and wax ring leaks</li>
            <li>Water softener and filter connections</li>
            <li>Shower pans and tub surrounds leaking into the ceiling below</li>
          </ul>

          <h2>What restoration usually involves</h2>
          <p>Independent restoration providers typically confirm the source is stopped, then use moisture meters and often thermal cameras to find where the water went. Standing water is extracted, materials that can’t be saved (swollen cabinet bases, wet pad, soaked drywall) are removed, and drying equipment runs until readings return to normal. Most also keep photos and moisture logs, which insurers commonly ask for.</p>

          <h2>Water travels down and sideways</h2>
          <p>In a two-story home with a basement, one leak can affect three levels: the room where it started, the ceiling below, and the basement under that. Water also wicks sideways through drywall and under flooring. That is why a provider may want to check rooms that look fine.</p>

          <h2>What to do right now</h2>
          <ol>
            <li>Turn off the water at the fixture or the main shutoff, usually in the basement near the water meter or where the line enters the house.</li>
            <li>Turn off power to wet areas if you can reach the panel safely.</li>
            <li>Move rugs, furniture, and electronics off wet floors.</li>
            <li>Take photos and video before cleanup starts.</li>
            <li>Call {CALL} to be connected with a local restoration provider.</li>
          </ol>
          <p>If the water came from a frozen pipe, see <a href="burst-frozen-pipes.html">burst and frozen pipes</a>. If it ended up in the basement, see <a href="flooded-basement-cleanup.html">flooded basement cleanup</a>.</p>
''',
    "faqs": [
        ("Can I dry it myself with fans?",
         "Fans move surface moisture but often miss water trapped in walls, pad, and subfloors. Professional moisture readings show whether materials are actually dry."),
        ("Who fixes the leak itself?",
         "Usually a licensed plumber or appliance technician. The restoration provider handles the water damage. Ask who does what so nothing falls through the cracks."),
    ],
})

site.service_page({
    "file": "storm-roof-leak-damage.html",
    "title": "Storm & Roof Leak Water Damage Help | Fishers, IN",
    "meta": "Storm damage, fallen limbs, or a roof leak letting water into your Fishers home? Call free to connect with independent storm water damage providers.",
    "crumb": "Storm &amp; Roof Leak Damage",
    "h1": "Storm &amp; Roof Leak Water Damage",
    "lead": "Indiana storms bring wind, heavy rain, and sometimes hail, often all at once. When that water gets inside, we can connect you with an independent provider who handles the ceilings, walls, and floors.",
    "schema_name": "Storm and Roof Leak Water Damage Referral",
    "service_type": "Storm and roof leak water damage restoration",
    "schema_desc": "Free referral for storm and roof leak water damage help in Fishers, Indiana.",
    "side_h": "Ceiling dripping?",
    "side_p": "Catch the water, cut power to leaking fixtures, then call.",
    "body": '''          <p>Spring and summer thunderstorms are part of life in central Indiana. Strong straight-line winds can lift shingles and snap branches onto roofs, and the heavy rain that follows finds every gap. Many neighborhoods in Fishers, especially older ones and those near Geist and the White River, have large mature trees close to the house.</p>

          <h2>How storm water usually gets in</h2>
          <ul>
            <li>Wind-lifted or missing shingles, and damaged flashing around chimneys and vents</li>
            <li>Tree limbs puncturing the roof or knocking gutters loose</li>
            <li>Hail cracking shingles or skylights</li>
            <li>Gutters clogged with leaves and seed pods overflowing behind the fascia</li>
            <li>Wind-driven rain past window and door seals</li>
            <li>Downspouts dumping next to the foundation, which can show up later as <a href="flooded-basement-cleanup.html">basement water</a></li>
          </ul>

          <h2>Ice dams in winter</h2>
          <p>When snow melts on a warm roof and refreezes at the cold edge, it can form an ice dam that backs water up under the shingles. The leak often shows up as a stain along an exterior wall or ceiling in the middle of winter, with no rain in sight.</p>

          <h2>Two jobs: outside and inside</h2>
          <p>A roofer repairs the roof and may tarp it in the meantime. A restoration provider deals with what already got in: wet attic insulation, ceiling drywall, framing, and anything below. If a tree is on the house, you may also need a tree service before anyone can work safely.</p>

          <h2>After the storm</h2>
          <ol>
            <li>Keep people out from under any ceiling that is sagging with water.</li>
            <li>Turn off power to leaking light fixtures and fans.</li>
            <li>Photograph outside damage (shingles in the yard, dented gutters, fallen limbs) and inside damage.</li>
            <li>Be cautious with door-to-door contractors after big storms, and check out any company before you sign.</li>
            <li>Call {CALL} to be connected with a provider for the inside water damage.</li>
          </ol>
          <p>Related: <a href="water-damage-restoration.html">water damage restoration</a>, and <a href="mold-remediation.html">mold remediation</a> if the attic or ceiling stayed wet for a while.</p>
''',
    "faqs": [
        ("Do you repair roofs?",
         "No. We are a referral service for the water damage inside the home. You will need a roofer for the roof itself."),
        ("Should I wait for the adjuster before drying?",
         "Insurers generally expect you to take reasonable steps to prevent more damage. Take photos, then start drying. Check your own policy for details."),
    ],
})

site.service_page({
    "file": "burst-frozen-pipes.html",
    "title": "Burst & Frozen Pipe Water Damage | Fishers, IN Referral",
    "meta": "Frozen or burst pipe in your Fishers home? Get a free referral to independent providers who dry walls, ceilings, and basements after a pipe break.",
    "crumb": "Burst &amp; Frozen Pipes",
    "h1": "Burst &amp; Frozen Pipe Water Damage",
    "lead": "A pipe that froze overnight can split and start leaking the moment it thaws. We connect Fishers homeowners with independent providers who handle the water damage after a break.",
    "schema_name": "Burst and Frozen Pipe Water Damage Referral",
    "service_type": "Frozen and burst pipe water damage restoration",
    "schema_desc": "Free referral for burst and frozen pipe water damage help in Fishers, Indiana.",
    "side_h": "Pipe burst?",
    "side_p": "Shut off the main valve, then call.",
    "body": '''          <p>Indiana winters regularly bring stretches of single-digit temperatures and wind chills below zero. Pipes inside heated living space usually handle it. The trouble spots are the ones near the cold: exterior walls, garages, crawl spaces, and the rim joist in the basement.</p>

          <h2>Where pipes tend to freeze in Fishers homes</h2>
          <ul>
            <li>Kitchen and bathroom sinks on outside walls, especially behind closed cabinets</li>
            <li>Lines running through an attached garage or over a garage ceiling</li>
            <li>Outdoor faucets with a hose left attached</li>
            <li>Lawn irrigation backflow devices that weren’t winterized</li>
            <li>Crawl spaces and basement rim joists where cold air leaks in</li>
            <li>Homes where the heat was turned way down during travel</li>
          </ul>

          <h2>The leak often starts when it warms up</h2>
          <p>Ice inside a cracked pipe can act like a plug. When the temperature climbs, the ice melts and water starts pouring out, sometimes inside a wall or ceiling where you won’t see it right away. Low water pressure during a freeze, a hissing sound, or a new stain are all reasons to shut off the main and look closer.</p>

          <h2>What to do</h2>
          <ol>
            <li>Close the main shutoff, typically in the basement near the meter.</li>
            <li>Open a faucet on the lowest level to drain pressure.</li>
            <li>Stay away from water near outlets, ceiling lights, and the panel.</li>
            <li>Photograph the damage and the pipe if you can see it.</li>
            <li>Call a plumber for the repair and {CALL} for a referral to a water damage provider.</li>
          </ol>

          <h2>What drying usually involves</h2>
          <p>Burst pipes often soak hidden spaces. Providers commonly open small sections of drywall so wall cavities can dry, extract water from carpet and the basement, and run dehumidifiers with daily readings. A leak upstairs can reach the basement, so expect them to check below the break too.</p>

          <h2>Before the next cold snap</h2>
          <ul>
            <li>Disconnect hoses and winterize irrigation before the first hard freeze.</li>
            <li>Open sink cabinets on outside walls on the coldest nights.</li>
            <li>Let a faucet drip when temperatures drop well below freezing.</li>
            <li>Keep the heat on (many people use 55°F or higher) when you travel.</li>
            <li>Seal gaps near pipes in the garage and basement rim joist.</li>
          </ul>
          <p>Related: <a href="flooded-basement-cleanup.html">flooded basement cleanup</a> and <a href="mold-remediation.html">mold remediation</a>.</p>
''',
    "faqs": [
        ("Is frozen pipe damage covered?",
         "Policies differ. Sudden bursts are often handled differently from slow leaks or damage in a home left without heat. Ask your insurer about your specific policy."),
        ("Can I thaw a frozen pipe myself?",
         "If you can reach it safely and there is no standing water, gentle heat like a hair dryer is common. Never use an open flame. Call a plumber if you aren’t sure."),
    ],
})

site.service_page({
    "file": "sewage-backup-cleanup.html",
    "title": "Sewage Backup Cleanup Referral | Fishers, IN",
    "meta": "Sewage coming up a basement floor drain or toilet in Fishers? Call free to connect with independent sewage cleanup and sanitizing providers.",
    "crumb": "Sewage Backup Cleanup",
    "h1": "Sewage Backup Cleanup in Fishers",
    "lead": "Dirty water coming up through the basement floor drain is a health hazard, not just a mess. We connect Fishers homeowners with independent providers equipped to remove it and sanitize the area.",
    "schema_name": "Sewage Backup Cleanup Referral",
    "service_type": "Sewage backup cleanup and sanitization",
    "schema_desc": "Free referral for sewage backup cleanup in Fishers, Indiana.",
    "side_h": "Sewage in the basement?",
    "side_p": "Stop using water, keep everyone away, and call.",
    "body": '''          <p>In a home with a basement, sewage backups almost always show up at the lowest opening: the basement floor drain, a basement bathroom, or the pit for a sewage ejector pump. Unlike clean water from a broken supply line, this water carries bacteria and other contaminants, and porous materials it touched are usually removed rather than cleaned.</p>

          <h2>Sump pit or sewage pit?</h2>
          <p>Many Fishers basements have two pits. The <strong>sump pit</strong> collects groundwater and sends it outside or to a storm drain. A <strong>sewage ejector pit</strong>, usually sealed with a bolted lid, lifts waste from a basement bathroom or laundry up to the sewer line. The Hamilton County Soil and Water Conservation District notes that these should stay separate. If the sealed pit overflowed or the water smells like sewage, treat it as a sewage backup.</p>

          <h2>Common causes</h2>
          <ul>
            <li>A failed sewage ejector pump or a stuck float</li>
            <li>Tree roots or debris in the sewer lateral</li>
            <li>Wipes, grease, and other items that don’t break down</li>
            <li>A broken or sagging section of line</li>
            <li>Heavy rain overloading the sewer system</li>
          </ul>

          <h2>What to do now</h2>
          <ol>
            <li>Stop using water in the house: no flushing, showers, laundry, or dishwasher.</li>
            <li>Keep kids, pets, and anyone with health concerns away.</li>
            <li>Wear gloves and boots if you must go near it, and wash well afterward.</li>
            <li>Turn off power to the area only if you can do it without stepping in water.</li>
            <li>Call a plumber to clear the line, and call {CALL} for a referral to a cleanup provider.</li>
          </ol>

          <h2>What professional cleanup involves</h2>
          <p>Providers typically wear protective gear, extract the contaminated water, remove affected carpet, pad, drywall, and insulation, clean and disinfect hard surfaces, and dry the area. Many also run air scrubbers for odor. Because the water is contaminated, more material usually has to go than with a clean-water leak.</p>

          <h2>Who handles the line?</h2>
          <p>In general, the homeowner is responsible for the line from the house to the public main, and the city or utility handles the main. If you think the problem is in the main, call the sewer utility listed on your bill. A plumber’s camera inspection can show where the blockage is.</p>

          <h2>Preventing it</h2>
          <ul>
            <li>Ask a plumber about a backwater valve.</li>
            <li>Service the ejector pump and test its alarm.</li>
            <li>Keep wipes and grease out of drains.</li>
            <li>Check your policy for sewer and drain backup coverage.</li>
          </ul>
          <p>Related: <a href="flooded-basement-cleanup.html">flooded basement cleanup</a> and <a href="mold-remediation.html">mold remediation</a>.</p>
''',
    "faqs": [
        ("Can carpet be saved after a sewage backup?",
         "Usually not. Carpet and pad that soaked up sewage are generally removed because they are hard to fully clean."),
        ("Is it safe to stay in the house?",
         "That depends on how much there is and where. Keep away from the affected area, especially young children and anyone with health issues, and ask the provider about your situation."),
    ],
})

site.service_page({
    "file": "mold-remediation.html",
    "title": "Mold Remediation Referral | Fishers, IN",
    "meta": "Musty basement or visible mold after a leak in your Fishers home? Call free to connect with independent mold remediation providers in Hamilton County.",
    "crumb": "Mold Remediation",
    "h1": "Mold Remediation After Water Damage",
    "lead": "Indiana’s humid summers and damp basements give mold plenty of chances. If you smell mustiness or see growth after water damage, we can connect you with an independent mold remediation provider.",
    "schema_name": "Mold Remediation Referral",
    "service_type": "Mold remediation",
    "schema_desc": "Free referral connecting callers with independent mold remediation providers in Fishers, Indiana.",
    "body": '''          <p>Mold needs moisture, something to grow on, and a little time. A finished basement offers all three: concrete that wicks ground moisture, carpet and drywall to feed on, and summer humidity that keeps things damp. Add a sump pump failure or a slow leak, and growth can start behind the drywall before anyone notices.</p>

          <h2>Where mold commonly shows up</h2>
          <ul>
            <li>Finished basements after a flood or seepage, especially behind drywall and under carpet</li>
            <li>Basement storage rooms and closets with poor air movement</li>
            <li>Bathrooms without a working exhaust fan</li>
            <li>Attics after a roof leak or with poor ventilation</li>
            <li>Under kitchen and bathroom sinks with a slow drip</li>
          </ul>

          <h2>What remediation generally involves</h2>
          <p>Independent providers usually begin with the moisture source, because mold comes back if the water does. Depending on the size of the area, they may set up containment and air filtration, remove affected porous materials like drywall, insulation, and carpet, clean and treat framing and hard surfaces, and dry everything before walls go back up. Some homeowners choose independent testing before or after the work.</p>

          <h2>Questions worth asking</h2>
          <ul>
            <li>What is the moisture source, and is it fixed?</li>
            <li>How will you contain the work area?</li>
            <li>What will be removed versus cleaned?</li>
            <li>What training or certifications does your crew have (for example, IICRC)?</li>
            <li>How will you confirm the area is dry before rebuilding?</li>
          </ul>

          <h2>Keep the basement dry</h2>
          <ul>
            <li>Run a dehumidifier in the basement during humid months.</li>
            <li>Keep the sump pump tested and backed up.</li>
            <li>Point downspouts well away from the foundation.</li>
            <li>Don’t store cardboard boxes directly on the basement floor.</li>
            <li>Dry any spill or seep within a day or two.</li>
          </ul>

          <h2>What we will not claim</h2>
          <p>We do not diagnose health conditions, guarantee a “mold-free” home, or interpret lab results. Talk to a medical professional about health concerns. We connect you with a provider who can assess the home.</p>

          <p>Mold usually follows water. If you still have an active problem, see <a href="flooded-basement-cleanup.html">flooded basement cleanup</a>, <a href="water-damage-restoration.html">water damage restoration</a>, or <a href="storm-roof-leak-damage.html">storm and roof leaks</a>. For a referral, call {CALL}.</p>
''',
    "faqs": [
        ("When should I call a professional?",
         "U.S. EPA guidance suggests professional help for areas larger than about 10 square feet, for mold in HVAC systems, or for mold tied to sewage or contaminated water."),
        ("Will a dehumidifier get rid of mold?",
         "A dehumidifier helps prevent mold by lowering humidity, but it won’t remove existing growth. Affected materials still need to be cleaned or removed."),
    ],
})

site.service_page({
    "file": "fire-smoke-damage.html",
    "title": "Fire & Smoke Damage Restoration Referral | Fishers, IN",
    "meta": "Kitchen fire, soot, smoke odor, or water damage from firefighting in Fishers? Call free to connect with independent fire and smoke restoration providers.",
    "crumb": "Fire &amp; Smoke Damage",
    "h1": "Fire &amp; Smoke Damage Restoration",
    "lead": "Fire damage rarely stops where the flames did. Smoke, soot, and water from firefighting spread through the house. We connect Fishers homeowners with independent providers who clean, deodorize, and dry after a fire.",
    "schema_name": "Fire and Smoke Damage Restoration Referral",
    "service_type": "Fire and smoke damage restoration",
    "schema_desc": "Free referral for fire, smoke, and soot damage restoration in Fishers, Indiana.",
    "side_h": "Had a fire?",
    "side_p": "Once the fire department clears the home, call.",
    "body": '''          <p><strong>If anything is still burning, call 911.</strong> This page is about the recovery after the fire is out and the fire department says it is safe to go back in.</p>

          <p>Common household fires start in the kitchen, at the dryer vent, from space heaters in winter, or from electrical problems. Even a small one can push soot through the ductwork into every room. A bigger fire usually brings a lot of water from hoses, and in a home with a basement, that water drains straight down. See <a href="water-damage-restoration.html">water damage restoration</a> and <a href="flooded-basement-cleanup.html">flooded basement cleanup</a>.</p>

          <h2>What fire restoration typically covers</h2>
          <ul>
            <li>Emergency board-up of windows and doors and tarping roof openings</li>
            <li>Extracting firefighting water and drying the structure</li>
            <li>Cleaning soot from walls, ceilings, cabinets, and belongings</li>
            <li>Odor treatment with air scrubbers and other deodorizing methods</li>
            <li>HVAC filter changes and duct cleaning when needed</li>
            <li>Packing out and inventorying contents for cleaning or claims</li>
          </ul>

          <h2>Smoke without flames</h2>
          <p>Smoke can come in from outside too. In the summer of 2023, smoke from Canadian wildfires drifted over Indiana and led to air quality alerts across the state. Most outdoor smoke clears on its own, but a nearby house or garage fire can leave odor and fine soot inside your home that needs cleaning.</p>

          <h2>Do’s and don’ts</h2>
          <ul>
            <li><strong>Do</strong> wait for the fire department’s all-clear before going in.</li>
            <li><strong>Do</strong> photograph everything before cleaning.</li>
            <li><strong>Do</strong> call your insurer early; fire claims usually involve an adjuster.</li>
            <li><strong>Don’t</strong> wipe soot with a wet cloth; it can smear and set.</li>
            <li><strong>Don’t</strong> run the furnace or AC until filters and ducts are checked.</li>
            <li><strong>Don’t</strong> use food, drinks, or medicine that were exposed to heat or smoke.</li>
          </ul>

          <h2>Get a referral</h2>
          <p>Call {CALL}. Tell us what burned, how much of the house has smoke or soot, and whether water was used. We will try to connect you with an independent fire restoration provider. Ask about drying too, since wet materials left behind can lead to <a href="mold-remediation.html">mold</a>.</p>
''',
    "faqs": [
        ("Can smoke smell really be removed?",
         "Often, yes. It usually takes cleaning soot from surfaces plus deodorizing equipment. Some heavily affected materials may need to be replaced."),
        ("Why do I have water damage from a fire?",
         "Hoses and sprinklers put out the fire with a lot of water. That water needs to be removed and dried quickly, just like any other leak."),
    ],
})

# ======================= SERVICE AREAS =======================
areas_inner = '''          <p>When you call, give us your neighborhood, a cross street, or your ZIP code. We use that to try to connect you with an independent provider who works in your area.</p>

          <h2>Fishers</h2>
          <p>Fishers is our main focus, including ZIP codes <strong>46037</strong>, <strong>46038</strong>, and the part of <strong>46040</strong> inside the city. It stretches from the White River on the west to Geist Reservoir on the east. A cross street is all we need.</p>
          <ul class="area-list">
            <li>Geist</li>
            <li>Saxony</li>
            <li>Britton Falls</li>
            <li>Brooks Landing</li>
            <li>Sunblest</li>
            <li>Avalon of Fishers</li>
            <li>River Place</li>
            <li>Fall Creek Place</li>
            <li>Windermere</li>
            <li>Nickel Plate District</li>
            <li>Fishers District (116th &amp; I-69)</li>
          </ul>

          <h2>Nearby communities</h2>
          <ul class="area-list">
            <li>Noblesville</li>
            <li>Carmel</li>
            <li>McCordsville</li>
            <li>Fortville</li>
            <li>Ingalls</li>
            <li>Lawrence</li>
            <li>Castleton area</li>
            <li>Northeast Indianapolis</li>
          </ul>

          <h2>Near the water</h2>
          <p>Homes along the White River on the west side, along Fall Creek, and around Geist Reservoir on the east side can look up their flood zone on FEMA’s Flood Map Service Center or through the City of Fishers GIS maps. Standard homeowners policies typically do not cover outside flooding; that usually takes separate flood insurance.</p>

          <h2>What “service area” means for a referral line</h2>
          <p>We don’t run trucks. The independent provider you talk with sets their own travel area, schedule, and pricing. If one provider can’t take your job, ask about other options on the call.</p>

          <h2>Outside these areas?</h2>
          <p>You’re still welcome to call from elsewhere in the Indianapolis area. We’ll tell you honestly if we can’t connect you with someone nearby.</p>

          <div class="notice">
            <strong>Note:</strong> Listing an area here doesn’t guarantee a provider is available the moment you call. Availability depends on the independent companies participating at that time.
          </div>'''
site.simple_page("service-areas.html", "Service Areas | Fishers Water Damage Referral",
                 "Free water damage referral for Fishers (46037, 46038), Geist, Saxony, Noblesville, Carmel, McCordsville, Fortville, and northeast Indianapolis.",
                 "Service Areas", "Service Areas",
                 "Our free referral line focuses on Fishers and nearby Hamilton County, Hancock County, and northeast Indianapolis communities. Provider availability can vary by day and location.",
                 areas_inner, prio="0.7", freq="monthly", with_side=True,
                 side_h="Call for your area", side_p="Fishers &amp; nearby communities")

# ======================= ABOUT =======================
about_inner = '''        <h2>What this site is</h2>
        <p>Fishers Water Damage is a <strong>free referral / connection service</strong>. We are not a restoration contractor, waterproofing company, mold remediator, fire restoration company, plumber, roofer, or insurance agency. We do not send crews, file claims for you, or do cleanup work.</p>
        <p>When you call {CALL}, your call may be connected or forwarded to an independent, licensed service provider who works in or near your area. That provider is a separate business, and any agreement you make is between you and them.</p>

        <h2>Why we built it</h2>
        <p>When the sump pump quits at 2 a.m. and the basement carpet is squishing, nobody wants to sort through pages of ads and national call centers. We wanted one plain number Fishers homeowners could call about basement water, leaks, sewage, mold, or fire damage, with honest information about how the referral works.</p>

        <h2>What we provide</h2>
        <ul>
          <li>Plain-language pages about common types of home damage around Fishers</li>
          <li>A phone number you can call for a referral connection</li>
          <li>Clear disclosure that we are not the contractor</li>
        </ul>

        <h2>What we don’t provide</h2>
        <ul>
          <li>On-site restoration, waterproofing, plumbing, roofing, or mold removal</li>
          <li>Guarantees about response time, pricing, or insurance coverage</li>
          <li>Medical advice about mold, sewage, or smoke exposure</li>
          <li>A walk-in office</li>
        </ul>

        <h2>Honesty matters</h2>
        <p>We don’t invent reviews, licenses, certifications, or years in business for this site, and we don’t use another company’s name or address. Ask any provider you talk with directly about their credentials, insurance, and experience.</p>

        <h2>Questions about the site?</h2>
        <p>For referrals, call {CALL}. For website or privacy questions, see <a href="contact.html">Contact</a>, <a href="privacy.html">Privacy Policy</a>, and <a href="terms.html">Terms of Use</a>.</p>'''
site.simple_page("about.html", "About This Referral Service | Fishers Water Damage",
                 "How the free Fishers, Indiana water damage referral line works, and what it does and does not provide.",
                 "About", "About This Referral Service",
                 "This site gives Fishers homeowners one clear next step after basement water, leaks, sewage, mold, or fire damage: a phone call with an independent local provider.",
                 about_inner, prio="0.5")

# ======================= CONTACT =======================
contact_inner = f'''        <div class="card" style="text-align:center;padding:2.5rem 1.5rem">
          <h2 class="mt-0">Free referral line</h2>
          <p>For flooded basements, sump pump failures, water damage, storm and roof leaks, burst pipes, sewage backups, mold, or fire and smoke damage in the Fishers area:</p>
          <p style="font-size:1.75rem;font-weight:800;margin:1rem 0">
            <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a>
          </p>
          <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
          <p class="muted" style="margin-top:1.5rem;margin-bottom:0">On a phone, tap the button to dial.</p>
        </div>
        <div class="notice" style="margin-top:1.5rem">
          <strong>Reminder:</strong> This is a referral connection service. Calls may be forwarded to an independent provider. There is no walk-in office.
        </div>
        <h2>Helpful to have ready</h2>
        <ul>
          <li>Your address or nearest cross street and ZIP code</li>
          <li>What happened (sump pump, pipe, roof, drain backup, fire)</li>
          <li>How deep the water is and whether the basement is finished</li>
          <li>Whether water is still coming in, and whether it might be sewage</li>
        </ul>'''
site.simple_page("contact.html", "Contact | Fishers Water Damage Referral",
                 "Call the free Fishers water damage referral line. Phone only, no form to fill out.",
                 "Contact", "Contact",
                 "Phone is the fastest way to reach us. There is no contact form on this site.",
                 contact_inner, prio="0.6")

site.legal_pages("November 11, 2026")
site.write()
