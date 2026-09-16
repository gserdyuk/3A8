# Run from anywhere: python examples/SAS/report_src/make_report_sas_v2.py  ->  examples/SAS/report_data_v2.json
# Assembles the data file of the v2 estimate (estimate_SAS_2026-09-16.md): the 2.1 chain through the plugin, runs 57-60,
# as the only bottom-up on the chart. The v1 estimate of record (2026-09-08, the 1.1 chain) is NOT drawn: its
# product-model engine (Hotyn-M 1.1) is retired and the installed instrument cannot produce it; it appears as a tile
# and in the text. (The 03:03 build of this file drew it as a dashed bell by mistake; removed in the next build.)
# The outside view, the no-method family, the obligations, questions and defaults are the case's and are shared with v1.
# Unit on the chart: person-days of 8 net task hours.
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import report_static as st
NOMETH = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "run49_raw", "curves_pd.json"), encoding="utf-8"))

H = 8.0
def pd(h): return round(h / H)

# the 2.1 chain (runs 57-59) and its calibration (run 60)
raw = 33444; raw_lo = 31954; raw_hi = 34933
cal_lo_c, cal_hi_c = 48483, 52608
cal_c = (cal_lo_c + cal_hi_c) / 2
cal_lo, cal_hi = 39837, 72031
sd_raw = 5288; sd_cal = sd_raw * (cal_c / raw)
# the v1 estimate of record (run 47 + run 48): a tile, not a curve - its engine is retired
v1_raw = 38118; v1_cal = 57600
# class, house factor 0.75 (constants 5b); RC46-1: 168 h/PM, RC46-2: 152 h/PM (as on the v1 chart)
rc1 = {q: pm * 168 * 0.75 for q, pm in [(0.1, 180), (0.5, 380), (0.8, 640), (0.9, 850)]}
rc2 = {q: pm * 152 * 0.75 for q, pm in [(0.1, 125), (0.5, 215), (0.8, 330), (0.9, 440)]}

d = {
 "title": "Project estimate",
 "eyebrow": "3A8 &middot; TriAngulEight",
 "headline": "Project estimate",
 "subject": "Case SAS &middot; member application solution for a standards body, 2018 &middot; RFP stage &middot; <b>no outcome, ever</b> &middot; v2: the estimate produced through the packaged instrument",
 "standfirst": "The same case estimated again, this time through the <code>3a8</code> plugin &mdash; the instrument as it is installed today &mdash; with the current product-model engine. The 187 leaves of the product are the same as on 8 September; the skeleton above them is shallower, and the whole difference between the two estimates, &times;0.88 before and after calibration, is the price of that skeleton. The estimate of record from 8 September is not drawn: its product-model engine is retired and the installed instrument cannot reproduce it. It is stated in a tile and in the text, and never averaged with this one.",
 "meta": [
  "<b>153</b> obligations &mdash; 146 product, 7 work",
  "<b>211</b> model elements &middot; <b>1 396</b> work items",
  "chain assembled <b>15&ndash;16 Sep</b> &middot; outside view read <b>8 Sep</b> &middot; diagnosed <b>16 Sep</b>",
  "unit <b>1 pd = 8 net task hours</b> &mdash; leave, holidays and sickness not included"
 ],
 "chart": {
  "axisMax": 15000,
  "rawSum": pd(raw),
  "rawSumLabel": "raw table sum %d (band %d–%d)" % (pd(raw), pd(raw_lo), pd(raw_hi)),
  "calibration": {"lo": pd(cal_lo), "hi": pd(cal_hi), "label": "calibration spread %d–%d · not percentiles" % (pd(cal_lo), pd(cal_hi))},
  "bottomUp": {"mu": pd(cal_c), "sd": pd(sd_cal)},
  "outside": [
   {"id": "RC46-1", "dash": "", "floor": pd(rc1[0.1] ** 2 / rc1[0.5]), "q": [[pd(v), q] for q, v in rc1.items()], "tailDrawn": False},
   {"id": "RC46-2", "dash": "6 4", "floor": pd(rc2[0.1] ** 2 / rc2[0.5]), "q": [[pd(v), q] for q, v in rc2.items()], "tailDrawn": False}
  ],
  "nomethod": NOMETH,
  "axisLabel": "NET WORKING TIME — PERSON-DAYS OF 8 TASK HOURS",
  "legend": [
   {"cls": "blue", "text": "Outside view RC46-1 &mdash; P50 %d (380 person-months at 168 recorded h)" % pd(rc1[0.5])},
   {"cls": "blue dash", "text": "Outside view RC46-2 &mdash; P50 %d (215 person-months at 152 charged h)" % pd(rc2[0.5])},
   {"cls": "red", "text": "Bottom-up, calibrated &mdash; P50 %d (the 2.1 chain through the plugin, runs 57&ndash;60)" % pd(cal_c)},
   {"cls": "ochre", "text": "No method &mdash; ten bare runs, one thin curve each, medians 2 730&ndash;5 250 (run 49)"}
  ],
  "hint": "<b>Two views of the same distributions.</b> Above, how likely each answer is &mdash; all curves on one scale, each enclosing the same area, so the bottom-up looks taller only because its mass is packed into a narrower range. Below, the same thing accumulated: <b>the chance of coming in at or under any figure</b>, which is what a number gets chosen against.<br><br><b>Move the pointer</b> and a read line crosses both panels, reporting the chance of exceeding that figure under each instrument. The two outside-view curves are <b>one sensor run twice on identical input</b>; each declared its own person-month and both are placed here by the house factor of 0.75 task hours per recorded hour, which both declarations contain (the diagnosis of this estimate used each reading's own factor band instead, 0.65&ndash;0.80, and shows both ends where they change a conclusion). The calibrated bottom-up sits at &times;1.05&ndash;1.27 of one reading's median and &times;1.85&ndash;2.30 of the other's &mdash; the diagnosis names that contradiction and does not resolve it. The bottom-up's width is the rate table's optimistic-to-pessimistic spread under a declared &rho; = 0.5, scaled by the calibration; it is a convention, not a measurement, and three times narrower than either class reading. Neither reading gave a floor; below P10 each curve is extended to P10&sup2;/P50 as a drawing convention. <b>The ten thin ochre curves</b> are the no-method baseline (run 49): the same document and assumption log handed to a bare agent with no method, ten times, never pooled.<br><br><b>No earlier estimate is drawn.</b> The estimate of record of 8 September (7 200 pd) came from a product-model engine that is now retired; the installed instrument cannot produce that curve, so it is not on this chart &mdash; it is a tile below and a section of the estimate document, &times;1.14 of this centre before and after calibration. The density panel&rsquo;s vertical axis reads as <b>chance per 100-pd window</b>; the exact mass is always the cumulative panel."
 },
 "tiles": [
  {"cls": "red", "k": "Centre", "v": "%d" % pd(cal_c), "unit": "pd", "d": "%d net task hours &asymp; 441 staffed person-months, the midpoint of the calibrated band 48 483&ndash;52 608 (repeat 2 &hellip; repeat 1). The table-priced assembly of %d &times; the gap-blind Step C chain, <b>&times;1.51</b> &mdash; the figure comparable with the outside view." % (round(cal_c), pd(raw))},
  {"cls": "red", "k": "Corridor &middot; P10&ndash;P90", "v": "%d&ndash;%d" % (pd(cal_c - 1.2816 * sd_cal), pd(cal_c + 1.2816 * sd_cal)), "unit": "pd", "d": "The drawn band. From the O/M/P in every rate cell, under a declared item correlation of <b>&rho; = 0.5</b>, scaled by the calibration."},
  {"cls": "", "k": "Calibration spread", "v": "%d&ndash;%d" % (pd(cal_lo), pd(cal_hi)), "unit": "pd", "d": "A different quantity, and <b>not percentiles</b>: the low chain on the lower repeat to the high chain on the upper one. 39 837 &ndash; 72 031 net task hours. Wider at the bottom than v1's because the sizing repeats disagree &times;1.09 on one rule (below)."},
  {"cls": "none", "k": "Previous estimate &middot; 8 Sep", "v": "%d" % pd(v1_cal), "unit": "pd", "d": "Not drawn. 57 600 net task hours &asymp; 503 staffed person-months, the estimate of record (<code>estimate_SAS_2026-09-08.md</code>), produced by a product-model engine (<code>Hotyn-M 1.1</code>) that the installed instrument no longer contains. <b>&times;1.14</b> of this estimate before and after calibration &mdash; the price of a skeleton of 59 parents against 24, integration at 54% of leaf effort against 46%. Which skeleton reads the product better, this case cannot say."},
  {"cls": "none", "k": "Reserve", "v": "Unresolved", "unit": "", "d": "Two P90s of one sensor that differ &times;2: %d and %d pd at the house factor. At each reading's own factor the lower P90 is <b>at or below the centre</b> and the higher lies 40&ndash;59 k h above it. Nothing averaged." % (pd(rc2[0.9]), pd(rc1[0.9]))},
  {"cls": "", "k": "Repeat spread", "v": "&times;1.093", "unit": "", "d": "Two independent size classifications, 77% class agreement, priced from the same table: 31 954 and 34 933 net task hours. Not noise: the repeats declared opposite rules for an obligation shared by several leaves &mdash; counted in full on each, or only for the part each leaf's name claims &mdash; a catalogue question the 2.1 model exposes and the 1.1 model hid (BACKLOG 2026-09-16)."},
  {"cls": "ochre", "k": "No method &middot; 10 runs", "v": "2 730&ndash;5 250", "unit": "pd", "d": "Medians of ten bare runs on the same text, mean 3 553 pd (169 person-months at 168 h). Spread &times;1.92 between runs, CV 25.5%; each run declares a &times;2.2 corridor of its own. Sits at &times;0.85 of this raw chain and &times;0.56 of the calibrated centre."},
  {"cls": "blue", "k": "Outside view &middot; P50", "v": "%d &middot; %d" % (pd(rc2[0.5]), pd(rc1[0.5])), "unit": "pd", "d": "Two readings of one sensor, in net working time: 215 and 380 person-months in their own declared units. <b>&times;1.95 apart</b> in commensurable hours, &times;1.77 as printed &mdash; reconciling units makes this gap larger, not smaller."}
 ],
 "sections": []
}

DIV = """
<div class="stack">
  <div class="row"><span class="idx">units first</span><div class="body">
    <div class="t">Units explain half to three quarters of one gap and manufacture the other <span class="chip blue">50&ndash;77%</span></div>
    <div class="x">Number against number the raw chain reads within &plusmn;6% of the lower class reading &mdash; convergence. After each reading's own touch-time factor (0.65&ndash;0.75 and 0.70&ndash;0.80) the chain is <b>&times;1.19&ndash;1.50 above</b> the lower reading's median and <b>&times;0.65&ndash;0.82 below</b> the higher one's. Against the higher reading, units are 50&ndash;77% of the naive gap; against the lower, &ldquo;units do not explain a gap; they hide one&rdquo;.</div>
  </div></div>
  <div class="row"><span class="idx">the seam</span><div class="body">
    <div class="t">The conversion may strip work the chain prices as items <span class="chip caution">unsized</span></div>
    <div class="x">The class readings' touch-time factor removes reviews, coordination and status time from their hours. The bottom-up prices some of exactly that: integration at every parent (46% of element work), code review, status reporting. If so, the converted class figures are too low by an amount nothing in the inputs sizes. Named for the first time on this case; the first thing that would change the diagnosis.</div>
  </div></div>
  <div class="row"><span class="idx">the class<br>vs itself</span><div class="body">
    <div class="t">The largest single quantity in the comparison <span class="chip blue">&times;1.95</span></div>
    <div class="x">The two outside-view medians are 22 876&ndash;26 144 and 41 496&ndash;47 880 net task hours at their own factors. Attributed, as on 8 September, to <b>one free parameter closed two ways</b>: the functional size and delivery rate behind the anchors &mdash; 320&ndash;400 person-months against an ISBSG anchor of 158 before uplift. No rate addresses it; it is the residual.</div>
  </div></div>
  <div class="row"><span class="idx">one way</span><div class="body">
    <div class="t">Calibration points up, overshoots one reading, widens the gap to the other</div>
    <div class="x">Against the higher reading the chain accounts for <b>104&ndash;269%</b> of the centre gap at that reading's own factors (the counted fills alone 34&ndash;85%; the crossing happens at the two globals). Against the lower, the corrections <b>widen</b> the gap: the centre lands &times;1.85&ndash;2.30 above its median. The residual left open is 22&ndash;30 k h below the centre on one side and &minus;11 to +3 k h on the other. &ldquo;I do not close it.&rdquo;</div>
  </div></div>
  <div class="row"><span class="idx">no method</span><div class="body">
    <div class="t">Ten bare runs land below the chain <span class="chip">&times;0.85</span></div>
    <div class="x">The no-method mean sits at &times;0.85 of this raw chain and &times;0.56 of its calibrated centre, inside the lower class reading. The ten medians spread &times;1.92 (CV 25.5%), and every run declares a corridor (&times;2.2) wider than that spread.</div>
  </div></div>
  <div class="row"><span class="idx">level</span><div class="body">
    <div class="t">The rate table's level <span class="chip caution">requested twice, not run</span></div>
    <div class="x">The one uncovered spot that acts multiplicatively on the whole centre. Both gap-blind rate rounds on this case declined to touch the table for lack of data, and both diagnoses ask for a narrow gap-blind round on exactly that question. Until it runs the centre is &ldquo;the table's level &times;1.5&rdquo;.</div>
  </div></div>
</div>
<h4>What Step C adds, and why the rates came out modest</h4>
<ul>
<li><b>H, hole fills</b> &mdash; the Access Data REST API's six unpriced items, migration of the stores that match a declared predecessor entity kind, the backup and DR statements: +138 / +373 / +787 h (repeat 1) priced by the estimate's own table at size S / M / L with integration along the real path.</li>
<li><b>C, closure fills</b> &mdash; the sizing sensors' closure violations <b>triaged against the assumption log</b>: about half closed by assumptions already taken (credentials in the identity provider, no accounting-system connectors, module-level stores are the shared domain model); the survivors &mdash; surfaces for screenless behaviours, other surfaces, behaviours, interfaces, stores, capacity and availability tests, the go-live initial load &mdash; +731 / +2 222 / +5 196 h.</li>
<li><b>T2 +8%</b> &mdash; project-long management, configuration and environment work that the structure prices once.</li>
<li><b>G2 &times;1.10</b> &mdash; a first-in-domain team (COCOMO II applications experience, Low).</li>
<li><b>G1 &times;1.18</b> &mdash; scope growth: the business rules and the identity protocol the document says will be decided during the project, the committee client's late decisions.</li>
<li><b>Refused</b>: the generic 20&ndash;30% omission rate for bottom-up task lists, because the coverage report shows every activity category carried; no integration, test, security, environment or documentation uplift. Overall <b>&times;1.51</b>, the same factor the 8 September round reached on the 1.1 structure by a different route.</li>
</ul>
<h4>False convergence, checked and refused</h4>
<p>Twice. The naive agreement with the lower class reading is a units artefact and disappears on
conversion. The calibrated centre straddles the higher reading's median at one end of a disputed
conversion factor (0.80: 51 072 against 48 483&ndash;52 608) &mdash; read as coincidence at one point,
not confirmation: the agreement vanishes at 0.65, and the second launch of the same class engine sits
at half that level.</p>
"""

FINDINGS2 = """
<div class="stack">
  <div class="row"><span class="idx">I-7</span><div class="body">
    <div class="t">The rules the software must obey do not exist yet <span class="chip red">largest driver, both class readings</span></div>
    <div class="x">&ldquo;All functionality is validated against X-Customer Standards and business rules, <b>which will be defined as part of the project</b>.&rdquo; Both outside-view readings named this the class's characteristic tail. The chain prices elaboration of what is known; the gap-blind scope-growth rate prices the change.</div>
  </div></div>
  <div class="row"><span class="idx">NFR-3 / G-1</span><div class="body">
    <div class="t">Where do users and roles live</div>
    <div class="x">One obligation puts accounts and roles in an enterprise identity system whose protocol &ldquo;has not been finalized&rdquo;; another puts user administration in the hands of a company administrator inside the application. Reading taken: both, joined by one claims integration.</div>
  </div></div>
  <div class="row"><span class="idx">shared<br>obligations</span><div class="body">
    <div class="t">One obligation on several leaves: counted once or on each? <span class="chip caution">&times;1.09 on the total</span></div>
    <div class="x">The 2.1 model keeps distinct leaves that realise the same obligations apart (six file-format adapters, the approval verbs of NFR-16 on three leaves). The sizing rules say &ldquo;count from the element's content plus its coverage&rdquo; and not whether a shared obligation counts in full on every leaf. The two sizing repeats declared opposite rules and differ 13 XL against 3. A catalogue precedent to adjudicate; until then it is this chain's widest step.</div>
  </div></div>
  <div class="row"><span class="idx">A9 &middot; input format</span><div class="body">
    <div class="t">A chain finding, not a document finding</div>
    <div class="x">The crossing sensor sees element names, not obligation texts, so the performance-test activity fired on one statement of 20 &mdash; this time the response-time design, whose name states that targets exist; the availability statements (99.9%, tested failover) drew none because their names state no figure. The gap-blind rates later priced the availability and capacity tests as fills, which is what the record predicted.</div>
  </div></div>
  <div class="row"><span class="idx">MD</span><div class="body">
    <div class="t">What the sensors refused rather than invented</div>
    <div class="x">Six judgement refusals at the crossing, all one question: is a store fed from inside the system a migration target (the read store, the role catalogue seeded with four roles). The other question of 8 September &mdash; does a parent holding only design statements draw test activities &mdash; could not arise on this skeleton. Sixteen of 24 stores drew no migration count because no predecessor entity kind was shown to need loading; the Access Data REST API was refused as unsizeable by both repeats. Recorded, not repaired.</div>
  </div></div>
</div>
"""

PROVENANCE2 = """
<div class="stack">
  <div class="row"><span class="idx">1</span><div class="body"><div class="t">Product model &middot; n = 2 &middot; <code>Hotyn-M 2.1</code></div><div class="x">146 product obligations &rarr; 211 elements: 187 leaves, 24 nodes (the second reading: 235 rows, 195 leaves, 41 nodes; leaves &times;1.04, anchored structure &times;1.11). Coverage lives in leaves only; childless and one-child nodes are deleted at closure. Produces no effort figure of any kind. Both replies arrived whole in one turn under a raised output cap &mdash; the protocol fact of 8 September (replies truncated in transit) did not recur.</div></div></div>
  <div class="row"><span class="idx">2</span><div class="body"><div class="t">Work model &middot; <code>Hotyn-W 1.2</code></div><div class="x">Crossed against the same declared technology as 8 September, byte for byte, seven batches &rarr; 1 396 work items on 210 elements. The per-element layer is the 8 September reading within 4%; the per-parent layer is half, because the skeleton has 23 parents where the old one had 58. Six judgement refusals, all one catalogue question.</div></div></div>
  <div class="row"><span class="idx">3</span><div class="body"><div class="t">Size classes &middot; n = 2 &middot; <code>Hotyn-D 2.0</code></div><div class="x">Each of 187 leaves classified by counting named things, the enumeration being the justification. Refuses to run if shown any rate or price. Class agreement 77%; whole-chain repeat spread &times;1.093, one declared rule apart.</div></div></div>
  <div class="row"><span class="idx">4</span><div class="body"><div class="t">Rate table <span class="chip caution">uncalibrated</span></div><div class="x">External norms in net task hours, gap-blind: never saw a project total, a budget, or a gap a rate would explain. Calibrated against no outcome &mdash; the centre is norms passed through a measured size vector, not a validated cost. The same table v0.1-h as 8 September.</div></div></div>
  <div class="row"><span class="idx">5</span><div class="body"><div class="t">Outside view &times;2 &middot; <code>Lytin-R 1.1</code></div><div class="x">The two readings of 8 September, reused as they stand: they ran in ignorance of any bottom-up, and the bottom-up they are now compared with did not exist when they were taken.</div></div></div>
  <div class="row"><span class="idx">0</span><div class="body"><div class="t">No method &times;10</div><div class="x">The document and the assumption log handed to a bare agent ten times, no sensor definition, one permitted file read each. The floor the chain must beat to be worth its cost: on repeatability it is &times;1.92 across runs against the chain's &times;1.093.</div></div></div>
  <div class="row"><span class="idx">6</span><div class="body"><div class="t">Steps C, B, D &middot; <code>Lytin-K 1.1</code>, <code>Lytin-G 1.1</code></div><div class="x">Calibration parameters from a gap-blind source that never saw the outside view, the size of the gap or the estimate of 8 September; then the diagnosis, the only participant permitted to see more than one method's output &mdash; told that no outcome exists, and given no figure of the earlier estimate. Its arithmetic matched the orchestrator's pre-registered recomputation to the hour.</div></div></div>
</div>
<h4>The instrument as installed</h4>
<p>Every sensor above ran as a subagent of the <b><code>3a8</code> plugin</b> (agents in <code>agents/</code>,
entry points <code>/3a8:estimate-product</code> and <code>/3a8:estimate</code>), launched from a child Claude
Code process with the plugin loaded, its output cap raised so that no sensor's turn was cut, every
prompt pinned with its checksum before launch, every raw reply transcribed from the harness
transcript. The estimate of 8 September was produced by the same sensors launched by hand from the
repository's own agent folder; the regression that separates the two (runs 52&ndash;60) found no
effect of the packaging and attributed the whole difference to the product-model engine's skeleton.</p>
<h4>Two coordinates, not one</h4>
<p>An estimate is a property of the triple <b>(project &times; engine &times; model)</b>. Every sensor
on this case ran on the same model, Claude Opus 5, so the model coordinate is held fixed. The engine
coordinate moved between the two estimates on this chart, and that is what the two bells measure.</p>
"""

NOT_IN = """
<div class="stack">
  <div class="row"><span class="idx">1</span><div class="body">
    <div class="t">The post-production support period <span class="chip caution">awaiting a parameter</span></div>
    <div class="x">Carried on every side, awaiting <b>the term and the service level</b>; the crossing entered it as a demanded branch without an activity. All instruments exclude it consistently; no double count. The one-sided risk that the higher class reading's anchors hold a warranty period inside the team's tenure is named and unpriced.</div>
  </div></div>
  <div class="row"><span class="idx">2</span><div class="body">
    <div class="t">The refused readings</div>
    <div class="x">Administration inside the identity system &middot; product connectors to accounting and ERP systems &middot; a public resolver &middot; industry-specific code paths &middot; a business-intelligence product &middot; a distributed delivery &middot; no penetration test. Each a step change, not a multiplier; not in the centre, and <b>not priced as options on this case</b>.</div>
  </div></div>
  <div class="row"><span class="idx">3</span><div class="body">
    <div class="t">The rate table's level</div>
    <div class="x">Uncalibrated against any outcome. A narrow gap-blind round is requested by both diagnoses on this case, not run. Until then the centre is the table's level raised &times;1.5, not an independent statement about effort.</div>
  </div></div>
  <div class="row"><span class="idx">4</span><div class="body">
    <div class="t">UX design and knowledge transfer <span class="chip caution">uncovered</span></div>
    <div class="x">In both class readings' role lists, not visible among the carried activity categories; only the 33-hour handover pack carries transfer. Requested as a gap-blind round; no rate covers them.</div>
  </div></div>
  <div class="row"><span class="idx">5</span><div class="body">
    <div class="t">The era</div>
    <div class="x">Eight years between the document and the norms. Every instrument refused to adjust, for the same reason: tooling pulls down, expectations on security, accessibility and operability pull up, and no source decides which wins.</div>
  </div></div>
  <div class="row"><span class="idx">6</span><div class="body">
    <div class="t">Tail and failure events</div>
    <div class="x">A late or changed identity platform, business rules never defined, committee stalemate, migration data that cannot be reconciled, a failed failover or ten-million-record performance test. Inside the class quantiles, in no bottom-up item &mdash; hence in the reserve and nowhere else. <b>IE9 compatibility blowing up is owned by no instrument.</b></div>
  </div></div>
  <div class="row"><span class="idx">7</span><div class="body">
    <div class="t">Effort to calendar, and team availability</div>
    <div class="x">A separate step, deliberately. Task hours do not become dates without a team shape, and this report supplies no team shape.</div>
  </div></div>
</div>
"""

d["footer"] = {
 "brand": "3A8",
 "brandsub": "TriAngulEight<br>an estimation instrument",
 "fine": [
  "<b>What this report is not.</b> Not a validated price, and not a price at all &mdash; it is work content in net task hours, shown as person-days of eight such hours. Converting it into money, calendar or headcount is the reader's act, using the reader's own figures. Every bottom-up number rests on a rate table of external industry norms calibrated against no outcome; the bottom-up stands on one product model; the previous estimate of this case, from a retired engine version, is stated in a tile at &times;1.14 and not drawn; the case has no outcome and never will.",
  "<b>What it is.</b> The estimate the instrument produces today, its corridor, the disagreement between two structurally independent methods stated rather than averaged away &mdash; here, chiefly the disagreement of the outside view with itself &mdash; and, on the record, the obligations, the findings, the questions and the defaults that the number is standing on."
 ]
}

d["sections"] = [
 {"id": "how-to-read", "title": "How to read the chart", "count": "the method", "lead": "Both instruments produce a distribution. Only one of them did so without being asked.", "html": st.HOW_TO_READ, "src": "docs/constants.md &middot; docs/instrument.md &middot; docs/sensors/"},
 {"id": "divergence", "title": "Why the methods disagree", "count": "&times;0.65 &ndash; &times;1.50", "lead": "At each reading's own conversion the raw chain sits between the two readings of the outside view; the calibrated centre sits above both. Steps B&ndash;D attributed the gaps without closing them, found the largest one inside the outside view itself, and named a seam in the conversion that nothing sizes.", "html": DIV, "src": "examples/SAS/run60_steps_BD.md &middot; run60_raw/RG60.md &middot; run60_raw/RK60.md"},
 {"id": "obligations", "title": "Obligations", "count": "153", "lead": "One entry per obligation <b>as the document words it</b>, under the document's own ids. Ids never change, so every artefact downstream still means what it meant. <b>No run may add, remove, split or merge an entry.</b>", "html": st.OBL, "src": "examples/SAS/requirements_product.md &middot; requirements_work.md"},
 {"id": "findings", "title": "Findings", "count": "5", "lead": "Produced without being asked for, by instruments whose job was something else. The first is the document's own admission; the rest are what the sensors refused to invent.", "html": FINDINGS2, "src": "examples/SAS/run58_work_model.md &middot; run59_sizing_and_assembly.md &middot; run46_raw/"},
 {"id": "two-ways", "title": "Variant readings", "count": "22, all unasked", "lead": "Pinned before any run and consumed by every run. <b>Ask the client; if no answer comes, assume; declare the assumption; and when runs are compared afterwards, exclude the differences the open question causes.</b> All stand unasked here, because this document has no client behind it.", "html": st.QS, "src": "examples/SAS/open_questions.md"},
 {"id": "defaults", "title": "Defaults", "count": "8", "lead": "Each is a fork the document leaves open and the estimate had to close. <b>The reading taken is inside the centre; the reading refused is not.</b>", "html": st.DEFAULTS, "src": "examples/SAS/assumptions.md &middot; technology_declaration.md"},
 {"id": "not-in-number", "title": "Estimate gaps", "count": "7", "lead": "Not oversights. Each is a thing the chain refused to price, with the reason it refused.", "html": NOT_IN, "src": "examples/SAS/estimate_SAS_2026-09-16.md"},
 {"id": "provenance", "title": "Where every number came from", "count": "7 roles", "lead": "Each sensor is an engine with a version, stamped on its own output. They are hired for what they are <b>forbidden to see</b>, not for autonomy.", "html": PROVENANCE2, "src": "PIPELINE.md &middot; docs/instrument.md &middot; skills/estimate/SKILL.md"},
 {"id": "methodology", "title": "Methodology", "count": "the documents", "lead": "This report is one output of a method that is written down. Nothing below is specific to this case; every file states what it is for, what it may not do, and what would change it.", "html": st.METHODOLOGY, "src": "the report format: tools/report/build_report.py"}
]

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'report_data_v2.json')
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print('written', out, 'centre', pd(cal_c), 'sd', pd(sd_cal), 'corridor', pd(cal_c - 1.2816 * sd_cal), pd(cal_c + 1.2816 * sd_cal), 'previous estimate (tile only)', pd(v1_cal))
