# 3A8 → EPAM LEAP AI Assets Marketplace

Working note. Written 2026-09-11 after reviewing the LEAP portal
(https://leap.epam.com) and its asset submission guide; updated 2026-09-13 and 2026-09-16.
Decision 2026-09-16, after the end-to-end test of the packaged instrument: **submitting.**
The letter and the pre-send check: `docs/leap_submission_2026-09-16.md`.

## 1. To do before submission

- [x] **Agents to the repository root — the repo is now a Claude Code plugin**
      (done 2026-09-13). `.claude-plugin/plugin.json` + `marketplace.json` in
      the root; the 12 agents moved from `.claude/agents/` to a flat `agents/`.
      Claude Code (plugin) and the marketplace crawler read the same folder,
      so there is no second copy and no sync script. Agents register as
      `3a8:<name>`. Use: `claude --plugin-dir .` inside a clone, or
      `/plugin marketplace add gserdyuk/3A8` + `/plugin install 3a8@3a8`
      anywhere. Verified with `claude --plugin-dir . plugin details 3a8`:
      12 agents listed. Living docs (PIPELINE.md, docs/instrument.md,
      rate_table.md, status, fp_counting_rules) point to `agents/`; session
      records, facts, archive and run transcripts keep the old path as history.
      Precedent: CodeMie sdlc-factory uses exactly this layout.
- [x] **Agent frontmatter.** (done 2026-09-13; one description had an unquoted colon, now quoted) Add `author: "Gennadiy Serdyuk <gserdyuk@gmail.com>"`
      to all 12 files. Today they carry only `name`, `description`, `tools`.
      Email decision: one address per field, never two. Skills and agents
      are reused outside EPAM, so they carry the git identity (gmail). The
      EPAM address goes into `FACTORY.md` `authors` only (see 2.3): that is
      the file the marketplace card is built from. The crawler does not
      validate the domain, and published assets exist with no email at all.
- [x] **Maintainer line in README.** One human-readable line with both
      addresses, e.g. `Maintainer: Gennadiy Serdyuk <gserdyuk@gmail.com>
      (at EPAM: gennadiy_serdyuk@epam.com)`. No parser touches it. If some
      commits are ever made with the EPAM address, add a `.mailmap` so
      `git log` and GitHub show one person.
- [x] **LICENSE.** (done 2026-09-13, Apache 2.0) The repository has none. Choose one (twotakt uses
      Apache 2.0) and add it before the EPAM GitLab copy is refreshed.
- [x] **Package as a factory.** (done 2026-09-13 as `factories/3a8/FACTORY.md`; **moved to the repository root, `FACTORY.md`, on 2026-09-17** at the LEAP team's request — see 2.4) Create `factories/3a8/FACTORY.md` (template
      in 2.3). Key fields: `sdlc_phase: Planning & Analysis`,
      `support_level: Self-Serve`. Use cases:
      - Effort estimation from an RFP or a requirement list
      - Diagnosing divergence between estimation methods
      - Calibration on completed projects with known outcomes
- [x] **State the isolation discipline.** (done 2026-09-13, section in FACTORY.md) In the FACTORY.md body say
      explicitly that the agents are not a pick-and-mix set: who may see what
      is defined by `PIPELINE.md`, and the run order by `docs/instrument.md`.
      Otherwise the catalog presents 12 agents "to choose from" and the
      method breaks.
- [x] **Hide internal agents — resolved by the flat layout.** The crawler
      registers agents only from `agents/<name>/`; flat `agents/<name>.md`
      files are not picked up as separate assets (CodeMie's seven agents are
      absent from the Agents tab for this reason). Only the factory goes to
      the catalog, which is what the isolation discipline wants. No
      `discoverable: false` needed.
- [x] **Validate YAML** (done 2026-09-13, `tools/check_frontmatter.py`, run with `PYTHONUTF8=1 py tools/check_frontmatter.py`) of every frontmatter block with `yaml.safe_load()`.
- [x] **Folder names** — letters, digits, `-`, `_` only.
- [x] **Entry points as skills** (done 2026-09-14). `skills/estimate-product`,
      `estimate-reference-class`, `estimate-wbs`, `estimate`: the orchestrator's
      run order per method, invoked as `/3a8:<name>`. These are the public
      surface of the factory and the assets the catalog lists individually.

## 2. Getting the project into EPAM GitLab and the LEAP Marketplace

Portal: https://leap.epam.com → HyperFactory → AI Assets Marketplace.
Guide: https://leap.epam.com/sp/ai-marketplace/contribute.

### 2.1. Hosting scheme (precedent: arozumenko/sdlc-skills)

The canonical repository stays on personal GitHub under its own license.
The EPAM GitLab copy exists only for the marketplace crawler. Artem Rozumenko
does exactly this: 4 catalog factories, `install_script` in FACTORY.md points
to `npx github:arozumenko/sdlc-skills`, and the catalog accepts it.

Half of the catalog's factories (19 of 38) live in personal namespaces of the
form `git.epam.com/<name_surname>/<repo>`; no team or practice is required.

### 2.2. EPAM GitLab copy (done 2026-09-13)

Project: https://git.epam.com/gennadiy_serdyuk/3A8 — created by importing
from GitHub. Import is one-off; it keeps no link to the source.

**Chosen sync method: a separate remote `epam`, pushed on demand.**
Pull mirroring (Settings → Repository → Mirroring, direction Pull) is not
available on git.epam.com (no Premium). A second push URL on origin and
GitHub Actions mirroring were rejected as less controllable.

The remote is already in `.git/config` (repeat on another machine):

```bash
git remote add epam https://git.epam.com/gennadiy_serdyuk/3A8.git
```

Refresh the EPAM copy when the state is ready to be seen:

```bash
git push epam main
```

- `git push` / `git pull` without a remote name still go to GitHub only.
- HTTPS push needs a Personal Access Token (scope `write_repository`); the
  SSO password does not work. Credential Manager remembers it after the
  first use.
- If `main` on GitLab is protected against force-push and history on GitHub
  was rewritten, the push is rejected: relax it in Settings → Repository →
  Protected branches, or do not rewrite `main`.
- Check the project Visibility is **Internal**: the crawler cannot see
  Private.
- The marketplace crawler re-reads the repository after every push.

### 2.3. Crawler layout requirements

- `skills/<name>/SKILL.md` — one skill per folder.
- `agents/<name>/agent.md` (or `<name>.md`, `<name>.agent.md`) — one agent
  per folder.
- `factories/<name>/FACTORY.md` — file name strictly uppercase. **The file sits in the root of the
  directory that is the factory.** A repository that holds several factories uses `factories/<name>/`;
  a repository that *is* one factory, as this one, carries `FACTORY.md` in its root, and the `skills/`
  beside it are read as part of that factory, not as standalone skills (LEAP team, 2026-09-17).
- Folder name = asset identifier: letters, digits, `-`, `_` only.
- Skill and agent frontmatter: `name`, `description`,
  `author: "Name <email>"`. The guide says email is required; in practice
  assets are published with no email and even with no `author` field at all
  (team-skills, epm-ease/agent-skills). The domain is not checked.
- Keep something out of the catalog: `discoverable: false` in its frontmatter.

FACTORY.md template. Any value containing a colon must be quoted, otherwise
the YAML breaks silently and the asset simply never appears:

```yaml
---
name: 3A8 — TriAngulEight
description: "Software estimation factory: four isolated sensors plus a reference class, divergence diagnosed, range with explained residual."
owner: Gennadiy Serdyuk
authors:
  - "Gennadiy Serdyuk <gennadiy_serdyuk@epam.com>"
install_script: "git clone https://github.com/gserdyuk/3A8.git"
install_script_unix: "git clone https://github.com/gserdyuk/3A8.git"
sdlc_phase: Planning & Analysis
support_level: Self-Serve
use_cases:
  - Effort estimation from an RFP or a requirement list
  - Diagnosing divergence between estimation methods
  - Calibration on completed projects with known outcomes
---
# 3A8 — TriAngulEight
<markdown: what it does, how to run, limits, link to PIPELINE.md>
```

`support_level` is strictly one of `Self-Serve`, `Best Effort Support`,
`Dedicated Capacity`. `sdlc_phase` is a single value, not a list. Omit
`project_deployments` if there is nothing to put there.

### 2.4. Submitting

Email to SpecialEPM-EASEFeedback@epam.com, one folder URL per asset type
plus the owner:

```
factory: https://git.epam.com/gennadiy_serdyuk/3A8   (FACTORY.md in the repository root)
owner:   Gennadiy Serdyuk
```

Submitted 2026-09-16 with two URLs (`factories/`, `skills/`). On 2026-09-17 the LEAP team (Dima) asked
whether the skills belong to the factory rather than stand alone, and said that by their processing rules
`FACTORY.md` belongs in the root of the directory where the factory lives — here, the repository root.
Answer: yes, the four skills are the factory's entry points; `FACTORY.md` moved to the root the same day.
The letter and the reply: `docs/leap_submission_2026-09-16.md`.

One asset is submitted: the factory, with the four entry-point skills (`skills/estimate*`) as its parts.
The agents are deliberately not submitted as separate assets (see checklist
item on hiding internal agents): they are internal sensors that only make sense
inside an entry point.

Published within a few working days. After that the repository is
re-crawled automatically on every push; no resubmission needed. Check it
appeared at https://leap.epam.com/hyperfactory/ai-assets-marketplace.

### 2.5. Decide before submitting

- Ownership and license — **settled by the author, 2026-09-16:** the copyright holder is Gennadiy
  Serdyuk <gserdyuk@gmail.com>, stated in `LICENSE` (Apache 2.0 appendix) and `NOTICE`. The GitHub
  repository is canonical; the EPAM GitLab copy is a mirror under the same license, not a transfer.
  The `authors` line of FACTORY.md carries the epam.com address so that the catalogue card links to
  the author as an employee; it does not change who owns the work. Whether EPAM's own IP policy has a
  view on this is a question the author puts to EPAM, not one the repository can settle.
- `owner`: personal name or EPM-UASP.
- "Proven On" (L2/L3) is filled for only 8 of 38 factories; FaxRxTx as the
  one validated case honestly rates L2. **Approved by the author 2026-09-16:** the letter
  claims L2 on FaxRxTx (outcome sealed, calibrated centre within ×1.3; re-estimated by the
  packaged plugin alone the same day) and leaves the level to the catalogue's criteria.
- The niche is empty: the catalog has no factory about effort estimation.
