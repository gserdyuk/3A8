# Run from anywhere: python examples/SAS/report_src/make_report_sas.py  ->  examples/SAS/report_data.json
# Assembles examples/SAS/report_data.json. Unit on the chart: person-days of 8 net task hours.
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import report_static as st

H = 8.0
def pd(h): return round(h / H)

# chain
raw = 38118; cal_c = 57600; cal_lo = 48092; cal_hi = 74123
sd_raw = 6330; sd_cal = sd_raw * (cal_c / raw)
# class, house factor 0.75 (constants 5b); RC46-1: 168 h/PM, RC46-2: 152 h/PM
rc1 = {q: pm * 168 * 0.75 for q, pm in [(0.1, 180), (0.5, 380), (0.8, 640), (0.9, 850)]}
rc2 = {q: pm * 152 * 0.75 for q, pm in [(0.1, 125), (0.5, 215), (0.8, 330), (0.9, 440)]}

d = {
 "title": "Project estimate",
 "eyebrow": "3A8 &middot; TriAngulEight",
 "headline": "Project estimate",
 "subject": "Case SAS &middot; member application solution for a standards body, 2018 &middot; RFP stage &middot; <b>no outcome, ever</b>",
 "standfirst": "The third case, and the first prepared under the case-profile rule: the team, the site, the domain and the absence of an outcome were pinned before any number existed. The chain was run end to end on one model coordinate; two readings of the outside view were taken in ignorance of it and landed on both sides of it, &times;1.8 apart from each other.",
 "meta": [
  "<b>153</b> obligations &mdash; 146 product, 7 work",
  "<b>246</b> model elements &middot; <b>1 650</b> work items",
  "chain assembled <b>8 Sep</b> &middot; outside view read <b>8 Sep</b> &middot; diagnosed <b>8 Sep</b>",
  "unit <b>1 pd = 8 net task hours</b> &mdash; leave, holidays and sickness not included"
 ],
 "chart": {
  "axisMax": 15000,
  "rawSum": pd(raw),
  "rawSumLabel": "raw table sum %d" % pd(raw),
  "calibration": {"lo": pd(cal_lo), "hi": pd(cal_hi), "label": "calibration spread %d\u2013%d \u00b7 not percentiles" % (pd(cal_lo), pd(cal_hi))},
  "bottomUp": {"mu": pd(cal_c), "sd": pd(sd_cal)},
  "outside": [
   {"id": "RC46-1", "dash": "", "floor": pd(rc1[0.1] ** 2 / rc1[0.5]), "q": [[pd(v), q] for q, v in rc1.items()], "tailDrawn": False},
   {"id": "RC46-2", "dash": "6 4", "floor": pd(rc2[0.1] ** 2 / rc2[0.5]), "q": [[pd(v), q] for q, v in rc2.items()], "tailDrawn": False}
  ],
  "axisLabel": "NET WORKING TIME \u2014 PERSON-DAYS OF 8 TASK HOURS",
  "legend": [
   {"cls": "blue", "text": "Outside view RC46-1 &mdash; P50 %d (380 person-months at 168 recorded h)" % pd(rc1[0.5])},
   {"cls": "blue dash", "text": "Outside view RC46-2 &mdash; P50 %d (215 person-months at 152 charged h)" % pd(rc2[0.5])},
   {"cls": "red", "text": "Bottom-up, calibrated &mdash; P50 %d" % pd(cal_c)}
  ],
  "hint": "<b>Two views of the same three distributions.</b> Above, how likely each answer is &mdash; all curves on one scale, each enclosing the same area, so the bottom-up looks taller only because its mass is packed into a narrower range. Below, the same thing accumulated: <b>the chance of coming in at or under any figure</b>, which is what a number gets chosen against.<br><br><b>Move the pointer</b> and a read line crosses both panels, reporting the chance of exceeding that figure under each instrument. The two outside-view curves are <b>one sensor run twice on identical input</b>; each declared its own person-month and both are placed by the house factor of 0.75 task hours per recorded hour, which both declarations contain. The calibrated bottom-up sits at about P63 of one reading and above P90 of the other &mdash; the diagnosis names that contradiction and does not resolve it. The bottom-up's width is the rate table's optimistic-to-pessimistic spread under a declared &rho; = 0.5, scaled by the calibration; it is a convention, not a measurement, and three times narrower than either class reading. Neither reading gave a floor; below P10 each curve is extended to P10&sup2;/P50 &mdash; the same ratio as P10 to P50 &mdash; as a drawing convention, so that the tenth of the mass below P10 is not drawn as a spike. The density panel&rsquo;s vertical axis reads as <b>chance per 100-pd window</b>; the exact mass is always the cumulative panel."
 },
 "tiles": [
  {"cls": "red", "k": "Centre", "v": "%d" % pd(cal_c), "unit": "pd", "d": "57 600 net task hours &asymp; 503 staffed person-months. The table-priced assembly of %d &times; the gap-blind Step C chain, <b>&times;1.51</b> &mdash; the figure comparable with the outside view." % pd(raw)},
  {"cls": "red", "k": "Corridor &middot; P10&ndash;P90", "v": "%d&ndash;%d" % (pd(cal_c - 1.2816 * sd_cal), pd(cal_c + 1.2816 * sd_cal)), "unit": "pd", "d": "The drawn band. From the O/M/P in every rate cell, under a declared item correlation of <b>&rho; = 0.5</b>, scaled by the calibration."},
  {"cls": "", "k": "Calibration spread", "v": "%d&ndash;%d" % (pd(cal_lo), pd(cal_hi)), "unit": "pd", "d": "A different quantity, and <b>not percentiles</b>: the centre at the low and high ends of the Step C rates. 48 100 &ndash; 74 100 net task hours."},
  {"cls": "none", "k": "Reserve", "v": "Unresolved", "unit": "", "d": "Two P90s of one sensor that differ &times;2: %d and %d pd. The centre sits at ~P63 of one and <b>above P90</b> of the other. Nothing averaged." % (pd(rc2[0.9]), pd(rc1[0.9]))},
  {"cls": "", "k": "Repeat spread", "v": "&times;1.0026", "unit": "", "d": "Two independent size classifications, 85% class agreement, priced from the same table: 38 069 and 38 168 net task hours. Not a measure of precision, the diagnosis says: a symmetric cancellation is the likelier reading."},
  {"cls": "blue", "k": "Outside view &middot; P50", "v": "%d &middot; %d" % (pd(rc2[0.5]), pd(rc1[0.5])), "unit": "pd", "d": "Two readings of one sensor, in net working time: 215 and 380 person-months in their own declared units. <b>&times;1.95 apart</b> after conversion, &times;1.77 before it &mdash; units explain 4&ndash;7% of the gap."}
 ],
 "sections": []
}

DIV = """
<div class="stack">
  <div class="row"><span class="idx">the class<br>vs itself</span><div class="body">
    <div class="t">The largest single quantity in the comparison <span class="chip blue">&times;1.82</span></div>
    <div class="x">The two outside-view medians are 24 510 and 44 688&ndash;47 880 net task hours &mdash; three times the distance from the bottom-up to the nearer of them. Before any conversion the raw medians are 215 and 380 person-months, so the conversion did not create it; the two declared units come out within 3% of each other in task hours. <b>Attributed to one free parameter closed two ways</b>: the functional-size regime behind the repository anchor &mdash; one reading closed it with a number (1 200&ndash;3 000 units &times; ~12 h), the other with words (&ldquo;large band, over 1 000 FP&rdquo;) &mdash; plus a staffing anchor about two different crews, plus misclassification leaning opposite ways at equal 60% confidence.</div>
  </div></div>
  <div class="row"><span class="idx">units first</span><div class="body">
    <div class="t">The naive comparison inverts the diagnosis</div>
    <div class="x">Number against number, the chain reads 17% above the lower reading and 40% below the higher. After each reading's own declared conversion it is <b>56% above</b> the lower and <b>15% below</b> the higher. The direction survives in one case and the magnitude is wrong threefold; in the other, &ldquo;the instruments nearly agree&rdquo; would have been a pure artefact of units.</div>
  </div></div>
  <div class="row"><span class="idx">one way</span><div class="body">
    <div class="t">Calibration points up, so it cannot meet both readings</div>
    <div class="x">Every Step C correction is upward &mdash; the bottom-up's known systematic is omission. Against the higher reading the gap is explained 100% with a +12 900 h overshoot. Against the lower, <b>explained share 0%</b> and the gap widens &times;2.43. The class-vs-class gap is addressed by no rate at all. Stated in those words rather than closed by adjustment.</div>
  </div></div>
  <div class="row"><span class="idx">level</span><div class="body">
    <div class="t">The rate table's level <span class="chip caution">round requested</span></div>
    <div class="x">The one uncovered spot that acts multiplicatively on the whole centre. The rate agent spent both permitted globals on sourced effects and refused to touch the table; the diagnostician asks for a narrow gap-blind round on exactly that question and says the centre should be read as &ldquo;the table's level &times;1.50&rdquo; until it runs.</div>
  </div></div>
</div>
<h4>What Step C adds, and why the rates came out modest</h4>
<ul>
<li><b>T1, T2, T3</b> &mdash; the 31/14 named holes, the real share of ~30 closure violations, and the three coarse XL leaves, each with the structure's own 20% integration on the increment.</li>
<li><b>A-1&hellip;A-5</b> &mdash; five once-scoped additions the coverage report itself named as absent: a load test against the five response-time targets, a failover and backup/DR exercise, a WCAG 2.0 A evaluation, a cross-browser matrix, initial help content. 550 / 970 / 1 680 h, the same order as the existing once-scoped layer.</li>
<li><b>G2 &times;1.15</b> &mdash; a first-in-domain team, a committee-governed client, generic optimism, <b>merged</b> into one global rather than charged three times.</li>
<li><b>G1 &times;1.18</b> &mdash; scope growth: the business rules and the identity protocol the document says will be decided during the project.</li>
<li><b>Suppressed by the coverage report</b>: no integration uplift (paid at 59 parents), no test or rework multiplier (two cycles of each carried), no management, security, environment or documentation uplift. The rate agent called this the largest single effect of the run.</li>
</ul>
<h4>False convergence, checked and refused</h4>
<p>The raw chain, 38 118 h, lands within 1.3% of the lower reading's P80 &mdash; only at that reading's
central conversion factor. At either end of its own declared band the coincidence disappears. The
two class readings share an engine, a prompt and a blind-spot list, so their agreement on
<b>shape</b> (P90/P50 of 2.24 and 2.05) is reproducibility of one instrument, not independent
confirmation; their disagreement on <b>level</b> is a measurement of that instrument's dispersion.</p>
"""

NOT_IN = """
<div class="stack">
  <div class="row"><span class="idx">1</span><div class="body">
    <div class="t">The post-production support period <span class="chip caution">awaiting a parameter</span></div>
    <div class="x">Carried on every side, awaiting <b>the term and the service level</b>. All three instruments exclude it consistently; no double count. The one-sided risk that the class anchors hold a warranty period inside the team's tenure is named and unpriced.</div>
  </div></div>
  <div class="row"><span class="idx">2</span><div class="body">
    <div class="t">The refused readings</div>
    <div class="x">Administration inside the identity system &middot; product connectors to accounting and ERP systems &middot; a public resolver &middot; industry-specific code paths &middot; a business-intelligence product &middot; a distributed delivery &middot; no penetration test. Each a step change, not a multiplier; not in the centre, and <b>not priced as options on this case</b> &mdash; no step-event round was run.</div>
  </div></div>
  <div class="row"><span class="idx">3</span><div class="body">
    <div class="t">The rate table's level</div>
    <div class="x">Uncalibrated against any outcome. A narrow gap-blind round is requested, not run. Until then the centre is the table's level raised &times;1.50, not an independent statement about effort.</div>
  </div></div>
  <div class="row"><span class="idx">4</span><div class="body">
    <div class="t">The era</div>
    <div class="x">Eight years between the document and the norms. Three independent instruments refused to adjust, for the same reason: tooling pulls down, expectations on security, accessibility and operability pull up, and no source decides which wins.</div>
  </div></div>
  <div class="row"><span class="idx">5</span><div class="body">
    <div class="t">Tail and failure events</div>
    <div class="x">A late or changed identity platform, business rules never defined, committee stalemate, migration data that cannot be reconciled. Inside the class quantiles, in no bottom-up item &mdash; hence in the reserve and nowhere else.</div>
  </div></div>
  <div class="row"><span class="idx">6</span><div class="body">
    <div class="t">Effort to calendar, and team availability</div>
    <div class="x">A separate step, deliberately. Task hours do not become dates without a team shape, and this report supplies no team shape.</div>
  </div></div>
</div>
"""

d["footer"] = {
 "brand": "3A8",
 "brandsub": "TriAngulEight<br>an estimation instrument",
 "fine": [
  "<b>What this report is not.</b> Not a validated price, and not a price at all &mdash; it is work content in net task hours, shown as person-days of eight such hours. Converting it into money, calendar or headcount is the reader's act, using the reader's own figures. Every bottom-up number rests on a rate table of external industry norms calibrated against no outcome; the bottom-up stands on one product model of two; and this case has no outcome and never will, so nothing here has been checked against reality.",
  "<b>What it is.</b> The estimate, its corridor, the disagreement between two structurally independent methods stated rather than averaged away &mdash; here, chiefly the disagreement of the outside view with itself &mdash; and, on the record, the obligations, the findings, the questions and the defaults that the number is standing on."
 ]
}

d["sections"] = [
 {"id": "how-to-read", "title": "How to read the chart", "count": "the method", "lead": "Both instruments produce a distribution. Only one of them did so without being asked.", "html": st.HOW_TO_READ, "src": "docs/constants.md &middot; docs/instrument.md"},
 {"id": "divergence", "title": "Why the methods disagree", "count": "&times;0.85 &ndash; &times;1.56", "lead": "At equal scope the raw chain sits between the two readings of the outside view; the calibrated centre sits above both. Steps B&ndash;D attributed the gaps without closing them, and found the largest one inside the outside view itself.", "html": DIV, "src": "examples/SAS/run48_steps_BD.md &middot; run48_raw/diagnosis.md"},
 {"id": "obligations", "title": "Obligations", "count": "153", "lead": "One entry per obligation <b>as the document words it</b>, under the document's own ids. Ids never change, so every artefact downstream still means what it meant. <b>No run may add, remove, split or merge an entry.</b>", "html": st.OBL, "src": "examples/SAS/requirements_product.md &middot; requirements_work.md"},
 {"id": "findings", "title": "Findings", "count": "5", "lead": "Produced without being asked for, by instruments whose job was something else. The first is the document's own admission; the rest are what the sensors refused to invent.", "html": st.FINDINGS, "src": "examples/SAS/run45_work_model.md &middot; run47_sizing_and_assembly.md &middot; run46_raw/"},
 {"id": "two-ways", "title": "Variant readings", "count": "22, all unasked", "lead": "Pinned before any run and consumed by every run. <b>Ask the client; if no answer comes, assume; declare the assumption; and when runs are compared afterwards, exclude the differences the open question causes.</b> All stand unasked here, because this document has no client behind it.", "html": st.QS, "src": "examples/SAS/open_questions.md"},
 {"id": "defaults", "title": "Defaults", "count": "8", "lead": "Each is a fork the document leaves open and the estimate had to close. <b>The reading taken is inside the centre; the reading refused is not.</b>", "html": st.DEFAULTS, "src": "examples/SAS/assumptions.md &middot; technology_declaration.md"},
 {"id": "not-in-number", "title": "Estimate gaps", "count": "6", "lead": "Not oversights. Each is a thing the chain refused to price, with the reason it refused.", "html": NOT_IN, "src": "examples/SAS/estimate_SAS_2026-09-08.md"},
 {"id": "provenance", "title": "Where every number came from", "count": "6 roles", "lead": "Each sensor is an engine with a version, stamped on its own output. They are hired for what they are <b>forbidden to see</b>, not for autonomy.", "html": st.PROVENANCE, "src": "PIPELINE.md &middot; docs/instrument.md"},
 {"id": "methodology", "title": "Methodology", "count": "the documents", "lead": "This report is one output of a method that is written down. Nothing below is specific to this case; every file states what it is for, what it may not do, and what would change it.", "html": st.METHODOLOGY, "src": "the report format: tools/report/build_report.py"}
]

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'report_data.json')
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print('written', out, 'centre', pd(cal_c), 'corridor', pd(cal_c - 1.2816 * sd_cal), pd(cal_c + 1.2816 * sd_cal), 'rc1', {q: pd(v) for q, v in rc1.items()}, 'rc2', {q: pd(v) for q, v in rc2.items()})
