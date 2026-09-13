# 3A8 → EPAM LEAP AI Assets Marketplace

Working note. Written 2026-09-11 after reviewing the LEAP portal
(https://leap.epam.com) and its asset submission guide; updated 2026-09-13.
Decision as of today: **not submitting yet**, but bring the repository to the
expected layout in advance.

## 1. To do before submission

- [ ] **Agents to the repository root.** The crawler looks for
      `agents/<name>/agent.md`; the 12 agents of 3A8 live in
      `.claude/agents/*.md`. Make `agents/` the canonical location, one folder
      per agent (`agents/diagnostician/agent.md`, etc.), and keep
      `.claude/agents/` for Claude Code. Symlinks are unreliable on Windows;
      simpler to keep copies plus a small sync script in `tools/`, or move
      them and point `.claude/settings.json` at the new path.
- [ ] **Agent frontmatter.** Add `author: "Gennadiy Serdyuk <gserdyuk@gmail.com>"`
      to all 12 files. Today they carry only `name`, `description`, `tools`.
      Email decision: one address per field, never two. Skills and agents
      are reused outside EPAM, so they carry the git identity (gmail). The
      EPAM address goes into `FACTORY.md` `authors` only (see 2.3): that is
      the file the marketplace card is built from. The crawler does not
      validate the domain, and published assets exist with no email at all.
- [ ] **Maintainer line in README.** One human-readable line with both
      addresses, e.g. `Maintainer: Gennadiy Serdyuk <gserdyuk@gmail.com>
      (at EPAM: gennadiy_serdyuk@epam.com)`. No parser touches it. If some
      commits are ever made with the EPAM address, add a `.mailmap` so
      `git log` and GitHub show one person.
- [ ] **LICENSE.** The repository has none. Choose one (twotakt uses
      Apache 2.0) and add it before the EPAM GitLab copy is refreshed.
- [ ] **Package as a factory.** Create `factories/3a8/FACTORY.md` (template
      in 2.3). Key fields: `sdlc_phase: Planning & Analysis`,
      `support_level: Self-Serve`. Use cases:
      - Effort estimation from an RFP or a requirement list
      - Diagnosing divergence between estimation methods
      - Calibration on completed projects with known outcomes
- [ ] **State the isolation discipline.** In the FACTORY.md body say
      explicitly that the agents are not a pick-and-mix set: who may see what
      is defined by `PIPELINE.md`, and the run order by `docs/instrument.md`.
      Otherwise the catalog presents 12 agents "to choose from" and the
      method breaks.
- [ ] **Hide internal agents.** For agents not meant for outside use (e.g.
      `version-probe`) set `discoverable: false` in the frontmatter.
- [ ] **Validate YAML** of every frontmatter block with `yaml.safe_load()`.
- [ ] **Folder names** — letters, digits, `-`, `_` only.

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
- `factories/<name>/FACTORY.md` — file name strictly uppercase.
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
agents:    https://git.epam.com/gennadiy_serdyuk/3A8/-/tree/main/agents
factories: https://git.epam.com/gennadiy_serdyuk/3A8/-/tree/main/factories
owner:     Gennadiy Serdyuk
```

Published within a few working days. After that the repository is
re-crawled automatically on every push; no resubmission needed. Check it
appeared at https://leap.epam.com/hyperfactory/ai-assets-marketplace.

### 2.5. Decide before submitting

- Ownership and license: a copy on EPAM GitLab with an EPAM author makes the
  asset an internal corporate one. The license must allow that.
- `owner`: personal name or EPM-UASP.
- "Proven On" (L2/L3) is filled for only 8 of 38 factories; FaxRxTx as the
  one validated case honestly rates L2.
- The niche is empty: the catalog has no factory about effort estimation.
