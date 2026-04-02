# Everything Qwen Code Migration Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate the Everything Claude Code repository to Everything Qwen Code, removing all other editor compatibility and creating a fresh repository at `C:\Users\informatica\everything-qwen-code`.

**Architecture:** Create new repository structure with `.qwen/` and `.agents/` directories, migrate 36 agents, 151 skills, 68 commands, hooks, rules, and MCP configs to Qwen Code format, update documentation, and publish to GitHub.

**Tech Stack:** PowerShell (Windows), Qwen Code format, Git, GitHub, Node.js scripts.

---

## File Structure Overview

### New Repository Structure
```
C:\Users\informatica\everything-qwen-code/
├── .agents/                          # 36 agents in Qwen Code format
├── .qwen/                            # Qwen Code configuration
│   ├── skills/                       # 151 skills
│   ├── commands/                     # 68 commands
│   ├── hooks/                        # Hooks
│   ├── rules/                        # Rules for 12+ languages
│   └── mcp-configs/                  # MCP configurations
├── contexts/                         # Context files (copied)
├── docs/                             # Documentation (updated)
├── examples/                         # Examples (updated)
├── manifests/                        # Installation manifests
├── plugins/                          # Plugins
├── research/                         # Research
├── schemas/                          # JSON schemas
├── scripts/                          # Scripts (adapted)
├── tests/                            # Test suite (updated)
├── .gitignore                        # Updated
├── .mcp.json                         # MCP config
├── AGENTS.md                         # Updated for Qwen Code
├── agent.yaml                        # Updated for Qwen Code
├── CHANGELOG.md                      # New section for Qwen Code
├── CONTRIBUTING.md                   # Updated
├── package.json                      # Updated for Qwen Code
├── README.md                         # Completely rewritten
└── VERSION                           # 1.0.0
```

### Files to Create (New)
- `.agents/*.md` (36 files) - Converted from `agents/*.md`
- `.qwen/skills/*/SKILL.md` (151 files) - Converted from `skills/*/`
- `.qwen/commands/*/COMMAND.md` (68 files) - Converted from `commands/*/`
- `.qwen/hooks/*/HOOK.md` - Converted from `hooks/`
- `.qwen/rules/` - Copied from `rules/`
- `.qwen/mcp-configs/*.json` - Copied from `mcp-configs/`

### Files to Modify
- `README.md` - Complete rewrite for Qwen Code
- `AGENTS.md` - Update references
- `CHANGELOG.md` - Add v1.0.0 Qwen Code section
- `package.json` - Update name, description, keywords, files
- `agent.yaml` - Update for Qwen Code
- `.gitignore` - Add Qwen Code patterns
- All documentation files

---

## Phase 1: Repository Setup

### Task 1: Create New Repository Directory

**Files:**
- Create: `C:\Users\informatica\everything-qwen-code\`

- [ ] **Step 1: Create repository directory**

```powershell
New-Item -ItemType Directory -Path "C:\Users\informatica\everything-qwen-code" -Force
```

Expected: Directory created successfully

- [ ] **Step 2: Initialize Git repository**

```powershell
cd C:\Users\informatica\everything-qwen-code
git init
git branch -M main
```

Expected: Git repository initialized, branch renamed to main

- [ ] **Step 3: Create initial .gitignore**

```powershell
@'
# Qwen Code
.qwen/tmp/
.qwen/debug/

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Environment
.env
.env.local
'@ | Out-File -FilePath "C:\Users\informatica\everything-qwen-code\.gitignore" -Encoding utf8
```

Expected: .gitignore created

- [ ] **Step 4: Initial commit**

```powershell
git add .gitignore
git commit -m "chore: initial repository setup"
```

Expected: Commit created

---

## Phase 2: Directory Structure

### Task 2: Create Directory Structure

**Files:**
- Create: `.agents/`, `.qwen/skills/`, `.qwen/commands/`, `.qwen/hooks/`, `.qwen/rules/`, `.qwen/mcp-configs/`

- [ ] **Step 1: Create .agents directory**

```powershell
New-Item -ItemType Directory -Path "C:\Users\informatica\everything-qwen-code\.agents" -Force
```

- [ ] **Step 2: Create .qwen directory structure**

```powershell
$directories = @(
    ".qwen/skills",
    ".qwen/commands",
    ".qwen/hooks",
    ".qwen/rules/common",
    ".qwen/rules/python",
    ".qwen/rules/typescript",
    ".qwen/rules/golang",
    ".qwen/rules/java",
    ".qwen/rules/kotlin",
    ".qwen/rules/rust",
    ".qwen/rules/cpp",
    ".qwen/rules/php",
    ".qwen/rules/perl",
    ".qwen/mcp-configs"
)

foreach ($dir in $directories) {
    New-Item -ItemType Directory -Path "C:\Users\informatica\everything-qwen-code\$dir" -Force
}
```

- [ ] **Step 3: Copy base directories from source**

```powershell
$baseDirs = @("contexts", "docs", "examples", "manifests", "plugins", "research", "schemas", "scripts", "tests")

foreach ($dir in $baseDirs) {
    $source = "C:\Users\informatica\everything-claude-code\$dir"
    $dest = "C:\Users\informatica\everything-qwen-code\$dir"
    if (Test-Path $source) {
        Copy-Item -Path $source -Destination $dest -Recurse -Force
    }
}
```

- [ ] **Step 4: Commit directory structure**

```powershell
cd C:\Users\informatica\everything-qwen-code
git add .
git commit -m "chore: create directory structure"
```

---

## Phase 3: Agent Migration (36 files)

### Task 3: Create Agent Conversion Script

**Files:**
- Create: `scripts/migrate-agents.ps1`

- [ ] **Step 1: Write agent conversion script**

```powershell
# scripts/migrate-agents.ps1
param(
    [string]$SourceDir = "C:\Users\informatica\everything-claude-code\agents",
    [string]$DestDir = "C:\Users\informatica\everything-qwen-code\.agents"
)

# Color mapping by agent type
$colorMap = @{
    "planner" = "blue"
    "architect" = "blue"
    "chief-of-staff" = "blue"
    "gan-planner" = "blue"
    "code-reviewer" = "red"
    "security-reviewer" = "red"
    "tdd-guide" = "red"
    "healthcare-reviewer" = "red"
    "build-error-resolver" = "yellow"
    "cpp-build-resolver" = "yellow"
    "go-build-resolver" = "yellow"
    "java-build-resolver" = "yellow"
    "kotlin-build-resolver" = "yellow"
    "pytorch-build-resolver" = "yellow"
    "rust-build-resolver" = "yellow"
    "harness-optimizer" = "yellow"
    "cpp-reviewer" = "cyan"
    "database-reviewer" = "cyan"
    "go-reviewer" = "cyan"
    "java-reviewer" = "cyan"
    "kotlin-reviewer" = "cyan"
    "python-reviewer" = "cyan"
    "rust-reviewer" = "cyan"
    "typescript-reviewer" = "cyan"
    "flutter-reviewer" = "cyan"
    "loop-operator" = "green"
    "performance-optimizer" = "green"
    "gan-generator" = "green"
    "gan-evaluator" = "green"
    "doc-updater" = "magenta"
    "docs-lookup" = "magenta"
    "opensource-forker" = "magenta"
    "opensource-packager" = "magenta"
    "opensource-sanitizer" = "magenta"
    "e2e-runner" = "green"
    "refactor-cleaner" = "cyan"
}

# Get all agent files
$agentFiles = Get-ChildItem -Path $SourceDir -Filter "*.md"

foreach ($file in $agentFiles) {
    $name = $file.BaseName
    $color = $colorMap[$name] ?? "Automatic Color"
    
    # Read original content
    $content = Get-Content $file.FullName -Raw
    
    # Extract existing frontmatter
    if ($content -match '^---\s*\n(.*?)\n---\s*\n(.*)'s) {
        $oldFrontmatter = $matches[1]
        $body = $matches[2]
        
        # Extract old description
        if ($oldFrontmatter -match 'description:\s*["\']?(.*?)["\']?\s*$') {
            $oldDescription = $matches[1]
        }
        
        # Create new frontmatter
        $newFrontmatter = @"
---
name: $name
description: "Use this agent when working with $name tasks. Examples: <example>Context: User needs assistance with ${name}. user: \"Can you help me with ${name}?\" assistant: \"I'll use the $name agent to assist you.\" </example>"
color: $color
---
"@
        
        # Create new file
        $newContent = "$newFrontmatter`n$body"
        $destPath = Join-Path $DestDir $file.Name
        $newContent | Out-File -FilePath $destPath -Encoding utf8
        
        Write-Host "Converted: $name ($color)"
    }
}

Write-Host "Agent migration complete. $( $agentFiles.Count ) agents converted."
```

- [ ] **Step 2: Run agent conversion script**

```powershell
cd C:\Users\informatica\everything-qwen-code
.\scripts\migrate-agents.ps1
```

Expected: 36 agents converted with success messages

- [ ] **Step 3: Verify agent files created**

```powershell
Get-ChildItem -Path "C:\Users\informatica\everything-qwen-code\.agents" -Filter "*.md" | Measure-Object | Select-Object -ExpandProperty Count
```

Expected: 36

- [ ] **Step 4: Commit agents**

```powershell
git add .agents/
git commit -m "feat: migrate 36 agents to Qwen Code format"
```

---

## Phase 4: Skill Migration (151 files)

### Task 4: Create Skill Migration Script

**Files:**
- Create: `scripts/migrate-skills.ps1`

- [ ] **Step 1: Write skill conversion script**

```powershell
# scripts/migrate-skills.ps1
param(
    [string]$SourceDir = "C:\Users\informatica\everything-claude-code\skills",
    [string]$DestDir = "C:\Users\informatica\everything-qwen-code\.qwen\skills"
)

# Get all skill directories
$skillDirs = Get-ChildItem -Path $SourceDir -Directory

foreach ($skillDir in $skillDirs) {
    $skillName = $skillDir.Name
    $destSkillDir = Join-Path $DestDir $skillName
    
    # Create destination directory
    New-Item -ItemType Directory -Path $destSkillDir -Force | Out-Null
    
    # Find main skill file (index.md, SKILL.md, or first .md file)
    $skillFiles = Get-ChildItem -Path $skillDir.FullName -Filter "*.md"
    
    if ($skillFiles.Count -gt 0) {
        # Use first MD file as source
        $sourceFile = $skillFiles[0]
        $content = Get-Content $sourceFile.FullName -Raw
        
        # Extract name from existing frontmatter or use directory name
        $name = $skillName
        if ($content -match '^---\s*\nname:\s*(.*?)\s*$'m) {
            $name = $matches[1].Trim()
        }
        
        # Extract description from existing frontmatter
        $description = "Skill for $skillName"
        if ($content -match 'description:\s*["\']?(.*?)["\']?\s*$'m) {
            $description = $matches[1].Trim()
        }
        
        # Create new frontmatter
        $newFrontmatter = @"
---
name: $name
description: "$description"
version: 1.0.0
---

"@
        
        # Extract body (remove old frontmatter)
        $body = $content
        if ($content -match '^---\s*\n(.*?)\n---\s*\n(.*)'s) {
            $body = $matches[2]
        }
        
        # Create SKILL.md
        $newContent = "$newFrontmatter$body"
        $destFile = Join-Path $destSkillDir "SKILL.md"
        $newContent | Out-File -FilePath $destFile -Encoding utf8
        
        # Copy additional files (scripts, references, etc.)
        $additionalFiles = Get-ChildItem -Path $skillDir.FullName -Exclude "*.md"
        foreach ($addFile in $additionalFiles) {
            Copy-Item -Path $addFile.FullName -Destination $destSkillDir -Force
        }
        
        Write-Host "Migrated: $skillName"
    }
}

Write-Host "Skill migration complete. $( $skillDirs.Count ) skills converted."
```

- [ ] **Step 2: Run skill conversion script**

```powershell
cd C:\Users\informatica\everything-qwen-code
.\scripts\migrate-skills.ps1
```

Expected: 151 skills migrated with success messages

- [ ] **Step 3: Verify skill files created**

```powershell
Get-ChildItem -Path "C:\Users\informatica\everything-qwen-code\.qwen\skills" -Directory | Measure-Object | Select-Object -ExpandProperty Count
```

Expected: 151

- [ ] **Step 4: Commit skills**

```powershell
git add .qwen/skills/
git commit -m "feat: migrate 151 skills to Qwen Code format"
```

---

## Phase 5: Commands, Hooks, Rules, MCP

### Task 5: Migrate Commands (68 files)

**Files:**
- Create: `scripts/migrate-commands.ps1`

- [ ] **Step 1: Write and run command migration script**

```powershell
# scripts/migrate-commands.ps1
param(
    [string]$SourceDir = "C:\Users\informatica\everything-claude-code\commands",
    [string]$DestDir = "C:\Users\informatica\everything-qwen-code\.qwen\commands"
)

$commandDirs = Get-ChildItem -Path $SourceDir -Directory

foreach ($cmdDir in $commandDirs) {
    $cmdName = $cmdDir.Name
    $destCmdDir = Join-Path $DestDir $cmdName
    
    New-Item -ItemType Directory -Path $destCmdDir -Force | Out-Null
    
    $cmdFiles = Get-ChildItem -Path $cmdDir.FullName -Filter "*.md"
    if ($cmdFiles.Count -gt 0) {
        $sourceFile = $cmdFiles[0]
        $content = Get-Content $sourceFile.FullName -Raw
        
        $name = $cmdName
        if ($content -match 'name:\s*(.*?)\s*$'m) {
            $name = $matches[1].Trim()
        }
        
        $description = "Command for $cmdName"
        if ($content -match 'description:\s*["\']?(.*?)["\']?\s*$'m) {
            $description = $matches[1].Trim()
        }
        
        $newFrontmatter = @"
---
name: $name
description: "$description"
version: 1.0.0
---

"@
        
        $body = $content
        if ($content -match '^---\s*\n(.*?)\n---\s*\n(.*)'s) {
            $body = $matches[2]
        }
        
        "$newFrontmatter$body" | Out-File -FilePath (Join-Path $destCmdDir "COMMAND.md") -Encoding utf8
        
        Write-Host "Migrated: $cmdName"
    }
}

Write-Host "Command migration complete. $( $commandDirs.Count ) commands converted."
```

- [ ] **Step 2: Run and commit**

```powershell
.\scripts\migrate-commands.ps1
git add .qwen/commands/
git commit -m "feat: migrate 68 commands to Qwen Code format"
```

### Task 6: Migrate Hooks

**Files:**
- Create: `scripts/migrate-hooks.ps1`

- [ ] **Step 1: Write and run hook migration script**

```powershell
# scripts/migrate-hooks.ps1
param(
    [string]$SourceDir = "C:\Users\informatica\everything-claude-code\hooks",
    [string]$DestDir = "C:\Users\informatica\everything-qwen-code\.qwen\hooks"
)

# Copy hooks directory
if (Test-Path $SourceDir) {
    Copy-Item -Path $SourceDir -Destination $DestDir -Recurse -Force
    Write-Host "Hooks migrated"
}
```

- [ ] **Step 2: Commit**

```powershell
git add .qwen/hooks/
git commit -m "feat: migrate hooks to Qwen Code format"
```

### Task 7: Migrate Rules

**Files:**
- Create: `scripts/migrate-rules.ps1`

- [ ] **Step 1: Copy rules**

```powershell
$sourceRules = "C:\Users\informatica\everything-claude-code\rules"
$destRules = "C:\Users\informatica\everything-qwen-code\.qwen\rules"

if (Test-Path $sourceRules) {
    Copy-Item -Path $sourceRules -Destination $destRules -Recurse -Force
    Write-Host "Rules migrated"
}
```

- [ ] **Step 2: Commit**

```powershell
git add .qwen/rules/
git commit -m "feat: migrate rules to Qwen Code format"
```

### Task 8: Migrate MCP Configs

**Files:**
- Create: `scripts/migrate-mcp.ps1`

- [ ] **Step 1: Copy MCP configs**

```powershell
$sourceMcp = "C:\Users\informatica\everything-claude-code\mcp-configs"
$destMcp = "C:\Users\informatica\everything-qwen-code\.qwen\mcp-configs"

if (Test-Path $sourceMcp) {
    Copy-Item -Path $sourceMcp -Destination $destMcp -Recurse -Force
    Write-Host "MCP configs migrated"
}
```

- [ ] **Step 2: Copy root .mcp.json**

```powershell
Copy-Item -Path "C:\Users\informatica\everything-claude-code\.mcp.json" -Destination "C:\Users\informatica\everything-qwen-code\.mcp.json" -Force
```

- [ ] **Step 3: Commit**

```powershell
git add .qwen/mcp-configs/ .mcp.json
git commit -m "feat: migrate MCP configurations"
```

---

## Phase 6: Configuration Files

### Task 9: Update package.json

**Files:**
- Modify: `package.json`

- [ ] **Step 1: Create updated package.json**

```json
{
  "name": "everything-qwen-code",
  "version": "1.0.0",
  "description": "Complete collection of battle-tested Qwen Code configs — agents, skills, hooks, rules, and MCP configurations evolved over 10+ months of intensive daily use",
  "keywords": [
    "qwen-code",
    "ai",
    "agents",
    "skills",
    "hooks",
    "mcp",
    "rules",
    "qwen",
    "tdd",
    "code-review",
    "security",
    "automation",
    "best-practices"
  ],
  "author": {
    "name": "Your Name",
    "url": "https://github.com/your-username"
  },
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/your-username/everything-qwen-code.git"
  },
  "homepage": "https://github.com/your-username/everything-qwen-code#readme",
  "bugs": {
    "url": "https://github.com/your-username/everything-qwen-code/issues"
  },
  "files": [
    ".agents/",
    ".qwen/",
    "contexts/",
    "docs/",
    "examples/",
    "manifests/",
    "plugins/",
    "research/",
    "schemas/",
    "scripts/",
    "tests/",
    "AGENTS.md",
    "README.md",
    "agent.yaml",
    "package.json"
  ],
  "scripts": {
    "lint": "eslint . && markdownlint '**/*.md' --ignore node_modules",
    "test": "node tests/run-all.js"
  },
  "engines": {
    "node": ">=18"
  }
}
```

- [ ] **Step 2: Write package.json**

```powershell
@'
{
  "name": "everything-qwen-code",
  "version": "1.0.0",
  "description": "Complete collection of battle-tested Qwen Code configs — agents, skills, hooks, rules, and MCP configurations evolved over 10+ months of intensive daily use",
  "keywords": [
    "qwen-code",
    "ai",
    "agents",
    "skills",
    "hooks",
    "mcp",
    "rules",
    "qwen",
    "tdd",
    "code-review",
    "security",
    "automation",
    "best-practices"
  ],
  "author": {
    "name": "Your Name",
    "url": "https://github.com/your-username"
  },
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/your-username/everything-qwen-code.git"
  },
  "homepage": "https://github.com/your-username/everything-qwen-code#readme",
  "bugs": {
    "url": "https://github.com/your-username/everything-qwen-code/issues"
  },
  "files": [
    ".agents/",
    ".qwen/",
    "contexts/",
    "docs/",
    "examples/",
    "manifests/",
    "plugins/",
    "research/",
    "schemas/",
    "scripts/",
    "tests/",
    "AGENTS.md",
    "README.md",
    "agent.yaml",
    "package.json"
  ],
  "scripts": {
    "lint": "eslint . && markdownlint '**/*.md' --ignore node_modules",
    "test": "node tests/run-all.js"
  },
  "engines": {
    "node": ">=18"
  }
}
'@ | Out-File -FilePath "C:\Users\informatica\everything-qwen-code\package.json" -Encoding utf8
```

- [ ] **Step 3: Commit**

```powershell
git add package.json
git commit -m "chore: update package.json for Qwen Code"
```

### Task 10: Update agent.yaml

**Files:**
- Modify: `agent.yaml`

- [ ] **Step 1: Create updated agent.yaml**

```powershell
@'
spec_version: "0.1.0"
name: everything-qwen-code
version: 1.0.0
description: "Complete collection of battle-tested Qwen Code configs for software development"
author: your-username
license: MIT
model:
  preferred: qwen-max
  fallback:
    - qwen-plus
skills:
  - accessibility-compliance
  - agent-development
  - api-design-principles
  - architecture-decision-records
  - architecture-patterns
  - async-python-patterns
  - auth-implementation-patterns
  - backend-patterns
  - brainstorming
  - code-review-excellence
  - coding-standards
  - command-development
  - continuous-learning
  - continuous-learning-v2
  - debugging
  - debugging-strategies
  - design-system-patterns
  - e2e-testing-patterns
  - error-handling-patterns
  - frontend-design
  - frontend-patterns
  - git-advanced-workflows
  - golang-patterns
  - golang-testing
  - javascript-testing-patterns
  - kotlin-patterns
  - kotlin-testing
  - memory-safety-patterns
  - microservices-patterns
  - modern-javascript-patterns
  - nextjs-app-router-patterns
  - postgres-patterns
  - python-patterns
  - python-testing
  - rag-implementation
  - react-modernization
  - react-state-management
  - responsive-design
  - rust-async-patterns
  - rust-patterns
  - security-review
  - sql-optimization-patterns
  - tdd-workflow
  - test-driven-development
  - typescript-advanced-types
  - web-component-design
  - workflow-patterns
tags:
  - qwen-code
  - developer-tools
  - code-review
  - testing
  - security
'@ | Out-File -FilePath "C:\Users\informatica\everything-qwen-code\agent.yaml" -Encoding utf8
```

- [ ] **Step 2: Commit**

```powershell
git add agent.yaml
git commit -m "chore: update agent.yaml for Qwen Code"
```

---

## Phase 7: Documentation

### Task 11: Update README.md

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Create new README.md**

```powershell
@'
# Everything Qwen Code

[![Stars](https://img.shields.io/github/stars/your-username/everything-qwen-code?style=flat)](https://github.com/your-username/everything-qwen-code/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**The performance optimization system for Qwen Code. From production experience.**

Not just configs. A complete system: skills, agents, hooks, rules, and MCP configurations. Production-ready agents, skills, hooks, rules, and MCP configurations evolved over 10+ months of intensive daily use building real products.

Built exclusively for **Qwen Code**.

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/everything-qwen-code.git
cd everything-qwen-code

# Install dependencies
npm install
```

### Usage

1. **Agents**: 36 specialized agents for different tasks
   - `planner` - Implementation planning
   - `architect` - System design
   - `code-reviewer` - Code quality review
   - `security-reviewer` - Security analysis
   - `tdd-guide` - Test-driven development

2. **Skills**: 151 skills for specialized workflows
   - `brainstorming` - Design before implementation
   - `writing-plans` - Create implementation plans
   - `security-review` - Security checklist
   - `tdd-workflow` - TDD enforcement

3. **Commands**: 68 slash commands
   - `/create-skill` - Create new skill
   - `/create-agent` - Create new agent
   - `/code-review` - Review code
   - `/test` - Run tests

---

## The Guides

This repo contains the raw code. The guides explain everything.

| Topic | What You'll Learn |
|-------|-------------------|
| Agent Usage | When to use each of the 36 agents |
| Skills | 151 specialized workflows |
| Commands | 68 slash commands |
| Hooks | Automated workflows |
| Rules | Coding standards for 12+ languages |

---

## What's Included

### 36 Agents

Specialized agents for every software development task:

**Planning & Architecture:**
- `planner` - Implementation planning
- `architect` - System architecture
- `chief-of-staff` - Strategic planning

**Code Review:**
- `code-reviewer` - General code review
- `security-reviewer` - Security analysis
- `typescript-reviewer` - TypeScript/JavaScript
- `python-reviewer` - Python
- `go-reviewer` - Go
- `java-reviewer` - Java
- `kotlin-reviewer` - Kotlin
- `rust-reviewer` - Rust
- `cpp-reviewer` - C++

**Build & Debug:**
- `build-error-resolver` - Fix build errors
- `tdd-guide` - Test-driven development

**Documentation:**
- `doc-updater` - Update documentation
- `docs-lookup` - API documentation

*(See `.agents/` for complete list)*

### 151 Skills

Skills for every development workflow:

**Core Engineering:**
- `brainstorming` - Design before code
- `writing-plans` - Implementation plans
- `tdd-workflow` - Test-driven development
- `code-review-excellence` - Code review patterns
- `security-review` - Security checklist

**Language-Specific:**
- `python-patterns`, `python-testing`
- `golang-patterns`, `golang-testing`
- `rust-patterns`, `rust-async-patterns`
- `typescript-advanced-types`
- `kotlin-patterns`, `kotlin-testing`

**Frontend:**
- `frontend-design`, `frontend-patterns`
- `react-modernization`, `react-state-management`
- `responsive-design`, `design-system-patterns`

**Backend:**
- `backend-patterns`, `postgres-patterns`
- `auth-implementation-patterns`
- `microservices-patterns`

*(See `.qwen/skills/` for complete list)*

### 68 Commands

Slash commands for common workflows:

- `/create-skill` - Create new skill
- `/create-agent` - Create new agent
- `/create-command` - Create new command
- `/create-hook` - Create new hook
- `/code-review` - Review code
- `/security-review` - Security analysis
- `/test` - Run tests
- `/build` - Build project

*(See `.qwen/commands/` for complete list)*

### Rules for 12+ Languages

Coding standards for:

- TypeScript/JavaScript
- Python
- Go
- Java
- Kotlin
- Rust
- C++
- PHP
- Perl
- Common (all languages)

*(See `.qwen/rules/` for complete list)*

---

## Project Structure

```
everything-qwen-code/
├── .agents/              # 36 agents in Qwen Code format
├── .qwen/                # Qwen Code configuration
│   ├── skills/           # 151 skills
│   ├── commands/         # 68 commands
│   ├── hooks/            # Automated hooks
│   ├── rules/            # Language rules
│   └── mcp-configs/      # MCP server configs
├── docs/                 # Documentation
├── scripts/              # Utility scripts
├── tests/                # Test suite
├── README.md             # This file
├── AGENTS.md             # Agent documentation
├── agent.yaml            # Agent configuration
└── package.json          # Package configuration
```

---

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

This project was inspired by the excellent Everything Claude Code project.
'@ | Out-File -FilePath "C:\Users\informatica\everything-qwen-code\README.md" -Encoding utf8
```

- [ ] **Step 2: Commit**

```powershell
git add README.md
git commit -m "docs: create README.md for Qwen Code"
```

### Task 12: Update AGENTS.md

**Files:**
- Modify: `AGENTS.md`

- [ ] **Step 1: Copy and update AGENTS.md**

```powershell
$source = "C:\Users\informatica\everything-claude-code\AGENTS.md"
$dest = "C:\Users\informatica\everything-qwen-code\AGENTS.md"

if (Test-Path $source) {
    $content = Get-Content $source -Raw
    
    # Replace Claude Code references with Qwen Code
    $content = $content -replace "Claude Code", "Qwen Code"
    $content = $content -replace "claude", "qwen", "IgnoreCase"
    $content = $content -replace "\.claude/", ".qwen/"
    
    $content | Out-File -FilePath $dest -Encoding utf8
    Write-Host "AGENTS.md updated"
}
```

- [ ] **Step 2: Commit**

```powershell
git add AGENTS.md
git commit -m "docs: update AGENTS.md for Qwen Code"
```

### Task 13: Update CHANGELOG.md

**Files:**
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Add Qwen Code section to CHANGELOG.md**

```powershell
$source = "C:\Users\informatica\everything-claude-code\CHANGELOG.md"
$dest = "C:\Users\informatica\everything-qwen-code\CHANGELOG.md"

if (Test-Path $source) {
    $content = Get-Content $source -Raw
    
    # Add new section at top
    $newSection = @"
# Changelog

All notable changes to Everything Qwen Code will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-02

### Added
- Initial release of Everything Qwen Code
- 36 agents converted to Qwen Code format
- 151 skills migrated to Qwen Code
- 68 commands migrated
- Hooks, rules, and MCP configurations
- Exclusive Qwen Code support

### Changed
- Renamed from Everything Claude Code to Everything Qwen Code
- All components adapted for Qwen Code format
- Documentation updated for Qwen Code

### Removed
- Claude Code compatibility
- Cursor, Codex, Kiro, Trae, CodeBuddy, OpenCode, Gemini support

"@
    
    "$newSection`n$content" | Out-File -FilePath $dest -Encoding utf8
    Write-Host "CHANGELOG.md updated"
}
```

- [ ] **Step 2: Commit**

```powershell
git add CHANGELOG.md
git commit -m "docs: add Qwen Code v1.0.0 to CHANGELOG.md"
```

### Task 14: Update Remaining Documentation

**Files:**
- Modify: `CONTRIBUTING.md`, `SECURITY.md`, `SOUL.md`, `TROUBLESHOOTING.md`, etc.

- [ ] **Step 1: Copy and update documentation files**

```powershell
$docs = @("CONTRIBUTING.md", "SECURITY.md", "SOUL.md", "TROUBLESHOOTING.md", "WORKING-CONTEXT.md")

foreach ($doc in $docs) {
    $source = "C:\Users\informatica\everything-claude-code\$doc"
    $dest = "C:\Users\informatica\everything-qwen-code\$doc"
    
    if (Test-Path $source) {
        $content = Get-Content $source -Raw
        
        # Replace references
        $content = $content -replace "Claude Code", "Qwen Code"
        $content = $content -replace "\.claude/", ".qwen/"
        
        $content | Out-File -FilePath $dest -Encoding utf8
        Write-Host "$doc updated"
    }
}
```

- [ ] **Step 2: Commit**

```powershell
git add *.md
git commit -m "docs: update remaining documentation for Qwen Code"
```

### Task 15: Create VERSION file

**Files:**
- Create: `VERSION`

- [ ] **Step 1: Create VERSION file**

```powershell
"1.0.0" | Out-File -FilePath "C:\Users\informatica\everything-qwen-code\VERSION" -Encoding utf8
```

- [ ] **Step 2: Commit**

```powershell
git add VERSION
git commit -m "chore: add VERSION file (1.0.0)"
```

---

## Phase 8: GitHub Repository

### Task 16: Create GitHub Repository

**Files:**
- GitHub repository creation

- [ ] **Step 1: Check if GitHub CLI is installed**

```powershell
gh --version
```

Expected: Version output or error if not installed

- [ ] **Step 2: If not installed, install GitHub CLI**

```powershell
winget install --id GitHub.cli
```

- [ ] **Step 3: Authenticate with GitHub**

```powershell
gh auth login
```

Expected: Browser opens for authentication

- [ ] **Step 4: Create repository**

```powershell
cd C:\Users\informatica\everything-qwen-code
gh repo create everything-qwen-code --public --source=. --remote=origin --push
```

Expected: Repository created on GitHub

- [ ] **Step 5: Verify repository**

```powershell
gh repo view everything-qwen-code
```

Expected: Repository details displayed

---

## Phase 9: Final Verification

### Task 17: Run Final Verification

**Files:**
- All repository files

- [ ] **Step 1: Verify directory structure**

```powershell
Write-Host "=== Directory Structure ==="
Get-ChildItem -Path "C:\Users\informatica\everything-qwen-code" -Directory | Select-Object Name

Write-Host "`n=== .agents/ count ==="
(Get-ChildItem -Path "C:\Users\informatica\everything-qwen-code\.agents" -Filter "*.md").Count

Write-Host "`n=== .qwen/skills/ count ==="
(Get-ChildItem -Path "C:\Users\informatica\everything-qwen-code\.qwen\skills" -Directory).Count

Write-Host "`n=== .qwen/commands/ count ==="
(Get-ChildItem -Path "C:\Users\informatica\everything-qwen-code\.qwen\commands" -Directory).Count
```

Expected: All directories present, 36 agents, 151 skills, 68 commands

- [ ] **Step 2: Verify Git status**

```powershell
cd C:\Users\informatica\everything-qwen-code
git status
```

Expected: Clean working tree

- [ ] **Step 3: Verify Git log**

```powershell
git log --oneline
```

Expected: Multiple commits showing migration progress

---

## Success Criteria

- [ ] Repository created at `C:\Users\informatica\everything-qwen-code`
- [ ] 36 agents migrated to `.agents/` in Qwen Code format
- [ ] 151 skills migrated to `.qwen/skills/`
- [ ] 68 commands migrated to `.qwen/commands/`
- [ ] Hooks migrated to `.qwen/hooks/`
- [ ] Rules migrated to `.qwen/rules/`
- [ ] MCP configs migrated to `.qwen/mcp-configs/`
- [ ] `package.json` updated for Qwen Code
- [ ] `agent.yaml` updated for Qwen Code
- [ ] `README.md` created for Qwen Code
- [ ] `AGENTS.md` updated for Qwen Code
- [ ] `CHANGELOG.md` updated with v1.0.0
- [ ] All documentation updated
- [ ] GitHub repository created and pushed
- [ ] All commits successful
- [ ] Git working tree clean

---

## Rollback Plan

If migration fails at any point:

1. **Delete partial repository:**
   ```powershell
   Remove-Item -Path "C:\Users\informatica\everything-qwen-code" -Recurse -Force
   ```

2. **Source repository remains intact:**
   - `C:\Users\informatica\everything-claude-code` is unchanged
   - Can retry migration anytime

3. **GitHub repository:**
   ```powershell
   gh repo delete everything-qwen-code --confirm
   ```

---

## Estimated Time

- Phase 1-2: Setup (15 minutes)
- Phase 3: Agents (30 minutes)
- Phase 4: Skills (45 minutes)
- Phase 5: Commands/Hooks/Rules/MCP (30 minutes)
- Phase 6: Configuration (15 minutes)
- Phase 7: Documentation (45 minutes)
- Phase 8: GitHub (15 minutes)
- Phase 9: Verification (10 minutes)

**Total: ~3.5 hours**
