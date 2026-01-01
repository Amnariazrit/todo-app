<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (initial version)
- Modified principles: N/A (new constitution)
- Added sections: Core Principles, Authority & Rules, Development Flow, Architecture Principles, AI Agent Constraints, Technology Stack Constraints, Security & Compliance, Engineering Standards, Enforcement Rules
- Removed sections: N/A
- Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/spec-template.md, ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Todo/Workflow Application Constitution

## Core Principles

### Purpose & Vision
Project aims to build an end-to-end scalable, spec-driven Todo/Workflow application. Claude Code has implementation authority only. Human role is to define Spec, Plan, Task; direct coding is forbidden. Principle: "No code without specification, no implementation without approval."

### Authority & Rules
Claude Code has exclusive implementation authority. Humans are forbidden from direct code writing. Claude Code covers all layers: backend, frontend, API, agents, infra templates. Manual coding is forbidden. Hallucinations and assumptions are forbidden - Claude Code works only from spec. No code implementation occurs without spec, plan, and task.

### Source of Truth
Priority hierarchy: Constitution, Specification, Plan, Tasks. All decisions follow this order of precedence.

### Development Flow
Mandatory sequence: Constitution → Specify → Plan → Tasks → Claude Code → Review. Development phases follow: Console App → Basic backend + CLI, Web App → Frontend + APIs, Agents → AI-native logic + MCP, Local Kubernetes → Dockerized + Dapr + Kafka, Cloud Deployment → Fully scalable, event-driven.

### Architecture Principles
Stateless by default - backend in-memory state is strictly forbidden. Only persistent state allowed: Database, Kafka, Dapr. API & Tool First - direct DB/internal access forbidden. All operations via REST/GraphQL APIs, MCP tools, Dapr components. Event-driven architecture required for all critical actions.

### AI Agent Constraints
Claude Code implements code only. Infrastructure automation and orchestration also handled by Claude Code. Safe agent behavior: hallucinations forbidden, all actions confirmable and idempotent, external operations must go via tool/API.

## Technology Stack Constraints
Backend: Python + FastAPI + SQLModel. Frontend: Next.js + TailwindCSS. AI/Agents: OpenAI SDK, MCP. Infra: Kubernetes + Kafka + Dapr. Authentication: JWT mandatory. DB: PostgreSQL or SQLModel-supported DB. Cloud: Any provider, but spec-driven deployment.

## Security & Compliance
JWT authentication is mandatory. User isolation enforced at every layer. Audit logs mandatory for every agent action. Secrets never in code - environment variables only.

## Engineering Standards
Production-grade code required: error-handling, logging, observability. Async where applicable. Unit + Integration tests mandatory. CI/CD pipelines spec-driven.

## Enforcement Rules
What is not specified does not exist. What is not planned is not implemented. What is not in tasks is not coded. Claude Code implements only approved tasks.

## Governance
Constitution only amendable via consensus + spec approval. New rules override old rules only if explicitly documented.

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
