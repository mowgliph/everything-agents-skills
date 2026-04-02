# Spec: Everything Qwen Code Migration

**Date:** 2026-04-02  
**Status:** Proposed  
**Author:** AI Assistant

---

## Executive Summary

Migrar el repositorio "Everything Claude Code" a "Everything Qwen Code", eliminando toda compatibilidad con otros editores (Claude Code, Cursor, Codex, Kiro, Trae, CodeBuddy, OpenCode, Gemini) y adaptando todos los componentes al formato nativo de Qwen Code.

**Alcance:**
- 36 agents → convertir a formato Qwen Code
- 151 skills → migrar a `.qwen/skills/`
- 68 commands → migrar a `.qwen/commands/`
- Hooks → migrar a `.qwen/hooks/`
- Rules → migrar a `.qwen/rules/`
- MCP configs → migrar a `.qwen/mcp-configs/`
- Documentación → actualizar completamente
- Scripts → adaptar para Qwen Code

---

## Contexto

El repositorio actual "Everything Claude Code" es un sistema de optimización para múltiples harnesses de AI agents. Contiene:

- 36 agents especializados en Markdown
- 151 skills en formato Claude Code Plugin
- 68 commands slash
- Hooks automatizados
- Rules para 12+ lenguajes
- Configuraciones MCP
- Scripts utilitarios

**Problema:** El repositorio soporta múltiples editores, creando complejidad innecesaria y duplicación de esfuerzos.

**Oportunidad:** Enfocarse exclusivamente en Qwen Code permite:
- Simplificar la base de código
- Mejorar la calidad de cada componente
- Reducir mantenimiento
- Mejor experiencia para usuarios de Qwen Code

---

## Requisitos Funcionales

### RF1: Migración de Agents (36 archivos)

Cada agent debe convertirse del formato Claude Code al formato Qwen Code:

**Formato Original (Claude Code):**
```markdown
---
name: planner
description: Expert planning specialist for complex features...
tools: ["Read", "Grep", "Glob"]
model: opus
---
```

**Formato Destino (Qwen Code):**
```markdown
---
name: planner
description: "Use this agent when [conditions]. Examples: <example>Context: [...] user: \"[...]\" assistant: \"[...]\" </example> <example>...</example>"
color: blue
---
```

**Lista de Agents a Migrar:**
1. `architect.md` → `.agents/architect.md`
2. `build-error-resolver.md` → `.agents/build-error-resolver.md`
3. `chief-of-staff.md` → `.agents/chief-of-staff.md`
4. `code-reviewer.md` → `.agents/code-reviewer.md`
5. `cpp-build-resolver.md` → `.agents/cpp-build-resolver.md`
6. `cpp-reviewer.md` → `.agents/cpp-reviewer.md`
7. `database-reviewer.md` → `.agents/database-reviewer.md`
8. `doc-updater.md` → `.agents/doc-updater.md`
9. `docs-lookup.md` → `.agents/docs-lookup.md`
10. `e2e-runner.md` → `.agents/e2e-runner.md`
11. `flutter-reviewer.md` → `.agents/flutter-reviewer.md`
12. `gan-evaluator.md` → `.agents/gan-evaluator.md`
13. `gan-generator.md` → `.agents/gan-generator.md`
14. `gan-planner.md` → `.agents/gan-planner.md`
15. `go-build-resolver.md` → `.agents/go-build-resolver.md`
16. `go-reviewer.md` → `.agents/go-reviewer.md`
17. `harness-optimizer.md` → `.agents/harness-optimizer.md`
18. `healthcare-reviewer.md` → `.agents/healthcare-reviewer.md`
19. `java-build-resolver.md` → `.agents/java-build-resolver.md`
20. `java-reviewer.md` → `.agents/java-reviewer.md`
21. `kotlin-build-resolver.md` → `.agents/kotlin-build-resolver.md`
22. `kotlin-reviewer.md` → `.agents/kotlin-reviewer.md`
23. `loop-operator.md` → `.agents/loop-operator.md`
24. `opensource-forker.md` → `.agents/opensource-forker.md`
25. `opensource-packager.md` → `.agents/opensource-packager.md`
26. `opensource-sanitizer.md` → `.agents/opensource-sanitizer.md`
27. `performance-optimizer.md` → `.agents/performance-optimizer.md`
28. `planner.md` → `.agents/planner.md`
29. `python-reviewer.md` → `.agents/python-reviewer.md`
30. `pytorch-build-resolver.md` → `.agents/pytorch-build-resolver.md`
31. `refactor-cleaner.md` → `.agents/refactor-cleaner.md`
32. `rust-build-resolver.md` → `.agents/rust-build-resolver.md`
33. `rust-reviewer.md` → `.agents/rust-reviewer.md`
34. `security-reviewer.md` → `.agents/security-reviewer.md`
35. `tdd-guide.md` → `.agents/tdd-guide.md`
36. `typescript-reviewer.md` → `.agents/typescript-reviewer.md`

**Asignación de Colores:**
- `blue`: architect, planner, chief-of-staff, gan-planner
- `red`: code-reviewer, security-reviewer, tdd-guide, healthcare-reviewer
- `yellow`: build-error-resolver, cpp-build-resolver, go-build-resolver, java-build-resolver, kotlin-build-resolver, pytorch-build-resolver, rust-build-resolver, harness-optimizer
- `cyan`: cpp-reviewer, database-reviewer, go-reviewer, java-reviewer, kotlin-reviewer, python-reviewer, rust-reviewer, typescript-reviewer, flutter-reviewer
- `green`: loop-operator, performance-optimizer, gan-generator, gan-evaluator
- `magenta`: doc-updater, docs-lookup, opensource-forker, opensource-packager, opensource-sanitizer

### RF2: Migración de Skills (151 archivos)

Cada skill debe migrarse manteniendo su funcionalidad pero adaptando el formato:

**Formato Original (Claude Code Plugin):**
- Archivos en `skills/<nombre>/`
- Usan herramientas específicas de Claude Code (`Task`, `skill`, etc.)

**Formato Destino (Qwen Code):**
- Archivos en `.qwen/skills/<nombre>/SKILL.md`
- Frontmatter YAML con `name`, `description`, `version`
- Contenido en Markdown con instrucciones claras

**Skills Críticas a Migrar (prioritarias):**
1. `accessibility-compliance`
2. `Agent Development`
3. `api-design-principles`
4. `architecture-decision-records`
5. `architecture-patterns`
6. `async-python-patterns`
7. `auth-implementation-patterns`
8. `backend-patterns`
9. `brainstorming`
10. `code-review-excellence`
11. `coding-standards`
12. `Command Development`
13. `continuous-learning`
14. `continuous-learning-v2`
15. `debugging`
16. `debugging-strategies`
17. `design-system-patterns`
18. `e2e-testing-patterns`
19. `error-handling-patterns`
20. `frontend-design`
21. `frontend-patterns`
22. `git-advanced-workflows`
23. `golang-patterns`
24. `golang-testing`
25. `javascript-testing-patterns`
26. `kotlin-patterns`
27. `kotlin-testing`
28. `memory-safety-patterns`
29. `microservices-patterns`
30. `modern-javascript-patterns`
31. `nextjs-app-router-patterns`
32. `postgres-patterns`
33. `python-patterns`
34. `python-testing`
35. `rag-implementation`
36. `react-modernization`
37. `react-state-management`
38. `responsive-design`
39. `rust-async-patterns`
40. `rust-patterns`
41. `security-review`
42. `sql-optimization-patterns`
43. `tdd-workflow`
44. `test-driven-development`
45. `typescript-advanced-types`
46. `web-component-design`
47. `workflow-patterns`

*(Lista completa de 151 skills en Anexo A)*

### RF3: Migración de Commands (68 archivos)

**Formato Original:**
- Archivos en `commands/<nombre>/`
- Formato específico de Claude Code

**Formato Destino:**
- Carpetas en `.qwen/commands/<nombre>/COMMAND.md`
- Frontmatter YAML con `name`, `description`, `arguments` (si aplica)

**Commands a Migrar:**
- `create-skill`
- `create-agent`
- `create-command`
- `create-hook`
- `code-review`
- `security-review`
- `tdd`
- `test`
- `build`
- `deploy`
- *(Lista completa en Anexo B)*

### RF4: Migración de Hooks

**Formato Original:**
- Hooks en `hooks/` y `.claude/hooks/`
- Eventos: `PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`, etc.

**Formato Destino:**
- Carpetas en `.qwen/hooks/<nombre>/HOOK.md`
- Frontmatter con `name`, `description`, `event`, `condition`

**Hooks Críticos:**
- `security-scan` (PreToolUse para comandos Bash)
- `session-recording` (SessionStart/SessionEnd)
- `continuous-learning` (PostToolUse)
- `context-optimization` (Stop)

### RF5: Migración de Rules

**Formato Original:**
- `rules/common/` - Reglas comunes
- `rules/python/`, `rules/typescript/`, etc. - Reglas por lenguaje

**Formato Destino:**
- `.qwen/rules/common/` - Reglas comunes
- `.qwen/rules/python/`, `.qwen/rules/typescript/`, etc.

**Rules a Migrar:**
- `common/` (12 archivos)
- `python/` (8 archivos)
- `typescript/` (6 archivos)
- `golang/` (4 archivos)
- `java/` (4 archivos)
- `kotlin/` (4 archivos)
- `rust/` (4 archivos)
- `cpp/` (4 archivos)
- `php/` (4 archivos)
- `perl/` (4 archivos)

### RF6: Migración de MCP Configs

**Formato Original:**
- `mcp-configs/*.json`

**Formato Destino:**
- `.qwen/mcp-configs/*.json`

**Configs a Migrar:**
- `github.json`
- `context7.json`
- `exa.json`
- `memory.json`
- `playwright.json`
- `sequential-thinking.json`

### RF7: Actualización de Documentación

**Archivos a Actualizar:**
1. `README.md` → Cambiar título, descripción, badges, ejemplos
2. `AGENTS.md` → Actualizar para Qwen Code
3. `CHANGELOG.md` → Mantener histórico, agregar nueva sección
4. `CONTRIBUTING.md` → Actualizar para Qwen Code
5. `COMMANDS-QUICK-REF.md` → Actualizar comandos
6. `EVALUATION.md` → Actualizar para Qwen Code
7. `SECURITY.md` → Mantener, actualizar referencias
8. `SOUL.md` → Actualizar filosofía para Qwen Code
9. `TROUBLESHOOTING.md` → Actualizar para Qwen Code
10. `VERSION` → Actualizar a 1.0.0 (Qwen Code)
11. `WORKING-CONTEXT.md` → Actualizar para Qwen Code
12. `the-longform-guide.md` → Actualizar para Qwen Code
13. `the-shortform-guide.md` → Actualizar para Qwen Code
14. `the-security-guide.md` → Actualizar para Qwen Code

### RF8: Actualización de package.json

**Cambios Requeridas:**
```json
{
  "name": "everything-qwen-code",
  "version": "1.0.0",
  "description": "Complete collection of battle-tested Qwen Code configs — agents, skills, hooks, rules, and MCP configurations",
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
  "files": [
    ".agents/",
    ".qwen/skills/",
    ".qwen/commands/",
    ".qwen/hooks/",
    ".qwen/rules/",
    ".qwen/mcp-configs/",
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
    "README.md"
  ]
}
```

### RF9: Actualización de agent.yaml

**Cambios Requeridos:**
```yaml
spec_version: "0.1.0"
name: everything-qwen-code
version: 1.0.0
description: "Complete collection of battle-tested Qwen Code configs for software development"
author: [tu-usuario]
license: MIT
model:
  preferred: qwen-max
  fallback:
    - qwen-plus
skills:
  - accessibility-compliance
  - agent-development
  - airflow-dag-patterns
  # ... todas las skills adaptadas
tags:
  - qwen-code
  - developer-tools
  - code-review
  - testing
  - security
```

### RF10: Eliminación de Directorios de Otros Editores

**Directorios a Eliminar:**
- `.claude/`
- `.claude-plugin/`
- `.codex/`
- `.codex-plugin/`
- `.cursor/`
- `.kiro/`
- `.trae/`
- `.codebuddy/`
- `.opencode/`
- `.gemini/`
- `.agents/plugins/` (si existe)

**Directorios a Mantener:**
- `.agents/` (nuevo, para agents Qwen Code)
- `.qwen/` (nuevo, para configuración Qwen Code)
- `agents/` (original, mantener como referencia hasta completar migración)
- `skills/` (original, mantener como referencia hasta completar migración)
- `commands/` (original, mantener como referencia hasta completar migración)
- `hooks/` (original, mantener como referencia hasta completar migración)
- `rules/` (original, mantener como referencia hasta completar migración)
- `mcp-configs/` (original, mantener como referencia hasta completar migración)

---

## Requisitos No Funcionales

### RNF1: Compatibilidad con Qwen Code

Todos los componentes deben ser 100% compatibles con Qwen Code:
- Agents deben usar formato YAML frontmatter con `description` incluyendo `<example>` blocks
- Skills deben usar formato `SKILL.md` con frontmatter YAML
- Commands deben usar formato `COMMAND.md` con frontmatter YAML
- Hooks deben usar formato `HOOK.md` con frontmatter YAML

### RNF2: Preservación de Funcionalidad

Cada componente migrado debe mantener la misma funcionalidad que su versión original:
- Mismas capacidades
- Mismos triggers/condiciones
- Mismos outputs esperados

### RNF3: Calidad de Código

- Todos los scripts deben pasar linting
- Tests deben pasar con 80%+ coverage
- Documentación debe estar actualizada
- No hardcoded paths o secrets

### RNF4: Performance

- Agents deben cargar en < 2 segundos
- Skills deben ejecutarse sin overhead significativo
- Hooks no deben bloquear el flujo de trabajo

---

## Diseño de Arquitectura

### Estructura Final del Repositorio

```
everything-qwen-code/
├── .agents/                          # Agents en formato Qwen Code (36 archivos)
│   ├── architect.md
│   ├── planner.md
│   ├── code-reviewer.md
│   └── ... (33 más)
├── .qwen/                            # Configuración Qwen Code
│   ├── skills/                       # 151 skills migradas
│   │   ├── accessibility-compliance/
│   │   │   └── SKILL.md
│   │   ├── agent-development/
│   │   │   └── SKILL.md
│   │   └── ... (149 más)
│   ├── commands/                     # 68 commands migrados
│   │   ├── create-skill/
│   │   │   └── COMMAND.md
│   │   └── ... (67 más)
│   ├── hooks/                        # Hooks migrados
│   │   ├── security-scan/
│   │   │   └── HOOK.md
│   │   └── ... (más)
│   ├── rules/                        # Rules migradas
│   │   ├── common/
│   │   ├── python/
│   │   ├── typescript/
│   │   └── ...
│   └── mcp-configs/                  # MCP configs migrados
│       ├── github.json
│       ├── context7.json
│       └── ...
├── contexts/                         # Context files (sin cambios)
├── docs/                             # Documentación
│   ├── superpowers/
│   │   └── specs/
│   │       └── 2026-04-02-everything-qwen-code-migration-design.md
│   └── ...
├── examples/                         # Ejemplos de uso
├── manifests/                        # Manifests de instalación
├── mcp-configs/                      # MCP configs source (referencia)
├── plugins/                          # Plugins
├── research/                         # Investigación
├── rules/                            # Rules source (referencia)
├── schemas/                          # JSON schemas
├── scripts/                          # Scripts utilitarios (adaptados)
├── skills/                           # Skills source (referencia)
├── tests/                            # Test suite (actualizada)
├── .gitignore                        # Actualizado
├── .mcp.json                         # MCP config root
├── AGENTS.md                         # Documentación de agents
├── agent.yaml                        # Agent config principal
├── CHANGELOG.md                      # Historial de cambios
├── CONTRIBUTING.md                   # Guía de contribución
├── package.json                      # Configuración npm
├── README.md                         # README principal
└── VERSION                           # Versión (1.0.0)
```

### Flujo de Migración

```
┌─────────────────────────────────────────────────────────────┐
│                    FASE 1: PREPARACIÓN                       │
├─────────────────────────────────────────────────────────────┤
│ 1. Crear estructura de directorios .qwen/                   │
│ 2. Crear estructura de directorios .agents/                 │
│ 3. Copiar archivos base (contexts, docs, examples, etc.)    │
│ 4. Actualizar .gitignore                                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   FASE 2: AGENTS (36)                        │
├─────────────────────────────────────────────────────────────┤
│ 1. Leer cada agent de agents/*.md                           │
│ 2. Reescribir frontmatter (description con ejemplos)        │
│ 3. Asignar color por tipo                                   │
│ 4. Adaptar system prompt al formato Qwen Code               │
│ 5. Guardar en .agents/*.md                                  │
│ 6. Validar formato                                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   FASE 3: SKILLS (151)                       │
├─────────────────────────────────────────────────────────────┤
│ 1. Leer cada skill de skills/<nombre>/                      │
│ 2. Crear carpeta .qwen/skills/<nombre>/                     │
│ 3. Crear SKILL.md con frontmatter YAML                      │
│ 4. Adaptar contenido para Qwen Code                         │
│ 5. Validar formato                                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   FASE 4: COMMANDS (68)                      │
├─────────────────────────────────────────────────────────────┤
│ 1. Leer cada command de commands/<nombre>/                  │
│ 2. Crear carpeta .qwen/commands/<nombre>/                   │
│ 3. Crear COMMAND.md con frontmatter YAML                    │
│ 4. Adaptar para Qwen Code                                   │
│ 5. Validar formato                                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    FASE 5: HOOKS                             │
├─────────────────────────────────────────────────────────────┤
│ 1. Leer hooks de hooks/ y .claude/hooks/                    │
│ 2. Crear carpeta .qwen/hooks/<nombre>/                      │
│ 3. Crear HOOK.md con frontmatter YAML                       │
│ 4. Adaptar eventos y condiciones                            │
│ 5. Validar formato                                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    FASE 6: RULES                             │
├─────────────────────────────────────────────────────────────┤
│ 1. Copiar rules/ a .qwen/rules/                             │
│ 2. Actualizar referencias a Claude Code                     │
│ 3. Validar formato                                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  FASE 7: MCP CONFIGS                         │
├─────────────────────────────────────────────────────────────┤
│ 1. Copiar mcp-configs/ a .qwen/mcp-configs/                 │
│ 2. Actualizar .mcp.json root                                │
│ 3. Validar configuración                                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   FASE 8: DOCUMENTACIÓN                      │
├─────────────────────────────────────────────────────────────┤
│ 1. Actualizar README.md                                     │
│ 2. Actualizar AGENTS.md                                     │
│ 3. Actualizar CHANGELOG.md                                  │
│ 4. Actualizar CONTRIBUTING.md                               │
│ 5. Actualizar resto de docs                                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   FASE 9: SCRIPTS                            │
├─────────────────────────────────────────────────────────────┤
│ 1. Actualizar scripts para Qwen Code                        │
│ 2. Actualizar package.json                                  │
│ 3. Actualizar agent.yaml                                    │
│ 4. Actualizar tests                                         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   FASE 10: LIMPIEZA                          │
├─────────────────────────────────────────────────────────────┤
│ 1. Eliminar directorios de otros editores                   │
│ 2. Eliminar archivos obsoletos                              │
│ 3. Actualizar .gitignore                                    │
│ 4. Ejecutar tests finales                                   │
│ 5. Commit inicial                                           │
└─────────────────────────────────────────────────────────────┘
```

---

## Trade-Off Analysis

### Decisión 1: Mantener vs Eliminar Directorios Originales

**Opción A: Eliminar inmediatamente**
- ✅ Pros: Repositorio limpio desde el inicio
- ❌ Contras: Pérdida de referencia durante migración

**Opción B: Mantener como referencia (Recomendada)**
- ✅ Pros: Referencia disponible durante migración
- ✅ Pros: Permite migración incremental
- ❌ Contras: Repositorio más grande temporalmente

**Decisión:** Opción B - Mantener directorios originales hasta completar migración, luego eliminar en Fase 10.

### Decisión 2: Migración Manual vs Automatizada

**Opción A: Scripts de conversión automática**
- ✅ Pros: Más rápido, consistente
- ❌ Contras: Complejo de implementar, puede perder matices

**Opción B: Migración manual con asistencia AI**
- ✅ Pros: Mayor calidad, atención a detalles
- ✅ Pros: Oportunidad de mejorar cada componente
- ❌ Contras: Más lento

**Decisión:** Opción B - Migración manual con asistencia AI para mayor calidad.

### Decisión 3: Versión Inicial

**Opción A: Mantener versión 1.9.0**
- ✅ Pros: Continuidad con histórico
- ❌ Contras: Confuso (es un producto diferente)

**Opción B: Reiniciar a 1.0.0 (Recomendada)**
- ✅ Pros: Claro que es un producto nuevo
- ✅ Pros: Permite nuevo changelog
- ❌ Contras: Pierde continuidad numérica

**Decisión:** Opción B - Versión 1.0.0 para Everything Qwen Code.

---

## Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Pérdida de funcionalidad en migración | Media | Alto | Tests exhaustivos por componente |
| Formato Qwen Code incorrecto | Baja | Alto | Validar con agente `system-architect` ya creado |
| Scripts incompatibles | Media | Medio | Adaptar incrementalmente, testear cada uno |
| Documentación desactualizada | Alta | Bajo | Revisión final completa |
| Paths hardcodeados en scripts | Media | Medio | Búsqueda y reemplazo global |
| Tests fallan por cambios | Alta | Medio | Actualizar tests junto con código |

---

## Plan de Implementación

### Fase 1: Preparación (1-2 horas)
- [ ] Crear `.agents/` directorio
- [ ] Crear `.qwen/` directorio con subdirectorios
- [ ] Copiar archivos base
- [ ] Actualizar `.gitignore`

### Fase 2: Agents (4-6 horas)
- [ ] Migrar 36 agents a formato Qwen Code
- [ ] Validar formato de cada agent
- [ ] Testear triggering de agents

### Fase 3: Skills (8-12 horas)
- [ ] Migrar 151 skills a `.qwen/skills/`
- [ ] Adaptar frontmatter y contenido
- [ ] Validar formato

### Fase 4: Commands (3-4 horas)
- [ ] Migrar 68 commands a `.qwen/commands/`
- [ ] Adaptar formato
- [ ] Validar

### Fase 5: Hooks (2-3 horas)
- [ ] Migrar hooks a `.qwen/hooks/`
- [ ] Adaptar eventos
- [ ] Validar

### Fase 6: Rules (1-2 horas)
- [ ] Copiar rules a `.qwen/rules/`
- [ ] Actualizar referencias
- [ ] Validar

### Fase 7: MCP Configs (1 hora)
- [ ] Copiar MCP configs
- [ ] Actualizar `.mcp.json`
- [ ] Validar

### Fase 8: Documentación (3-4 horas)
- [ ] Actualizar README.md
- [ ] Actualizar AGENTS.md
- [ ] Actualizar CHANGELOG.md
- [ ] Actualizar resto de docs

### Fase 9: Scripts (2-3 horas)
- [ ] Actualizar package.json
- [ ] Actualizar agent.yaml
- [ ] Adaptar scripts
- [ ] Actualizar tests

### Fase 10: Limpieza (1-2 horas)
- [ ] Eliminar directorios obsoletos
- [ ] Limpieza final
- [ ] Tests finales
- [ ] Commit inicial

**Total estimado:** 25-35 horas

---

## Criterios de Aceptación

### Agents
- [ ] 36 agents en `.agents/` con formato Qwen Code
- [ ] Cada agent tiene `description` con 2-4 ejemplos `<example>`
- [ ] Cada agent tiene `color` asignado
- [ ] System prompts estructurados correctamente

### Skills
- [ ] 151 skills en `.qwen/skills/<nombre>/SKILL.md`
- [ ] Frontmatter YAML completo (name, description, version)
- [ ] Contenido adaptado para Qwen Code

### Commands
- [ ] 68 commands en `.qwen/commands/<nombre>/COMMAND.md`
- [ ] Frontmatter YAML completo
- [ ] Funcionalidad preservada

### Hooks
- [ ] Hooks en `.qwen/hooks/<nombre>/HOOK.md`
- [ ] Eventos y condiciones correctos

### Rules
- [ ] Rules en `.qwen/rules/`
- [ ] Referencias actualizadas a Qwen Code

### Documentación
- [ ] README.md actualizado
- [ ] AGENTS.md actualizado
- [ ] CHANGELOG.md con nueva sección Qwen Code
- [ ] Resto de docs actualizados

### Tests
- [ ] Todos los tests pasan
- [ ] 80%+ code coverage
- [ ] Scripts de validación pasan

---

## Anexos

### Anexo A: Lista Completa de Skills (151)

[Lista completa disponible en el repositorio original - skills/]

### Anexo B: Lista Completa de Commands (68)

[Lista completa disponible en el repositorio original - commands/]

### Anexo C: Referencias

- Skill `Agent Development` en `C:\Users\informatica\.qwen\skills\Agent Development\SKILL.md`
- Agent `system-architect` en `C:\Users\informatica\.qwen\agents\system-architect.md`
- Skill `brainstorming` en `C:\Users\informatica\.qwen\skills\brainstorming\SKILL.md`

---

## Historial de Revisiones

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0 | 2026-04-02 | AI Assistant | Versión inicial |
