# Diagnosis-independent sections of the SAS report. Imported by the final assembler.
import os
S = os.path.dirname(os.path.abspath(__file__))
OBL = open(S + '/frag_obligations.html', encoding='utf-8').read()
QS = open(S + '/frag_questions.html', encoding='utf-8').read()

HOW_TO_READ = """
<p>Both instruments produce a distribution. The outside view produces quantiles natively; the
bottom-up's range comes from the optimistic, most-likely and pessimistic value in every rate cell,
summed under a <b>declared</b> item correlation of &rho; = 0.5 &mdash; independent items would claim
the total is known to &plusmn;1%, perfectly correlated ones would give &times;1.9, and the truth is
certainly neither. Across &rho; from 0.25 to 0.75 the band edges move about &plusmn;20%.</p>
<h4>The two outside-view readings are one sensor run twice</h4>
<p>Same input, same day, same engine. They built the same eight-branch class, excluded the same
neighbours, used the same relative anchors &mdash; and landed <b>&times;1.77 apart at the median
before any conversion</b>, because their absolute anchors differ: one staffs the class from tier-1
vendor patterns, the other sizes it in functional units against repository delivery rates. This is
the third case on which the class disagrees with itself by more than it disagrees with the chain.
<b>Only the marked quantiles are readings; the curve between them is interpolation.</b> Neither reading
quoted a P95 &mdash; both said the class contains non-delivery beyond P90 and declined to number it, so
the tails are hatched rather than drawn.</p>
<h4>The unit, and the one conversion applied</h4>
<p>Net hours of work on the task, shown as person-days of 8 such hours. <b>Leave, public holidays and
sickness are not in these numbers</b>, and neither is any notion of calendar or headcount. Each class
reading declared its own unit &mdash; 168 recorded hours per person-month with leave outside, and 152
charged hours per person-month with leave inside &mdash; and each put its own conversion to task hours
in a band containing 0.75. <b>The house factor 0.75 is applied to both</b>, to the class side only;
the bottom-up needs none, having been priced in task hours to begin with.</p>
<h4>Known direction of error</h4>
<p>The bottom-up curve is a normal approximation. Rate cells are right-skewed and correlated sums keep
skew, so the true upper tail is <b>fatter</b> than drawn.</p>
"""

DEFAULTS = """
<div class="stack">
  <div class="row"><span class="idx">A4</span><div class="body">
    <div class="t">Identity</div>
    <div class="x"><b>Taken:</b> the client's identity system issues claims through one protocol; the application keeps its own company&ndash;user&ndash;role model and hosts the administration. <b>Refused:</b> all user and role administration inside the identity system, which would reduce three obligations to interface calls.</div>
  </div></div>
  <div class="row"><span class="idx">A6</span><div class="body">
    <div class="t">Import and export <span class="chip red">worth a branch</span></div>
    <div class="x"><b>Taken:</b> six file formats plus the API, one adapter each; SAP reached through IDoc. <b>Refused:</b> bespoke connectors to named accounting or ERP products &mdash; the obligation says &ldquo;external systems such as QuickBooks or SAP&rdquo;.</div>
  </div></div>
  <div class="row"><span class="idx">A9</span><div class="body">
    <div class="t">Barcodes and the digital identifier</div>
    <div class="x"><b>Taken:</b> four symbologies from a library, at selectable sizes; the embeddable identifier is a snippet with no resolver behind it. <b>Refused:</b> a public resolver service &mdash; which the document itself names as future expansion.</div>
  </div></div>
  <div class="row"><span class="idx">A8 &middot; A14</span><div class="body">
    <div class="t">The read store and the reports</div>
    <div class="x"><b>Taken:</b> one non-transactional read store fed as changes occur, with reports built into the solution over it. <b>Refused:</b> overnight batch replication; a third-party business-intelligence product. &ldquo;Near real-time&rdquo; has no number in the document and none was pinned.</div>
  </div></div>
  <div class="row"><span class="idx">A10</span><div class="body">
    <div class="t">Twenty-five industries</div>
    <div class="x"><b>Taken:</b> one configurable mechanism per varying thing, industry parameters as configuration data the client maintains; the industry count multiplies nothing. <b>Refused:</b> industry-specific code paths.</div>
  </div></div>
  <div class="row"><span class="idx">A16 &middot; A17</span><div class="body">
    <div class="t">Migration and environments</div>
    <div class="x">Seven entity kinds from the current applications, two rehearsal cycles; four environments, the fourth read as a shared integration environment. The first case in the project to declare migration at all &mdash; the sizing sensors split on whether a store written at run time has a migration count, and the catalogue owes an answer.</div>
  </div></div>
  <div class="row"><span class="idx">scope &times;2</span><div class="body">
    <div class="t">Two decisions in the technology declaration</div>
    <div class="x">One team at one site rather than a distributed delivery (the document names an outsourcing vendor and no site) &middot; an external penetration test and remediation rather than none (nothing in the document names one; three once-scoped items hang on it). Each a declared fork, each separately priceable.</div>
  </div></div>
  <div class="row"><span class="idx">term</span><div class="body">
    <div class="t">Not a default but a hole <span class="chip caution">question for the client</span></div>
    <div class="x">The post-production support period and transition service are <b>carried and not priced</b>: an open-ended obligation has no effort figure until somebody says for how long and at what service level.</div>
  </div></div>
</div>
"""

FINDINGS = """
<div class="stack">
  <div class="row"><span class="idx">I-7</span><div class="body">
    <div class="t">The rules the software must obey do not exist yet <span class="chip red">largest driver, both class readings</span></div>
    <div class="x">&ldquo;All functionality is validated against X-Customer Standards and business rules, <b>which will be defined as part of the project</b>.&rdquo; Both outside-view readings, independently, named this the class's characteristic tail: the requirement set moving while it is built. The chain prices elaboration of what is known; the gap-blind scope-growth rate prices the change.</div>
  </div></div>
  <div class="row"><span class="idx">NFR-3 / G-1</span><div class="body">
    <div class="t">Where do users and roles live</div>
    <div class="x">One obligation puts accounts and roles in an enterprise identity system whose protocol &ldquo;has not been finalized&rdquo;; another puts user administration in the hands of a company administrator inside the application. Reading taken: both, joined by one claims integration.</div>
  </div></div>
  <div class="row"><span class="idx">P-13 / P-14</span><div class="body">
    <div class="t">A stated plurality with no members</div>
    <div class="x">&ldquo;Supported barcodes of various types and sizes&rdquo; names no symbology. Four were assumed so that the model has something to count; the count is an assumption, declared as one.</div>
  </div></div>
  <div class="row"><span class="idx">A9 &middot; input format</span><div class="body">
    <div class="t">A chain finding, not a document finding</div>
    <div class="x">The crossing sensor sees element names, not obligation texts, so the performance-test activity fired on one statement of 24 &mdash; the five response-time targets live in the obligation text, which it never received. Named before any number existed; the gap-blind rates later priced the load test as a hole, which is what the record predicted.</div>
  </div></div>
  <div class="row"><span class="idx">MD</span><div class="body">
    <div class="t">What the sensors refused rather than invented</div>
    <div class="x">Twenty-five judgement refusals at the crossing, all one question asked twice: does a parent holding only design statements draw test activities, and is a store fed from inside the system a migration target. Three elements refused as too coarse to size (XL) by both sizing repeats: the notification engine, the record import service, the basic-and-full attribute profiles. Catalogue findings, recorded, not repaired.</div>
  </div></div>
</div>
"""

PROVENANCE = """
<div class="stack">
  <div class="row"><span class="idx">1</span><div class="body"><div class="t">Product model &middot; n = 2</div><div class="x">146 product obligations &rarr; 246 elements (the second reading: 242, anchored structure &times;1.017). Produces no effort figure of any kind. Both replies lost their head in transit &mdash; a protocol fact on record, not a repair.</div></div></div>
  <div class="row"><span class="idx">2</span><div class="body"><div class="t">Work model</div><div class="x">Crossed against a declared technology, seven batches &rarr; 1 650 work items on 245 elements. May not invent an activity: work the product needs but no declared activity covers is reported as a <b>finding</b> &mdash; 25 such refusals here.</div></div></div>
  <div class="row"><span class="idx">3</span><div class="body"><div class="t">Size classes &middot; n = 2</div><div class="x">Each of 187 elements classified by counting named things, the enumeration being the justification. Refuses to run if shown any rate or price. Class agreement 85.0%; whole-chain repeat spread &times;1.0026.</div></div></div>
  <div class="row"><span class="idx">4</span><div class="body"><div class="t">Rate table <span class="chip caution">uncalibrated</span></div><div class="x">External norms in net task hours, gap-blind: never saw a project total, a budget, or a gap a rate would explain. Calibrated against no outcome &mdash; the centre is norms passed through a measured size vector, not a validated cost.</div></div></div>
  <div class="row"><span class="idx">5</span><div class="body"><div class="t">Outside view &times;2</div><div class="x">Ran in parallel and in ignorance of all of the above, the unit convention withheld so that each declared its own. Both quarantined the repository status the harness prepends, naming the numeric commit subject in it without using it.</div></div></div>
  <div class="row"><span class="idx">6</span><div class="body"><div class="t">Steps B, C, D</div><div class="x">Calibration parameters from a gap-blind source that never saw the outside view or the size of the gap; then the diagnosis, the only participant permitted to see more than one method's output &mdash; told in its brief that no outcome exists.</div></div></div>
</div>
<h4>Two coordinates, not one</h4>
<p>An estimate is a property of the triple <b>(project &times; engine &times; model)</b>. Every sensor
on this case ran on the same model, Claude Opus 5, so the model coordinate is held fixed and the
readings above are engine-and-project readings only.</p>
<h4>The declaration is required, not volunteered</h4>
<p>Every role that produces a number must state, before any figure, <b>its unit, whether leave sits
inside it, whose roles are counted, and how far its own sources disagree</b>. This case is the first
on which two readings of one sensor declared <i>different</i> units &mdash; 168 recorded hours per
person-month with leave outside, 152 charged hours with leave inside &mdash; which is exactly what
requiring the declaration was for.</p>
"""

METHODOLOGY = """
<div class="stack">
  <div class="row"><span class="idx">frame</span><div class="body">
    <div class="t"><a href="../../../METHODOLOGY.md">METHODOLOGY.md</a></div>
    <div class="x">Why independence of <b>techniques</b> replaces independence of experts, what each method is structurally blind to, and why a divergence is diagnosed rather than averaged.</div>
  </div></div>
  <div class="row"><span class="idx">chain</span><div class="body">
    <div class="t"><a href="../../../docs/instrument.md">docs/instrument.md</a></div>
    <div class="x">What actually runs: the product model, the crossing against a declared technology, the size classes, the pinned table, the script. What is pinned at each step and what each sensor is forbidden to produce.</div>
  </div></div>
  <div class="row"><span class="idx">numbers</span><div class="body">
    <div class="t"><a href="../../../docs/constants.md">docs/constants.md</a></div>
    <div class="x">Every constant the method has, and the comparison-layer conversion pinned by the author: 6 net task hours per present day, &times;1.10 leave, 21 days &mdash; so 1 staffed person-month &asymp; 114.5 net task hours.</div>
  </div></div>
  <div class="row"><span class="idx">case</span><div class="body">
    <div class="t"><a href="../../../docs/case_profile.md">docs/case_profile.md</a></div>
    <div class="x">The rule this case was the first to follow: team grade, site count, domain familiarity and the outcome's unit are pinned <b>before</b> any estimate exists, so that no condition can be chosen after a number is on the table.</div>
  </div></div>
  <div class="row"><span class="idx">isolation</span><div class="body">
    <div class="t"><a href="../../../PIPELINE.md">PIPELINE.md</a></div>
    <div class="x">The visibility matrix: who may see what, in what order the sensors are launched, and the disciplines that are mechanically checkable rather than promised.</div>
  </div></div>
  <div class="row"><span class="idx">prices</span><div class="body">
    <div class="t"><a href="../../../docs/rate_table.md">docs/rate_table.md</a> &middot; <a href="../../../docs/technology_catalogue.md">technology_catalogue.md</a></div>
    <div class="x">The pinned rates, in net person-hours, written gap-blind by a role that never saw a project total. And the vocabulary a technology declaration is written in &mdash; this case's declaration proposes one amendment to it.</div>
  </div></div>
  <div class="row"><span class="idx">done</span><div class="body">
    <div class="t"><a href="../../../docs/exit_criterion.md">docs/exit_criterion.md</a></div>
    <div class="x">When the instrument may be called fit for use, decided in advance. This case scores repeatability and, given a human scale, position; it cannot score calibratability, because it has no outcome.</div>
  </div></div>
  <div class="row"><span class="idx">this case</span><div class="body">
    <div class="t"><a href="../">examples/SAS/</a></div>
    <div class="x">The pinned inputs, the case profile, the assumption log, the technology declaration, and every run with its raw sensor output kept verbatim.</div>
  </div></div>
</div>
"""
