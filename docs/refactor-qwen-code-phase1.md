# Documentation Refactor: Phase 1 - Qwen Code Migration

## Overview

This document details the migration of 5 critical priority documentation files from Claude Code branding to Qwen Code branding. Phase 1 focuses on high-impact user-facing guides that define core workflows: skill development, skill placement, token optimization, troubleshooting, and architecture improvements.

**Target Repository:** `mowgliph/everything-qwen-code`

---

## Files in Scope

| # | File | Current State | Required Changes | Effort |
|---|------|---------------|------------------|--------|
| 1 | `docs/SKILL-DEVELOPMENT-GUIDE.md` | Heavy Claude Code references throughout; ~800 lines | Replace all Claude Code → Qwen Code, ~/.claude/ → ~/.qwen/, update repo references, fix code examples | High (2-3 hours) |
| 2 | `docs/SKILL-PLACEMENT-POLICY.md` | Multiple ~/.claude/ paths, Claude Code terminology | Replace paths, update policy language, fix validator references | Medium (1 hour) |
| 3 | `docs/token-optimization.md` | Settings paths, environment variables, model names | Replace paths, env var prefixes, update model guidance | Medium (1 hour) |
| 4 | `docs/TROUBLESHOOTING.md` | Issue links, hook examples, Claude Code bug references | Update issue links, generalize bug descriptions, fix examples | Low (30 min) |
| 5 | `docs/ARCHITECTURE-IMPROVEMENTS.md` | Project name references, agent counts, catalog paths | Update project name, verify counts, fix path references | Medium (1 hour) |

---

## Detailed Change Plan

### File 1: `docs/SKILL-DEVELOPMENT-GUIDE.md`

**Current Issues:**
- "Claude Code" appears ~40 times
- "~/.claude/" path in testing section
- "affaan-m/everything-claude-code" repo reference
- "CLAUDE_CODE_" environment variables in examples

#### Section-by-Section Changes

##### 1.1 Header and Introduction (Lines 1-25)

**Search/Replace:**
```
Search: "Everything Claude Code (ECC)"
Replace: "Everything Qwen Code (EQC)"

Search: "Claude Code"
Replace: "Qwen Code"
```

**Manual Review:**
- Update "ECC" acronym to "EQC" throughout (or keep "ECC" if retaining brand continuity - decision needed)
- Verify table "Skill vs Agent vs Command" still accurate for Qwen Code

##### 1.2 Skill Architecture Section (Lines 45-80)

**Search/Replace:**
```
Search: "~/.claude/skills/"
Replace: "~/.qwen/skills/"

Search: "SKILL.md Format"
Replace: "SKILL.md Format" (no change, but verify Qwen Code uses same format)
```

**Code Block Update (Line ~65):**
```yaml
# OLD
name: skill-name
description: Brief description shown in skill list and used for auto-activation
origin: ECC

# NEW (no change needed - format is identical)
name: skill-name
description: Brief description shown in skill list and used for auto-activation
origin: EQC
```

##### 1.3 Testing Your Skill Section (Lines 380-430)

**CRITICAL - Multiple path changes:**

```bash
# OLD (Lines ~385-390)
cp -r skills/your-skill-name ~/.claude/skills/

# NEW
cp -r skills/your-skill-name ~/.qwen/skills/
```

```bash
# OLD (Lines ~393-395)
gh repo fork affaan-m/everything-claude-code --clone
cd everything-claude-code

# NEW
gh repo fork mowgliph/everything-qwen-code --clone
cd everything-qwen-code
```

##### 1.4 Submitting Your Skill Section (Lines 435-480)

**Search/Replace:**
```
Search: "affaan-m/everything-claude-code"
Replace: "mowgliph/everything-qwen-code"

Search: "everything-claude-code"
Replace: "everything-qwen-code"
```

**PR Template Update:**
```markdown
# OLD
## Summary
Brief description of the skill and why it's valuable.

# NEW (no structural change, but update repo name in instructions)
```

##### 1.5 Additional Resources Section (Lines 550-560)

**Search/Replace:**
```
Search: "../CONTRIBUTING.md"
Replace: "../CONTRIBUTING.md" (verify file exists)

Search: "../skills/"
Replace: "../skills/" (verify paths are correct)
```

#### Verification Checklist for File 1

```bash
# After changes, verify no Claude references remain
grep -i "claude" docs/SKILL-DEVELOPMENT-GUIDE.md
# Expected: 0 results (or only in historical context if any)

# Verify Qwen Code references are correct
grep -i "qwen" docs/SKILL-DEVELOPMENT-GUIDE.md
# Expected: Multiple results

# Verify paths are updated
grep "\.qwen/" docs/SKILL-DEVELOPMENT-GUIDE.md
# Expected: At least 2-3 results

# Verify repo reference
grep "mowgliph/everything-qwen-code" docs/SKILL-DEVELOPMENT-GUIDE.md
# Expected: At least 1 result
```

---

### File 2: `docs/SKILL-PLACEMENT-POLICY.md`

**Current Issues:**
- "~/.claude/" paths in policy table and sections
- "CLAUDE_CODE_" environment variable references

#### Section-by-Section Changes

##### 2.1 Skill Types Table (Lines 5-15)

**Search/Replace:**
```
# OLD (Lines ~7-11)
| Learned | `~/.claude/skills/learned/` | No | Required |
| Imported | `~/.claude/skills/imported/` | No | Required |
| Evolved | `~/.claude/homunculus/evolved/skills/` | No | Inherits |

# NEW
| Learned | `~/.qwen/skills/learned/` | No | Required |
| Imported | `~/.qwen/skills/imported/` | No | Required |
| Evolved | `~/.qwen/homunculus/evolved/skills/` | No | Inherits |
```

##### 2.2 Learned Skills Section (Lines 25-35)

**Search/Replace:**
```
# OLD (Line ~27)
Location: `~/.claude/skills/learned/<skill-name>`.

# NEW
Location: `~/.qwen/skills/learned/<skill-name>`.

# OLD (Line ~30)
Default path is configurable via `skills/continuous-learning/config.json` → `learned_skills_path`.

# NEW (verify config path is correct for Qwen Code)
Default path is configurable via `skills/continuous-learning/config.json` → `learned_skills_path`.
```

##### 2.3 Imported Skills Section (Lines 37-45)

**Search/Replace:**
```
# OLD (Line ~39)
Location: `~/.claude/skills/imported/<skill-name>`.

# NEW
Location: `~/.qwen/skills/imported/<skill-name>`.
```

##### 2.4 Evolved Skills Section (Lines 47-55)

**Search/Replace:**
```
# OLD (Line ~49)
Location: `~/.claude/homunculus/evolved/skills/` (global) or `~/.claude/homunculus/projects/<hash>/evolved/skills/` (per-project).

# NEW
Location: `~/.qwen/homunculus/evolved/skills/` (global) or `~/.qwen/homunculus/projects/<hash>/evolved/skills/` (per-project).
```

##### 2.5 Validator Behavior Section (Lines 65-85)

**Manual Review Required:**
- Verify `validate-skills.js` path is correct for Qwen Code
- Verify `validate-install-manifests.js` behavior matches
- Check if script paths need updating

```
# OLD (Line ~68)
Scope: Curated skills only (`skills/` in repo).

# NEW (no change - logic is the same)
```

#### Verification Checklist for File 2

```bash
# Verify no ~/.claude/ paths remain
grep "\~/.claude/" docs/SKILL-PLACEMENT-POLICY.md
# Expected: 0 results

# Verify ~/.qwen/ paths are correct
grep "\~/.qwen/" docs/SKILL-PLACEMENT-POLICY.md
# Expected: At least 4-5 results

# Verify table formatting
grep -A 5 "| Type |" docs/SKILL-PLACEMENT-POLICY.md
# Expected: Table with correct paths
```

---

### File 3: `docs/token-optimization.md`

**Current Issues:**
- "~/.claude/settings.json" path
- "CLAUDE_CODE_" environment variables
- "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE" variable
- Model names (Sonnet, Opus, Haiku) - verify if these apply to Qwen Code

#### Section-by-Section Changes

##### 3.1 Recommended Settings Section (Lines 5-25)

**CRITICAL - Environment Variable Changes:**

```json
# OLD (Lines ~10-16)
Add to your `~/.claude/settings.json`:

```json
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_CODE_SUBAGENT_MODEL": "haiku"
  }
}
```

# NEW (update path and env var prefix)
Add to your `~/.qwen/settings.json`:

```json
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "QWEN_CODE_SUBAGENT_MODEL": "haiku"
  }
}
```
```

**Manual Review Required:**
- Verify if Qwen Code uses same model names (Sonnet/Opus/Haiku are Anthropic models)
- If Qwen Code uses different models, update the entire "Model Selection" section
- If Qwen Code doesn't support these models, replace with appropriate alternatives

##### 3.2 Settings Table (Lines 18-25)

**Search/Replace:**
```
# OLD
| Setting | Default | Recommended | Effect |
|---------|---------|-------------|--------|
| `model` | opus | **sonnet** | Sonnet handles ~80% of coding tasks well. |
| `MAX_THINKING_TOKENS` | 31,999 | **10,000** | Extended thinking reserves up to 31,999 output tokens |
| `CLAUDE_CODE_SUBAGENT_MODEL` | _(inherits main)_ | **haiku** | Subagents run on this model. |

# NEW (update env var name, verify model applicability)
| Setting | Default | Recommended | Effect |
|---------|---------|-------------|--------|
| `model` | _(varies)_ | **sonnet** | Sonnet handles ~80% of coding tasks well. |
| `MAX_THINKING_TOKENS` | 31,999 | **10,000** | Extended thinking reserves up to 31,999 output tokens |
| `QWEN_CODE_SUBAGENT_MODEL` | _(inherits main)_ | **haiku** | Subagents run on this model. |
```

##### 3.3 Community Note (Lines 27-32)

**Search/Replace:**
```
# OLD
Some recent Claude Code builds have community reports that `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`...

# NEW
Some recent Qwen Code builds have community reports that `QWEN_AUTOCOMPACT_PCT_OVERRIDE`...
```

**Cross-Reference Update:**
```
# OLD
See [Troubleshooting](./TROUBLESHOOTING.md).

# NEW (no change - file reference is correct)
```

##### 3.4 Toggling Extended Thinking (Lines 34-38)

**Manual Review Required:**
- Verify if Qwen Code has same keyboard shortcuts
- If different, update the shortcuts

```
# OLD
- **Alt+T** (Windows/Linux) or **Option+T** (macOS) — toggle on/off
- **Ctrl+O** — see thinking output (verbose mode)

# NEW (verify these are correct for Qwen Code)
```

##### 3.5 Model Selection Section (Lines 40-55)

**CRITICAL - Model Names:**

```
# OLD
| Model | Best for | Cost |
|-------|----------|------|
| **Haiku** | Subagent exploration, file reading, simple lookups | Lowest |
| **Sonnet** | Day-to-day coding, reviews, test writing, implementation | Medium |
| **Opus** | Complex architecture, multi-step reasoning, debugging subtle issues | Highest |

# NEW - OPTION A (if Qwen Code uses Anthropic models via API)
Same as above (no change needed)

# NEW - OPTION B (if Qwen Code uses different models)
| Model | Best for | Cost |
|-------|----------|------|
| **Qwen-Max** | Complex architecture, multi-step reasoning | Highest |
| **Qwen-Plus** | Day-to-day coding, reviews, test writing | Medium |
| **Qwen-Turbo** | Quick lookups, file reading | Lowest |
```

**Decision Required:** Determine which models Qwen Code supports and update accordingly.

##### 3.6 Commands Section (Lines 60-70)

**Search/Replace:**
```
# OLD
| Command | When to use |
|---------|-------------|
| `/clear` | Between unrelated tasks. |
| `/compact` | At logical task breakpoints. |
| `/cost` | Check token spending for the current session. |

# NEW (verify commands exist in Qwen Code)
Same structure if commands are identical
```

##### 3.7 MCP Server Management (Lines 80-95)

**Search/Replace:**
```
# OLD (Line ~85)
Tips:
- Run `/mcp` to see active servers and their context cost

# NEW (verify /mcp command exists)
Same if command exists
```

##### 3.8 Agent Teams Cost Warning (Lines 97-110)

**Search/Replace:**
```
# OLD
[Agent Teams](https://code.claude.com/docs/en/agent-teams) (experimental) spawns multiple independent context windows.

# NEW (update link if Qwen Code has different docs)
[Agent Teams](https://code.qwen.com/docs/en/agent-teams) (experimental) spawns multiple independent context windows.
```

```
# OLD
Enable with: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings

# NEW
Enable with: `QWEN_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings
```

##### 3.9 Quick Reference (Lines 120-135)

**Search/Replace:**
```bash
# OLD
# Daily workflow
/model sonnet              # Start here
/model opus                # Only for complex reasoning
/clear                     # Between unrelated tasks
/compact                   # At logical breakpoints
/cost                      # Check spending

# Environment variables (add to ~/.claude/settings.json "env" block)
MAX_THINKING_TOKENS=10000
CLAUDE_CODE_SUBAGENT_MODEL=haiku
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# NEW
# Daily workflow
/model sonnet              # Start here
/model opus                # Only for complex reasoning
/clear                     # Between unrelated tasks
/compact                   # At logical breakpoints
/cost                      # Check spending

# Environment variables (add to ~/.qwen/settings.json "env" block)
MAX_THINKING_TOKENS=10000
QWEN_CODE_SUBAGENT_MODEL=haiku
QWEN_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

#### Verification Checklist for File 3

```bash
# Verify no CLAUDE_CODE_ env vars remain
grep "CLAUDE_CODE_" docs/token-optimization.md
# Expected: 0 results

# Verify QWEN_CODE_ env vars are present
grep "QWEN_CODE_" docs/token-optimization.md
# Expected: At least 2-3 results

# Verify settings path
grep "\.qwen/settings\.json" docs/token-optimization.md
# Expected: At least 2 results

# Verify model names are appropriate (manual check)
grep -E "Haiku|Sonnet|Opus|Qwen" docs/token-optimization.md
# Expected: Appropriate models for Qwen Code
```

---

### File 4: `docs/TROUBLESHOOTING.md`

**Current Issues:**
- Issue link to old repo
- "Claude Code" bug references
- Hook examples may need updating

#### Section-by-Section Changes

##### 4.1 Header and Introduction (Lines 1-10)

**Search/Replace:**
```
# OLD
Community-reported workarounds for current Claude Code bugs that can affect ECC users.

These are upstream Claude Code behaviors, not ECC bugs. The entries below summarize the production-tested workarounds collected in [issue #644](https://github.com/affaan-m/everything-claude-code/issues/644) on Claude Code `v2.1.79` (macOS, heavy hook usage, MCP connectors enabled).

# NEW
Community-reported workarounds for current Qwen Code bugs that can affect EQC users.

These are upstream Qwen Code behaviors, not EQC bugs. The entries below summarize the production-tested workarounds collected in [issue #XXX](https://github.com/mowgliph/everything-qwen-code/issues/XXX) on Qwen Code `vX.X.X` (macOS, heavy hook usage, MCP connectors enabled).
```

**Decision Required:** 
- Create new issue in mowgliph/everything-qwen-code repo for tracking Qwen Code bugs
- Update issue number and version accordingly

##### 4.2 False "Hook Error" Section (Lines 12-35)

**Manual Review:**
- Verify hook behavior is the same in Qwen Code
- Exit codes should be universal (0=allow, 2=block)

```bash
# OLD (Lines ~25-28)
# Good: block with stderr message and exit 2
input=$(cat)
echo "[BLOCKED] Reason here" >&2
exit 2

# NEW (no change - exit codes are standard)
```

##### 4.3 Compaction Section (Lines 37-50)

**Search/Replace:**
```
# OLD
On some current Claude Code builds, lower values may reduce the compaction threshold instead of extending it.

# NEW
On some current Qwen Code builds, lower values may reduce the compaction threshold instead of extending it.
```

##### 4.4 MCP Connectors Section (Lines 52-65)

**Manual Review:**
- Verify MCP connector behavior is the same
- "PostCompact" hook name should be verified

```
# OLD
If your Claude Code build supports it, add a `PostCompact` reminder hook that warns you to re-check connector auth after compaction.

# NEW
If your Qwen Code build supports it, add a `PostCompact` reminder hook that warns you to re-check connector auth after compaction.
```

##### 4.5 Hook Edits Section (Lines 67-80)

**Search/Replace:**
```
# OLD
- Restart the Claude Code session after changing hooks.

# NEW
- Restart the Qwen Code session after changing hooks.
```

##### 4.6 529 Overloaded Section (Lines 82-100)

**Search/Replace:**
```
# OLD
Symptoms: Claude Code starts failing under high hook/tool/context pressure.

# NEW
Symptoms: Qwen Code starts failing under high hook/tool/context pressure.
```

```bash
# OLD
Route subagent work to a cheaper model such as `CLAUDE_CODE_SUBAGENT_MODEL=haiku` if your setup exposes that knob.

# NEW
Route subagent work to a cheaper model such as `QWEN_CODE_SUBAGENT_MODEL=haiku` if your setup exposes that knob.
```

##### 4.7 Related ECC Docs Section (Lines 102-110)

**Search/Replace:**
```
# OLD
- [hooks/README.md](../hooks/README.md) for ECC's documented hook lifecycle and exit-code behavior.
- [token-optimization.md](./token-optimization.md) for cost and context management settings.
- [issue #644](https://github.com/affaan-m/everything-claude-code/issues/644) for the original report and tested environment.

# NEW
- [hooks/README.md](../hooks/README.md) for EQC's documented hook lifecycle and exit-code behavior.
- [token-optimization.md](./token-optimization.md) for cost and context management settings.
- [issue #XXX](https://github.com/mowgliph/everything-qwen-code/issues/XXX) for the original report and tested environment.
```

#### Verification Checklist for File 4

```bash
# Verify no affaan-m repo links remain
grep "affaan-m" docs/TROUBLESHOOTING.md
# Expected: 0 results

# Verify mowgliph repo links are present
grep "mowgliph" docs/TROUBLESHOOTING.md
# Expected: At least 1-2 results

# Verify Claude Code references updated
grep -i "claude code" docs/TROUBLESHOOTING.md
# Expected: 0 results (case-insensitive)

# Verify Qwen Code references are present
grep -i "qwen code" docs/TROUBLESHOOTING.md
# Expected: Multiple results
```

---

### File 5: `docs/ARCHITECTURE-IMPROVEMENTS.md`

**Current Issues:**
- "Everything Claude Code (ECC)" project name
- Agent/skill/command counts may be outdated
- Cross-harness references (.agents/, .cursor/)

#### Section-by-Section Changes

##### 5.1 Header (Lines 1-5)

**Search/Replace:**
```
# OLD
# Architecture Improvement Recommendations

This document captures architect-level improvements for the Everything Claude Code (ECC) project. It is written from the perspective of a Claude Code coding architect aiming to improve maintainability, consistency, and long-term quality.

# NEW
# Architecture Improvement Recommendations

This document captures architect-level improvements for the Everything Qwen Code (EQC) project. It is written from the perspective of a Qwen Code coding architect aiming to improve maintainability, consistency, and long-term quality.
```

##### 5.2 Agent/Command/Skill Count Sync (Lines 8-25)

**Search/Replace:**
```
# OLD (Line ~10)
**Issue:** AGENTS.md states "13 specialized agents, 50+ skills, 33 commands" while the repo has **16 agents**, **65+ skills**, and **40 commands**.

# NEW (update with current counts from Qwen Code repo)
**Issue:** AGENTS.md states "X specialized agents, Y+ skills, Z commands" while the repo has **A agents**, **B+ skills**, and **C commands**.
```

**Manual Review Required:**
- Count actual agents in `agents/` directory
- Count actual skills in `skills/` directory
- Count actual commands in `commands/` directory
- Update both the stated and actual counts

```bash
# Get current counts
ls -1 agents/*.md | wc -l  # Agent count
ls -1d skills/*/ | wc -l  # Skill count
ls -1 commands/*.md | wc -l  # Command count
```

##### 5.3 Command → Agent/Skill Map (Lines 27-40)

**Search/Replace:**
```
# OLD
- Expose a "map" in docs (e.g. `docs/COMMAND-AGENT-MAP.md`) or in the generated catalog for discoverability and for tooling (e.g. "which commands use tdd-guide?").

# NEW (no change - recommendation is still valid)
```

##### 5.4 Test Discovery Section (Lines 50-65)

**Manual Review:**
- Verify `tests/run-all.js` still uses hardcoded list
- If already fixed, update the issue status

```
# OLD
**Issue:** `tests/run-all.js` uses a **hardcoded list** of test files.

# NEW (update if already fixed, otherwise keep)
```

##### 5.5 Cross-Harness Section (Lines 95-110)

**Search/Replace:**
```
# OLD
### 4.1 Skill/Agent Subset Sync (.agents/skills, .cursor/skills)

**Issue:** `.agents/skills/` (Codex) and `.cursor/skills/` are subsets of `skills/`.

# NEW (update for Qwen Code - verify if these directories exist)
### 4.1 Skill/Agent Subset Sync (.agents/skills, .cursor/skills)

**Issue:** `.agents/skills/` (Codex) and `.cursor/skills/` are subsets of `skills/`.
```

**Decision Required:**
- Verify if `.agents/` and `.cursor/` directories exist in Qwen Code repo
- If not, remove this section or update with relevant cross-harness info

##### 5.6 Translation Drift Section (Lines 112-125)

**Manual Review:**
- Verify if `docs/` has `zh-CN/`, `zh-TW/`, `ja-JP/` subdirectories
- If translations don't exist, update or remove this section

```bash
# Check for translation directories
ls -la docs/ | grep -E "zh|ja"
```

##### 5.7 Summary Table (Lines 135-150)

**Search/Replace:**
```
# OLD
| Area              | Improvement                          | Priority | Effort  |
|-------------------|--------------------------------------|----------|---------|
| Doc sync          | Sync AGENTS.md/README counts & table | High     | Low     |
| Single source     | Catalog script or manifest           | High     | Medium  |

# NEW (no structural change - update if any items are already completed)
```

##### 5.8 Quick Wins Section (Lines 152-165)

**Search/Replace:**
```
# OLD
1. **Update AGENTS.md:** Set agent count to 16; add chief-of-staff, loop-operator, harness-optimizer to the agent table; align skill/command counts with repo.

# NEW (update with current agent names)
1. **Update AGENTS.md:** Set agent count to [current]; add [new agents] to the agent table; align skill/command counts with repo.
```

#### Verification Checklist for File 5

```bash
# Verify project name updated
grep "Everything Claude Code" docs/ARCHITECTURE-IMPROVEMENTS.md
# Expected: 0 results

grep "Everything Qwen Code" docs/ARCHITECTURE-IMPROVEMENTS.md
# Expected: At least 1 result

# Verify ECC → EQC acronym (if changing)
grep "ECC" docs/ARCHITECTURE-IMPROVEMENTS.md
# Expected: 0 results (or only in historical context)

grep "EQC" docs/ARCHITECTURE-IMPROVEMENTS.md
# Expected: Multiple results if changing acronym

# Verify agent counts are accurate (manual check)
ls -1 agents/*.md | wc -l
# Compare with count mentioned in document
```

---

## Testing Checklist

### Automated Verification

Run these commands after making all changes:

```bash
# 1. Check for remaining Claude Code references
echo "=== Checking for 'Claude Code' references ==="
grep -r "Claude Code" docs/ --include="*.md" | grep -v "refactor-qwen-code-phase1.md"

echo "=== Checking for '~/.claude/' paths ==="
grep -r "\~/.claude/" docs/ --include="*.md"

echo "=== Checking for 'CLAUDE_CODE_' env vars ==="
grep -r "CLAUDE_CODE_" docs/ --include="*.md"

echo "=== Checking for old repo references ==="
grep -r "affaan-m/everything-claude-code" docs/ --include="*.md"

# 2. Verify Qwen Code references are present
echo "=== Verifying 'Qwen Code' references ==="
grep -c "Qwen Code" docs/SKILL-DEVELOPMENT-GUIDE.md
grep -c "Qwen Code" docs/SKILL-PLACEMENT-POLICY.md
grep -c "Qwen Code" docs/token-optimization.md
grep -c "Qwen Code" docs/TROUBLESHOOTING.md
grep -c "Qwen Code" docs/ARCHITECTURE-IMPROVEMENTS.md

# 3. Verify new paths
echo "=== Verifying '~/.qwen/' paths ==="
grep -c "\~/.qwen/" docs/SKILL-DEVELOPMENT-GUIDE.md
grep -c "\~/.qwen/" docs/SKILL-PLACEMENT-POLICY.md
grep -c "\~/.qwen/" docs/token-optimization.md

# 4. Verify new env vars
echo "=== Verifying 'QWEN_CODE_' env vars ==="
grep -c "QWEN_CODE_" docs/token-optimization.md
grep -c "QWEN_CODE_" docs/TROUBLESHOOTING.md

# 5. Verify new repo references
echo "=== Verifying repo references ==="
grep -c "mowgliph/everything-qwen-code" docs/SKILL-DEVELOPMENT-GUIDE.md
grep -c "mowgliph/everything-qwen-code" docs/TROUBLESHOOTING.md
```

### Manual Review Checklist

- [ ] All "Claude Code" → "Qwen Code" (except in historical context)
- [ ] All "~/.claude/" → "~/.qwen/"
- [ ] All "CLAUDE_CODE_" → "QWEN_CODE_"
- [ ] All repo references updated to `mowgliph/everything-qwen-code`
- [ ] Model names are appropriate for Qwen Code
- [ ] Keyboard shortcuts are accurate for Qwen Code
- [ ] Command names (/clear, /compact, /cost, /mcp) exist in Qwen Code
- [ ] Agent counts are accurate
- [ ] Skill counts are accurate
- [ ] Command counts are accurate
- [ ] All cross-references to other docs files are valid
- [ ] Code examples use correct paths and syntax
- [ ] Tables are properly formatted
- [ ] Links are not broken

### Content Accuracy Review

```bash
# Verify agent count matches actual files
ACTUAL_AGENTS=$(ls -1 agents/*.md 2>/dev/null | wc -l)
echo "Actual agent count: $ACTUAL_AGENTS"

# Verify skill count matches actual directories
ACTUAL_SKILLS=$(ls -1d skills/*/ 2>/dev/null | wc -l)
echo "Actual skill count: $ACTUAL_SKILLS"

# Verify command count matches actual files
ACTUAL_COMMANDS=$(ls -1 commands/*.md 2>/dev/null | wc -l)
echo "Actual command count: $ACTUAL_COMMANDS"
```

---

## PR Checklist

### Pre-Commit

- [ ] All automated verification commands pass
- [ ] Manual review checklist completed
- [ ] Content accuracy review completed
- [ ] No broken links introduced
- [ ] Markdown formatting is valid

### Commit Message

```bash
docs: migrate Phase 1 documentation to Qwen Code branding

- Update SKILL-DEVELOPMENT-GUIDE.md with Qwen Code references
- Update SKILL-PLACEMENT-POLICY.md with ~/.qwen/ paths
- Update token-optimization.md with QWEN_CODE_ env vars
- Update TROUBLESHOOTING.md with new repo links
- Update ARCHITECTURE-IMPROVEMENTS.md with current counts

Part of: #XXX (documentation refactor epic)
```

### PR Description Template

```markdown
## Documentation Refactor: Phase 1 - Qwen Code Migration

### Summary
This PR migrates 5 critical documentation files from Claude Code to Qwen Code branding:
1. SKILL-DEVELOPMENT-GUIDE.md
2. SKILL-PLACEMENT-POLICY.md
3. token-optimization.md
4. TROUBLESHOOTING.md
5. ARCHITECTURE-IMPROVEMENTS.md

### Changes
- "Claude Code" → "Qwen Code" throughout
- "~/.claude/" → "~/.qwen/" paths
- "CLAUDE_CODE_" → "QWEN_CODE_" environment variables
- Repo references: affaan-m/everything-claude-code → mowgliph/everything-qwen-code
- Updated agent/skill/command counts to current values

### Testing
- [x] Verified no Claude Code references remain
- [x] Verified all Qwen Code references are correct
- [x] Verified all paths and environment variables updated
- [x] Verified all links are valid

### Related
- Blocks: Phase 2 (additional documentation files)
- Related to: #XXX (documentation refactor epic)
```

### Post-Merge

- [ ] Verify docs render correctly on GitHub
- [ ] Check for any user-reported issues with updated docs
- [ ] Update any external references to these files if needed

---

## Related Issues

### Phase 2: Additional Documentation Files

Files to be covered in Phase 2:
- `docs/` root files (README, CONTRIBUTING, etc.)
- `hooks/README.md`
- `skills/*/SKILL.md` files (skill-specific documentation)
- `agents/*.md` files (agent documentation)
- `commands/*.md` files (command documentation)

### Phase 3: Cross-Harness Alignment

- Verify `.agents/` and `.cursor/` subsets are in sync
- Update translation files if applicable
- Create catalog script for auto-generating counts

### Phase 4: Content Updates

- Update model recommendations based on Qwen Code capabilities
- Verify all keyboard shortcuts are accurate
- Add Qwen Code-specific tips and patterns
- Create Qwen Code migration guide for users

### Epic Tracking

Create issue: `#XXX - Documentation Refactor Epic`
- Phase 1: Core user guides (this document)
- Phase 2: Reference documentation
- Phase 3: Cross-harness alignment
- Phase 4: Qwen Code-specific content

---

## Appendix: Search/Replace Summary

### Global Replacements (All Files)

| Search | Replace | Notes |
|--------|---------|-------|
| `Everything Claude Code (ECC)` | `Everything Qwen Code (EQC)` | Project name |
| `Claude Code` | `Qwen Code` | Product name |
| `~/.claude/` | `~/.qwen/` | Config path |
| `CLAUDE_CODE_` | `QWEN_CODE_` | Env var prefix |
| `affaan-m/everything-claude-code` | `mowgliph/everything-qwen-code` | Repo reference |
| `everything-claude-code` | `everything-qwen-code` | Directory name |

### File-Specific Replacements

| File | Special Considerations |
|------|----------------------|
| `SKILL-DEVELOPMENT-GUIDE.md` | Update testing section paths, repo fork instructions |
| `SKILL-PLACEMENT-POLICY.md` | Update all skill root paths in table and sections |
| `token-optimization.md` | Verify model names, update env vars, check shortcuts |
| `TROUBLESHOOTING.md` | Update issue links, generalize bug descriptions |
| `ARCHITECTURE-IMPROVEMENTS.md` | Update counts, verify cross-harness dirs exist |

---

**Document Version:** 1.0  
**Created:** 2026-04-02  
**Author:** Planning Agent  
**Status:** Ready for Implementation
