# Submission of 3A8 to the LEAP AI Assets Marketplace — the letter and the pre-send check

Prepared 2026-09-16, after the end-to-end test of the packaged instrument (`examples/FaxRxTx/run61_e2e_test.md`).
The author sends the mail; nothing here is sent by the repository or its tools. Procedure and layout rules:
`docs/leap-marketplace.md` §2.4.

## Pre-send check

- [ ] `git push epam main` done and `git rev-parse epam/main` equals `origin/main` (both at the commit that carries this file).
- [ ] https://git.epam.com/gennadiy_serdyuk/3A8 → Settings → General → Visibility is **Internal** (the crawler cannot read Private).
- [ ] `PYTHONUTF8=1 py tools/check_frontmatter.py` passes (skills, agents, FACTORY.md frontmatter).
- [ ] The two folder URLs below open in a browser while signed in to git.epam.com.

## The letter

**To:** SpecialEPM-EASEFeedback@epam.com
**Subject:** AI Assets Marketplace submission — 3A8 (TriAngulEight), a software estimation factory and its four entry-point skills

Hello,

I would like to submit one factory and four skills to the AI Assets Marketplace.

```
factories: https://git.epam.com/gennadiy_serdyuk/3A8/-/tree/main/factories
skills:    https://git.epam.com/gennadiy_serdyuk/3A8/-/tree/main/skills
owner:     Gennadiy Serdyuk
```

**What it is.** 3A8 is a software effort estimation instrument packaged as a Claude Code plugin (release 0.2.0).
It runs a bottom-up chain of three isolated sensors (product model → work model → size classes, priced from a
pinned table of external norms), a reference-class reading taken blind to the chain, a gap-blind calibration round
and a diagnosis that explains the divergence between the methods instead of averaging it. The output is an estimate
document and an HTML report: centre, corridor, reserve, and every number traced to the sensor run that produced it.
The catalogue has no factory on effort estimation today.

**Entry points** (the skills submitted): `/3a8:estimate` — the whole instrument; `/3a8:estimate-product` — the
bottom-up half; `/3a8:estimate-reference-class` — the outside view; `/3a8:estimate-wbs` — a quick one-sensor
reading. The twelve agents in `agents/` are internal sensors of the factory and are deliberately not submitted as
separate assets: each is defined by what it must not see (`PIPELINE.md`), and outside the entry points they do not
form a method.

**Support level:** Self-Serve. **SDLC phase:** Planning & Analysis.

**Proven On.** One real project with a documented outcome (FaxRxTx, a fax back-end of 2007–2009, 120 staffed
person-months): estimated with the outcome sealed, calibrated centre within ×1.3 of the actual; re-estimated on
2026-09-16 by the packaged plugin alone from the pinned inputs to the report, 22 sensor launches, 46 minutes, raw
chain 0.73 × and calibrated centre 1.26 × the actual. Two further worked cases (a training RFP and a real RFP kept
outside the public repository) have no outcome. I would rate this L2; please set the level as your criteria
prescribe.

**Licence and hosting.** Apache 2.0, copyright Gennadiy Serdyuk. The canonical repository is
https://github.com/gserdyuk/3A8; the git.epam.com project is a mirror refreshed on demand for the crawler.

Thank you,
Gennadiy Serdyuk
gennadiy_serdyuk@epam.com

## After it is published

- Check the card at https://leap.epam.com/hyperfactory/ai-assets-marketplace; the repository is re-crawled on every
  `git push epam main`, no resubmission needed.
- Record the publication date and the assigned Proven On level in `docs/leap-marketplace.md` §2.5.
