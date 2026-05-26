# Architecture Overview

## System Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Interfaces                        │
│  Telegram / Discord  │  Voice (STT/TTS)  │  Desktop / Mobile   │
│       Bot            │    Wake-word       │    Companion App    │
│                      │                   │                      │
│              [ Phase 0–1 ]          [ Phase 5 ]                 │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                  ┌────────▼────────┐
                  │   API Gateway   │  (request routing, auth)
                  └────────┬────────┘
                           │
           ┌───────────────┼───────────────┐
           │                               │
  ┌────────▼────────┐             ┌────────▼────────┐
  │    Jansori      │             │     Hermes      │
  │   (Companion)   │◄───────────►│  (Exec Agent)   │
  │                 │  delegation │                 │
  │  - Personality  │             │  - Task planner │
  │  - Reminders    │             │  - Tool caller  │
  │  - Check-ins    │             │  - Async queue  │
  │  - Nudging      │             │  - Approval flow│
  └────────┬────────┘             └────────┬────────┘
           │                               │
           └───────────┬───────────────────┘
                       │
          ┌────────────▼────────────┐
          │     Shared Memory       │
          │                         │
          │  - Vector DB (semantic) │
          │  - Episodic memory      │
          │  - User preference      │
          │  - Unified event log    │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │    LLM / AI Layer       │
          │                         │
          │  - Multi-model routing  │
          │  - Prompt versioning    │
          │  - Cost tracking        │
          │  - Tool abstraction     │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │   External Integrations │
          │                         │
          │  Gmail · Calendar       │
          │  Notion · GitHub        │
          │  Apple HealthKit        │
          │  Slack / Telegram       │
          └─────────────────────────┘
```

## Core Components

### Jansori (Companion Agent)
Emotionally persistent personal companion. Handles conversation, habit accountability, reminders, and daily check-ins.

- **Personality engine** — consistent tone, adaptive nagging intensity
- **Reminder scheduler** — time-based and behavior-triggered notifications
- **Behavioral scoring** — habit streaks, recovery awareness
- Delegates executable tasks to Hermes

### Hermes (Execution Agent)
Action-oriented autonomous agent. Executes multi-step tasks across external services.

- **Task planner** — breaks goals into steps, manages state machine
- **Tool orchestrator** — calls external APIs with retry/recovery
- **Approval workflow** — human-in-the-loop for high-stakes actions
- **Async task queue** — non-blocking execution with status reporting back to Jansori

### Shared Memory Layer
Central intelligence store accessible by both agents.

| Store | Purpose |
|---|---|
| Vector DB | Semantic search over past conversations and facts |
| Episodic memory | Timestamped event log (what happened, when) |
| Semantic memory | Distilled facts about user (preferences, patterns) |
| Preference model | Behavioral profile, scheduling awareness |

### LLM / AI Layer
Model routing and abstraction between agents and external LLM APIs.

- Multi-model routing (task complexity → model selection)
- Prompt versioning and A/B tracking
- Per-request cost tracking
- Tool calling abstraction shared by both agents

## Directory Structure (target)

```
jansori-assistant/
├── agents/
│   ├── jansori/          # Companion logic, personality, reminders
│   └── hermes/           # Task planning, tool execution, approval
├── memory/               # Vector DB client, memory read/write layer
├── llm/                  # Model routing, prompt registry, cost tracking
├── integrations/         # Per-service adapters (Telegram, Gmail, etc.)
├── interfaces/
│   ├── telegram/         # Bot adapter
│   ├── discord/          # Bot adapter
│   └── voice/            # STT/TTS pipeline (Phase 5)
├── infra/                # Docker, CI/CD, observability
├── docs/                 # Project documentation
└── main.py               # Entry point
```

## Interfaces

| Interface | Phase | Role |
|---|---|---|
| Telegram bot | 0 | Early prototype, ping/notifications |
| Discord bot | 1 | Primary Jansori MVP channel |
| Voice (STT/TTS) | 5 | Ambient companion interaction |
| Desktop/Mobile app | 5 | Companion UI |
| Physical device | 6 | Raspberry Pi embodied companion |

## Infrastructure

- **Local dev** — Docker Compose for services and dependencies
- **Secrets** — `.env` / secrets manager, never committed
- **Observability** — structured logging, uptime alerts, error recovery
- **CI/CD** — GitHub Actions for lint, test, deploy

## Key Design Principles

- **API-first** — all inter-component communication via well-defined interfaces
- **Memory and execution are separate** — agents read/write memory; neither owns it
- **Human-in-the-loop by default** — Hermes requires approval for destructive/high-stakes actions
- **Gradual autonomy** — start minimal (ping bot), expand capability per phase
- **Privacy-aware** — personal data stays in controlled storage, never passed raw to third-party logs
