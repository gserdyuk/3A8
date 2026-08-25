#!/usr/bin/env python3
"""
Build an estimate report from a case data file.

    python tools/report/build_report.py examples/BMS/report_data.json

Writes  examples/<case>/reports/report_<YYYY-MM-DDTHHMM>.html  next to the data file
and updates  examples/<case>/reports/README.md  with one line for the new report.

Nothing about a particular project lives in this file. The data file carries the case;
this file carries the format. A second project supplies its own data file and gets the
same report: the same chart, the same accordion, the same footer.

Reports are never overwritten. A run produces a new timestamped file, because the
project records rather than edits: a report overwritten in place destroys the
comparison with the one before it.
"""

import json, os, sys, datetime, re

STYLE = r'''<style>
:root{
  --ground:#EEF0EA; --surface:#FAFBF7; --surface-2:#E7EAE1;
  --ink:#161A15; --ink-2:#3C443A; --muted:#5D655A; --faint:#8B9386;
  --rule:#D2D7C9; --rule-2:#BFC5B4;
  --pen-blue:#20456B; --pen-blue-fill:rgba(32,69,107,.10);
  --pen-red:#9E3B26; --pen-red-fill:rgba(158,59,38,.13);
  --caution:#7A5A12;
  --shadow:0 1px 2px rgba(22,26,21,.07), 0 8px 24px -12px rgba(22,26,21,.18);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#121410; --surface:#1A1D18; --surface-2:#22261E;
    --ink:#E6E9E1; --ink-2:#C6CCBE; --muted:#98A090; --faint:#727A6C;
    --rule:#2E3329; --rule-2:#3D4436;
    --pen-blue:#82ACD8; --pen-blue-fill:rgba(130,172,216,.13);
    --pen-red:#DD9078; --pen-red-fill:rgba(221,144,120,.16);
    --caution:#C9A758;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -14px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"]{
  --ground:#121410; --surface:#1A1D18; --surface-2:#22261E;
  --ink:#E6E9E1; --ink-2:#C6CCBE; --muted:#98A090; --faint:#727A6C;
  --rule:#2E3329; --rule-2:#3D4436;
  --pen-blue:#82ACD8; --pen-blue-fill:rgba(130,172,216,.13);
  --pen-red:#DD9078; --pen-red-fill:rgba(221,144,120,.16);
  --caution:#C9A758;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -14px rgba(0,0,0,.7);
}
*{box-sizing:border-box}
@media (prefers-reduced-motion:reduce){*{transition-duration:.01ms !important}}
body{margin:0; background:var(--ground); color:var(--ink);
  font-family:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:15px; line-height:1.6; -webkit-font-smoothing:antialiased}
.wrap{max-width:1060px; margin:0 auto; padding:0 24px 40px}
:focus-visible{outline:2px solid var(--pen-blue); outline-offset:2px}

header.mast{padding:34px 0 20px}
.eyebrow{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--muted)}
h1{font-family:Newsreader,Georgia,serif; font-weight:500; font-size:clamp(29px,4vw,42px);
  line-height:1.1; letter-spacing:-.015em; margin:10px 0 10px; text-wrap:balance}
h1 em{font-style:italic; color:var(--ink-2)}
.standfirst{max-width:68ch; color:var(--ink-2); font-size:16px; margin:0}
.mast-meta{display:flex; flex-wrap:wrap; gap:6px 24px; margin-top:16px;
  font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px; color:var(--muted)}
.mast-meta b{color:var(--ink-2); font-weight:500}

.chart-card{background:var(--surface); border:1px solid var(--rule); border-radius:3px;
  padding:22px 22px 14px; box-shadow:var(--shadow)}
.chart-legend{display:flex; flex-wrap:wrap; gap:9px 24px; margin-bottom:14px;
  font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11.5px; color:var(--ink-2)}
.lg{display:flex; align-items:center; gap:9px}
.lg i{width:22px; height:0; border-top-width:2px; border-top-style:solid; display:block; flex:none}
.lg.blue i{border-color:var(--pen-blue)} .lg.red i{border-color:var(--pen-red)}
.lg.dash i{border-top-style:dashed} .lg.dot i{border-top-style:dotted; border-top-width:3px}
.lg.fact i{border-color:var(--ink); border-top-width:3px}
svg.plot{width:100%; height:auto; display:block; overflow:visible}
svg.plot text{font-family:"IBM Plex Mono",ui-monospace,monospace; fill:var(--muted)}
.hint{margin:12px 0 0; padding-top:11px; border-top:1px solid var(--rule);
  font-size:12.5px; color:var(--muted)}
.hint b{color:var(--ink-2); font-weight:500}

.tiles{display:grid; grid-template-columns:repeat(auto-fit,minmax(185px,1fr)); gap:1px;
  background:var(--rule); border:1px solid var(--rule); border-radius:3px; overflow:hidden;
  margin-top:20px}
.tile{background:var(--surface); padding:16px 18px 18px; display:flex; flex-direction:column; gap:4px}
.tile .k{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:10px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--muted)}
.tile .v{font-family:Newsreader,Georgia,serif; font-size:26px; font-weight:500; line-height:1.1;
  letter-spacing:-.01em; font-variant-numeric:tabular-nums}
.tile .v small{font-size:13px; color:var(--muted); font-family:"IBM Plex Sans",sans-serif;
  font-weight:400; letter-spacing:0}
.tile .d{font-size:12px; color:var(--muted); margin-top:1px; line-height:1.45}
.tile.red .v{color:var(--pen-red)} .tile.blue .v{color:var(--pen-blue)}
.tile.none .v{font-size:17px; color:var(--caution)}
.tiles > .tile:last-child{grid-column:1/-1}

.acc{margin-top:34px; border:1px solid var(--rule); border-radius:3px; overflow:hidden;
  background:var(--rule)}
.acc > details{background:var(--surface); border-bottom:1px solid var(--rule)}
.acc > details:last-child{border-bottom:none}
.acc summary{list-style:none; cursor:pointer; padding:15px 20px; display:flex;
  align-items:baseline; gap:14px; transition:background .12s}
.acc summary::-webkit-details-marker{display:none}
.acc summary:hover{background:var(--surface-2)}
.acc summary .n{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px;
  color:var(--faint); flex:none; width:2.2em}
.acc summary .h{font-family:Newsreader,Georgia,serif; font-size:19px; font-weight:500;
  letter-spacing:-.01em; flex:1; text-wrap:balance}
.acc summary .c{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px;
  color:var(--muted); flex:none}
.acc summary .c::after{content:" +"; color:var(--faint)}
.acc details[open] > summary{background:var(--surface-2); border-bottom:1px solid var(--rule)}
.acc details[open] > summary .c::after{content:" \2212"}
.acc .panel{padding:20px 20px 26px}
.acc .panel > .lead{color:var(--ink-2); font-size:14px; margin:0 0 18px; max-width:74ch}
.acc .panel > .lead b{color:var(--ink)}

.stack{display:flex; flex-direction:column; gap:1px; background:var(--rule);
  border:1px solid var(--rule); border-radius:3px; overflow:hidden}
.row{background:var(--surface); padding:14px 18px; display:grid; grid-template-columns:auto 1fr;
  gap:15px; align-items:baseline}
.row .idx{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px; color:var(--faint);
  padding-top:2px; white-space:nowrap}
.row .body{min-width:0}
.row .t{font-weight:600; font-size:14px; margin-bottom:3px}
.row .x{color:var(--ink-2); font-size:13.5px}
.chip{display:inline-block; font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:9.5px;
  letter-spacing:.1em; text-transform:uppercase; padding:2px 7px; border-radius:2px;
  border:1px solid currentColor; margin-left:8px; vertical-align:1px; white-space:nowrap}
.chip.caution{color:var(--caution)} .chip.blue{color:var(--pen-blue)} .chip.red{color:var(--pen-red)}

.tbl-scroll{overflow-x:auto; border:1px solid var(--rule); border-radius:3px; background:var(--surface)}
.tbl-tall{max-height:min(58vh,520px); overflow-y:auto}
table{border-collapse:collapse; width:100%; min-width:600px; font-size:13.5px}
th,td{text-align:left; padding:10px 15px; border-bottom:1px solid var(--rule); vertical-align:top}
thead th{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:10px; letter-spacing:.1em;
  text-transform:uppercase; color:var(--muted); font-weight:400; background:var(--surface-2);
  white-space:nowrap; position:sticky; top:0; z-index:1}
tbody tr:last-child td{border-bottom:none}
td.num{text-align:right; font-variant-numeric:tabular-nums;
  font-family:"IBM Plex Mono",ui-monospace,monospace; white-space:nowrap}
td.q{color:var(--ink-2)}
.tag{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px; color:var(--pen-blue);
  white-space:nowrap}

.acc .panel h4{font-size:12px; font-family:"IBM Plex Mono",ui-monospace,monospace;
  text-transform:uppercase; letter-spacing:.1em; color:var(--muted); font-weight:400; margin:24px 0 9px}
.acc .panel p{margin:0 0 11px; max-width:74ch; font-size:13.5px; color:var(--ink-2)}
.acc .panel p b{color:var(--ink)}
.acc .panel ul{margin:0 0 12px; padding-left:19px; max-width:74ch; font-size:13.5px; color:var(--ink-2)}
.acc .panel li{margin-bottom:7px}
.acc .panel blockquote{margin:0 0 14px; padding:2px 0 2px 15px; border-left:2px solid var(--rule-2);
  font-family:Newsreader,Georgia,serif; font-size:16px; font-style:italic; color:var(--ink); max-width:66ch}
.src-line{margin-top:18px; padding-top:12px; border-top:1px solid var(--rule);
  font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px; color:var(--pen-blue)}
.acc .panel a{color:var(--pen-blue); text-decoration:none;
  border-bottom:1px solid color-mix(in srgb, var(--pen-blue) 35%, transparent)}
.acc .panel a:hover{border-bottom-color:var(--pen-blue)}
.row .t a{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:12.5px}

footer{margin-top:48px; padding:26px 0 8px; border-top:1px solid var(--rule-2);
  display:grid; grid-template-columns:minmax(190px,auto) 1fr; gap:28px 40px}
footer .brand{font-family:Newsreader,Georgia,serif; font-size:26px; font-weight:500;
  letter-spacing:-.01em; line-height:1.2}
footer .brand span{display:block; font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:10.5px; letter-spacing:.13em; text-transform:uppercase; color:var(--muted);
  margin-top:8px; line-height:1.8}
footer .fine{font-size:12.5px; color:var(--muted); max-width:74ch}
footer .fine b{color:var(--ink-2); font-weight:500}
footer .fine p{margin:0 0 9px}
footer .stamp{grid-column:1/-1; margin-top:8px; padding-top:14px; border-top:1px solid var(--rule);
  font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:10.5px; color:var(--faint)}
@media (max-width:640px){
  .wrap{padding:0 16px 32px}
  .row{grid-template-columns:1fr; gap:4px}
  .chart-card{padding:16px 12px 10px}
  .acc summary{padding:13px 15px; gap:10px}
  .acc summary .h{font-size:17px}
  .acc .panel{padding:16px 15px 22px}
  footer{grid-template-columns:1fr; gap:20px}
}
</style>'''

CHART_JS = r'''<script>
const CASE = __CHART__;

const W = 900, H = 440, M = {l:14, r:14, t:14, b:52};
const XMAX = CASE.axisMax, PW = W - M.l - M.r, AXIS_Y = H - M.b, PLOT_TOP = M.t + 6;
const X = v => M.l + (v / XMAX) * PW;
const XINV = px => (px - M.l) / PW * XMAX;

function segs(run){
  const pts = [[run.floor,0], ...run.q], out = [];
  for(let i=1;i<pts.length;i++){
    const [x0,p0]=pts[i-1], [x1,p1]=pts[i];
    out.push({x0,x1,p0,p1,d:(p1-p0)/(x1-x0)});
  }
  return out;
}
function smooth(arr){
  let cur = arr;
  for(let pass=0; pass<2; pass++){
    const k = 26;
    cur = cur.map((_,i)=>{
      let a=0,n=0;
      for(let j=Math.max(0,i-k); j<=Math.min(cur.length-1,i+k); j++){ a+=cur[j][1]; n++; }
      return [cur[i][0], a/n];
    });
  }
  return cur;
}
function sample(run){
  const sg = segs(run), out = [];
  const lo = run.floor, hi = run.q[run.q.length-1][0], N = 300;
  for(let i=0;i<=N;i++){
    const x = lo + (hi-lo)*i/N;
    let d = 0;
    for(const s of sg){ if(x>=s.x0 && x<=s.x1){ d = s.d; break; } }
    out.push([x,d]);
  }
  return smooth(out);
}
function normalSample(){
  const B = CASE.bottomUp, out=[], lo=Math.max(0,B.mu-3.6*B.sd), hi=B.mu+3.6*B.sd, N=300;
  for(let i=0;i<=N;i++){
    const x=lo+(hi-lo)*i/N;
    out.push([x, Math.exp(-0.5*Math.pow((x-B.mu)/B.sd,2))/(B.sd*Math.sqrt(2*Math.PI))]);
  }
  return out;
}
function cdfOutside(run, x){
  if(x <= run.floor) return 0;
  const sg = segs(run), last = sg[sg.length-1];
  if(x >= last.x1) return null;
  for(const s of sg) if(x <= s.x1) return s.p0 + (s.p1-s.p0)*(x-s.x0)/(s.x1-s.x0);
  return null;
}
function erf(z){
  const t=1/(1+0.3275911*Math.abs(z));
  const y=1-(((((1.061405429*t-1.453152027)*t)+1.421413741)*t-0.284496736)*t+0.254829592)*t*Math.exp(-z*z);
  return z>=0?y:-y;
}
const cdfNormal = x => 0.5*(1+erf((x-CASE.bottomUp.mu)/(CASE.bottomUp.sd*Math.SQRT2)));

const S = CASE.outside.map(sample), SW = normalSample();
const DMAX = Math.max(...S.flat().map(p=>p[1]), ...SW.map(p=>p[1]));
if(!isFinite(DMAX) || DMAX <= 0) throw new Error("no distribution to draw");
const Y = d => AXIS_Y - (d / DMAX) * (AXIS_Y - PLOT_TOP);
function at(pts, x){
  for(let j=1;j<pts.length;j++){
    if(x <= pts[j][0]){
      const [x0,d0]=pts[j-1], [x1,d1]=pts[j];
      return d0 + (d1-d0)*((x-x0)/(x1-x0 || 1));
    }
  }
  return pts[pts.length-1][1];
}
const path = pts => pts.map(([x,d],i)=>`${i?"L":"M"} ${X(x).toFixed(1)} ${Y(d).toFixed(1)}`).join(" ");
const areaPath = pts => `M ${X(pts[0][0]).toFixed(1)} ${AXIS_Y} ` + path(pts).slice(1) +
  ` L ${X(pts[pts.length-1][0]).toFixed(1)} ${AXIS_Y} Z`;

let svg = `<defs><pattern id="tail" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="7" stroke="var(--pen-blue)" stroke-width="1" opacity=".3"/></pattern></defs>`;

const STEP = XMAX > 2400 ? 200 : 100, MAJOR = STEP * 3;
for(let v=0; v<=XMAX; v+=STEP){
  const major = v % MAJOR === 0;
  svg += `<line x1="${X(v).toFixed(1)}" y1="${PLOT_TOP-6}" x2="${X(v).toFixed(1)}" y2="${AXIS_Y}"
    stroke="var(--rule)" stroke-width="1" opacity="${major?1:.45}"/>`;
  if(major) svg += `<text x="${X(v).toFixed(1)}" y="${AXIS_Y+18}" font-size="11" text-anchor="middle">${v}</text>`;
  else svg += `<line x1="${X(v).toFixed(1)}" y1="${AXIS_Y}" x2="${X(v).toFixed(1)}" y2="${AXIS_Y+4}" stroke="var(--rule-2)" stroke-width="1"/>`;
}
svg += `<text x="${X(XMAX)}" y="${AXIS_Y+36}" font-size="10" text-anchor="end" letter-spacing="1.4">${CASE.axisLabel}</text>`;

CASE.outside.forEach((r,i)=>{
  if(r.tailDrawn) return;
  const p90 = r.q[r.q.length-1][0], last = at(S[i],p90);
  svg += `<path d="M ${X(p90)} ${AXIS_Y} L ${X(p90)} ${Y(last).toFixed(1)}
    Q ${X((p90+XMAX)/2)} ${Y(last*.45).toFixed(1)} ${X(XMAX)} ${(AXIS_Y-5).toFixed(1)} L ${X(XMAX)} ${AXIS_Y} Z"
    fill="url(#tail)" stroke="none"/>`;
});

CASE.outside.forEach((r,i)=>{
  svg += `<path d="${path(S[i])}" fill="none" stroke="var(--pen-blue)" stroke-width="1.9"
    ${r.dash?`stroke-dasharray="${r.dash}"`:''} stroke-linejoin="round" stroke-linecap="round"/>`;
  r.q.forEach(([x,p])=>{
    svg += `<circle cx="${X(x).toFixed(1)}" cy="${Y(at(S[i],x)).toFixed(1)}" r="3"
      fill="var(--surface)" stroke="var(--pen-blue)" stroke-width="1.7"/>`;
  });
  const mx = r.q[1][0];
  svg += `<text x="${X(mx)}" y="${(Y(at(S[i],mx))-11).toFixed(1)}" font-size="11"
    text-anchor="middle" fill="var(--pen-blue)" font-weight="500">${r.id}</text>`;
});

svg += `<path d="${areaPath(SW)}" fill="var(--pen-red-fill)" stroke="none"/>`;
svg += `<path d="${path(SW)}" fill="none" stroke="var(--pen-red)" stroke-width="2.2" stroke-linejoin="round"/>`;
[CASE.bottomUp.mu-1.2816*CASE.bottomUp.sd, CASE.bottomUp.mu, CASE.bottomUp.mu+1.2816*CASE.bottomUp.sd]
  .forEach(x=>{
    svg += `<circle cx="${X(x).toFixed(1)}" cy="${Y(at(SW,x)).toFixed(1)}" r="3"
      fill="var(--surface)" stroke="var(--pen-red)" stroke-width="1.7"/>`;
  });

if(CASE.rawSum){
  svg += `<line x1="${X(CASE.rawSum)}" y1="${AXIS_Y}" x2="${X(CASE.rawSum)}" y2="${AXIS_Y-28}"
    stroke="var(--pen-red)" stroke-width="1.3" stroke-dasharray="3 3" opacity=".7"/>`;
  svg += `<text x="${X(CASE.rawSum)}" y="${AXIS_Y-33}" font-size="9.5" text-anchor="middle"
    fill="var(--pen-red)" opacity=".8">${CASE.rawSumLabel}</text>`;
}
const beyond = CASE.outside.find(r=>r.beyondLabel);
if(beyond) svg += `<text x="${X(XMAX)-4}" y="${AXIS_Y-10}" font-size="9.5" text-anchor="end"
  fill="var(--pen-blue)">${beyond.beyondLabel}</text>`;

if(CASE.fact){
  const f = CASE.fact;
  svg += `<line x1="${X(f.value)}" y1="${PLOT_TOP-6}" x2="${X(f.value)}" y2="${AXIS_Y}"
    stroke="var(--ink)" stroke-width="2"/>`;
  svg += `<rect x="${X(f.value)-3}" y="${PLOT_TOP-10}" width="6" height="6" fill="var(--ink)"/>`;
  const anchor = X(f.value) > W*0.6 ? "end" : "start";
  const dx = anchor === "end" ? -9 : 9;
  svg += `<text x="${X(f.value)+dx}" y="${PLOT_TOP+2}" font-size="11.5" text-anchor="${anchor}"
    fill="var(--ink)" font-weight="600">${f.label}</text>`;
}

if(CASE.calibration){
  const BY = PLOT_TOP+262, cs = CASE.calibration;
  svg += `<line x1="${X(cs.lo)}" y1="${BY}" x2="${X(cs.hi)}" y2="${BY}"
    stroke="var(--pen-red)" stroke-width="1.4" stroke-dasharray="5 4"/>`;
  [cs.lo,cs.hi].forEach(v=>{
    svg += `<line x1="${X(v)}" y1="${BY-6}" x2="${X(v)}" y2="${BY+6}" stroke="var(--pen-red)" stroke-width="1.4"/>`;
  });
  svg += `<text x="${X(cs.lo)}" y="${BY-11}" font-size="10.5" fill="var(--pen-red)">${cs.label}</text>`;
}

svg += `<line x1="${M.l}" y1="${AXIS_Y}" x2="${W-M.r}" y2="${AXIS_Y}" stroke="var(--rule-2)" stroke-width="1.5"/>`;
svg += `<g id="cursor" style="display:none">
  <line id="cur-line" y1="${PLOT_TOP-6}" y2="${AXIS_Y}" stroke="var(--ink)" stroke-width="1" opacity=".55"/>
  <g><rect id="cur-bg" rx="2" fill="var(--surface)" stroke="var(--rule-2)" stroke-width="1"/>
  <text id="cur-t" font-size="11"></text></g></g>`;
svg += `<rect id="hit" x="${M.l}" y="${PLOT_TOP-6}" width="${PW}" height="${AXIS_Y-PLOT_TOP+6}"
  fill="transparent" style="cursor:crosshair"/>`;

const plot = document.getElementById("plot");
plot.innerHTML = svg;

const cursor = document.getElementById("cursor"), curLine = document.getElementById("cur-line"),
      curBg = document.getElementById("cur-bg"), curT = document.getElementById("cur-t"),
      hit = document.getElementById("hit");
const pct = v => v === null ? "past its last quantile" : "P" + Math.round(v*100);

function move(evt){
  const pt = plot.createSVGPoint(), src = evt.touches ? evt.touches[0] : evt;
  pt.x = src.clientX; pt.y = src.clientY;
  const loc = pt.matrixTransform(plot.getScreenCTM().inverse());
  const v = Math.max(0, Math.min(XMAX, XINV(loc.x)));
  cursor.style.display = "";
  curLine.setAttribute("x1", X(v)); curLine.setAttribute("x2", X(v));

  const lines = [`${Math.round(v)} person-days · ${Math.round(v*8).toLocaleString("en")} h`];
  CASE.outside.forEach(r => lines.push(`${r.id}: ${pct(cdfOutside(r, v))}`));
  lines.push(`bottom-up: ${pct(cdfNormal(v))}`);
  if(CASE.fact) lines.push(`outcome: ${(v/CASE.fact.value).toFixed(2)}×`);

  curT.textContent = "";
  lines.forEach((s,i)=>{
    const t = document.createElementNS("http://www.w3.org/2000/svg","tspan");
    t.textContent = s; t.setAttribute("x", 0); t.setAttribute("dy", i ? 15 : 0);
    if(i===0) t.setAttribute("font-weight","600");
    t.setAttribute("fill", i===0 ? "var(--ink)" : (i===lines.length-1 ? "var(--pen-red)" : "var(--pen-blue)"));
    curT.appendChild(t);
  });
  const bw = 182, bh = 16 + lines.length*15;
  const flip = X(v) + bw + 14 > W - M.r;
  const bx = flip ? X(v) - bw - 10 : X(v) + 10, by = PLOT_TOP + 4;
  curBg.setAttribute("x", bx); curBg.setAttribute("y", by);
  curBg.setAttribute("width", bw); curBg.setAttribute("height", bh);
  curT.setAttribute("transform", `translate(${bx+11},${by+19})`);
}
hit.addEventListener("mousemove", move);
hit.addEventListener("touchmove", e=>{ move(e); e.preventDefault(); }, {passive:false});
hit.addEventListener("mouseleave", ()=>{ cursor.style.display = "none"; });
</script>'''


def render(d, stamp_human, data_path):
    legend = "\n      ".join(
        '<span class="lg %s"><i></i>%s</span>' % (l["cls"], l["text"]) for l in d["chart"]["legend"])
    meta = "\n    ".join("<span>%s</span>" % m for m in d["meta"])
    tiles = "\n    ".join(
        '<div class="tile %s"><div class="k">%s</div><div class="v">%s%s</div><div class="d">%s</div></div>'
        % (t["cls"], t["k"], t["v"], (" <small>%s</small>" % t["unit"]) if t["unit"] else "", t["d"])
        for t in d["tiles"])

    items = []
    for i, s in enumerate(d["sections"], 1):
        src = ('\n      <div class="src-line">%s</div>' % s["src"]) if s.get("src") else ""
        items.append(
            '    <details id="%s">\n'
            '      <summary><span class="n">%02d</span><span class="h">%s</span>'
            '<span class="c">%s</span></summary>\n'
            '      <div class="panel">\n        <p class="lead">%s</p>\n%s%s\n      </div>\n'
            '    </details>' % (s["id"], i, s["title"], s["count"], s["lead"], s["html"], src))
    acc = "\n".join(items)

    fine = "\n      ".join("<p>%s</p>" % p for p in d["footer"]["fine"])
    chart_json = json.dumps(d["chart"], ensure_ascii=False)

    return (
'<title>%s &middot; %s</title>\n'
'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&'
'family=IBM+Plex+Sans:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;'
'0,6..72,600;1,6..72,400&display=swap">\n\n' % (d["title"], stamp_human)
+ STYLE + r'''

<div class="wrap">

<header class="mast">
  <div class="eyebrow">''' + d["eyebrow"] + r'''</div>
  <h1>''' + d["headline"] + r'''</h1>
  <p class="stamp-line">''' + d["subject"] + r''' &middot; generated <b>''' + stamp_human + r'''</b></p>
  <p class="standfirst">''' + d["standfirst"] + r'''</p>
  <div class="mast-meta">
    ''' + meta + r'''
  </div>
</header>

<div class="chart-card">
  <div class="chart-legend">
      ''' + legend + r'''
  </div>
  <svg class="plot" id="plot" viewBox="0 0 900 440" role="img"
    aria-label="Estimate distributions plotted on one net-working-time scale in person-days of eight task hours."></svg>
  <p class="hint">''' + d["chart"]["hint"] + r'''</p>
</div>

<div class="tiles">
    ''' + tiles + r'''
</div>

<div class="acc">
''' + acc + r'''
</div>

<footer>
  <div class="brand">''' + d["footer"]["brand"] + r'''<span>''' + d["footer"]["brandsub"] + r'''</span></div>
  <div class="fine">
      ''' + fine + r'''
  </div>
  <div class="stamp">generated ''' + stamp_human + r''' &middot; from ''' + data_path + r''' &middot; format: tools/report/build_report.py</div>
</footer>

</div>
''' + CHART_JS.replace("__CHART__", chart_json) + "\n")


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: build_report.py <case>/report_data.json")
    data_path = sys.argv[1].replace("\\", "/")
    d = json.load(open(data_path, encoding="utf-8"))

    now = datetime.datetime.now()
    stamp = now.strftime("%Y-%m-%dT%H%M")
    human = now.strftime("%Y-%m-%d %H:%M")

    outdir = os.path.join(os.path.dirname(data_path), "reports")
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, "report_%s.html" % stamp).replace("\\", "/")

    html = render(d, human, data_path)
    open(outfile, "w", encoding="utf-8", newline="\n").write(html)

    # index — one line per report, newest last, so the history of a case reads in order
    idx = os.path.join(outdir, "README.md").replace("\\", "/")
    if not os.path.exists(idx):
        open(idx, "w", encoding="utf-8", newline="\n").write(
            "# Reports\n\nOne file per run. **Reports are never overwritten** — a new run produces a\n"
            "new timestamped file, because a report replaced in place destroys the comparison with\n"
            "the one before it. Add the one-line note yourself: what moved, and why.\n\n"
            "| generated | file | centre | what changed |\n|---|---|---|---|\n")
    centre = next((t["v"] for t in d["tiles"] if t["k"].lower().startswith("centre")), "")
    with open(idx, "a", encoding="utf-8", newline="\n") as f:
        f.write("| %s | [%s](%s) | %s | _(fill in)_ |\n"
                % (human, os.path.basename(outfile), os.path.basename(outfile), centre))

    print("report:", outfile)
    print("index :", idx)


if __name__ == "__main__":
    main()
