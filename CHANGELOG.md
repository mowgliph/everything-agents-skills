# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-04-02

### Added

- **36 Specialized Agents** for software development tasks:
  - **Planning & Architecture:** `planner`, `architect`, `chief-of-staff`
  - **Code Review:** `code-reviewer`, `security-reviewer`, `typescript-reviewer`, `python-reviewer`, `go-reviewer`, `java-reviewer`, `kotlin-reviewer`, `rust-reviewer`, `cpp-reviewer`
  - **Build & Debug:** `build-error-resolver`, `tdd-guide`
  - **Documentation:** `doc-updater`, `docs-lookup`
- **151 Skills** for specialized workflows:
  - **Core Engineering:** `brainstorming`, `writing-plans`, `tdd-workflow`, `code-review-excellence`, `security-review`
  - **Language-Specific:** `python-patterns`, `golang-patterns`, `rust-patterns`, `typescript-advanced-types`, `kotlin-patterns`
  - **Frontend:** `frontend-design`, `frontend-patterns`, `react-modernization`, `responsive-design`, `design-system-patterns`
  - **Backend:** `backend-patterns`, `postgres-patterns`, `auth-implementation-patterns`, `microservices-patterns`
- **68 Slash Commands** for common workflows:
  - `/create-skill`, `/create-agent`, `/code-review`, `/test`
- **Automated Hooks** for PreToolUse, PostToolUse, SessionStart, and Stop events
- **Rules for 12+ Languages:** TypeScript, Python, Go, Java, Kotlin, Rust, C++, PHP, Perl, and more
- **14 MCP Server Configurations** for external service integration
- **Comprehensive Documentation:** AGENTS.md, SECURITY.md, CONTRIBUTING.md, CHANGELOG.md
- **Test Suite:** Unit tests, integration tests, and E2E tests
- **Plugin System:** Extensible architecture for custom agents, skills, and commands

### Changed

- Initial release as Everything Qwen Code (forked from Everything Claude Code)
- Rebranded for Qwen Code platform
- Version reset to 0.1.0 for initial release

### Security

- Security policy with vulnerability reporting process
- Secure secrets management guidelines

## Links

- [GitHub Repository](https://github.com/mowgliph/everything-qwen-code)
- [Issues](https://github.com/mowgliph/everything-qwen-code/issues)
- [Pull Requests](https://github.com/mowgliph/everything-qwen-code/pulls)
