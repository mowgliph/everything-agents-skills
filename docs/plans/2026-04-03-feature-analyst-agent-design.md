# Feature Analyst Agent Design

## Date: 2026-04-03

## Context
The project has 36 specialized agents but lacks a dedicated feature analysis specialist. Users need an expert in feature research across code, product, and technical dimensions.

## Decision
Create `feature-analyst` agent following the established pattern (single `.md` file in `.agents/`).

## Design

### Agent Purpose
Comprehensive feature research and analysis specialist covering:
1. **Code Feature Analysis** - Patterns, quality, technical debt, improvements
2. **Product Feature Research** - Competitive analysis, market positioning, user needs
3. **Technical Feature Evaluation** - Feasibility, complexity, dependencies, risks

### File Structure
```
.agents/feature-analyst.md  (new agent config)
```

### Agent Configuration
- **Name**: feature-analyst
- **Description**: Specialist in feature research, analysis, and evaluation across code, product, and technical dimensions
- **Color**: purple (distinguishing from blue planners/architects and red security)
- **Type**: Research & Analysis agent

### Capabilities
- Feature pattern recognition and classification
- Competitive landscape analysis
- Technical feasibility assessment
- Feature prioritization frameworks
- Risk identification and mitigation
- Implementation complexity estimation
- Market positioning evaluation
- User needs assessment

### Analysis Framework
1. **Discovery** - Gather context, understand requirements
2. **Research** - Investigate existing implementations, competitors
3. **Evaluation** - Assess feasibility, complexity, value
4. **Recommendation** - Provide actionable insights with trade-offs
5. **Documentation** - Create structured analysis reports

### Integration
- Leverages existing 323 skills for domain knowledge
- Complements `planner` (implementation) and `architect` (system design)
- Focuses specifically on feature analysis and research

## Consequences

### Positive
- Fills gap in agent ecosystem
- Provides specialized feature expertise
- Consistent with existing agent patterns
- Easy to maintain and enhance

### Negative
- Adds one more agent to manage
- May overlap slightly with general-purpose for basic research

### Alternatives Considered
- **Approach B**: Agent + custom skills bundle (more complex, deferred)
- **Approach C**: Agent + evaluation framework (significant effort, deferred)

## Status
Approved - Ready for implementation
