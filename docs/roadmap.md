# Jansori + Hermes Agent Unified Roadmap

## Vision

Build a persistent AI ecosystem composed of:

- **Jansori (잔소리)** → emotionally persistent personal companion & behavior coach
- **Hermes Agent** → action-oriented autonomous execution agent
- **Shared Memory + Infrastructure** → unified intelligence layer across all interfaces

The long-term goal is to create a deeply personalized AI operating layer that can remember, reason, plan, execute, monitor, and proactively intervene across daily life and work.

---

## Phase 0 — Foundation & System Architecture

**Goal:** Establish the technical and operational foundation for a scalable multi-agent ecosystem.

**Action Items:**
- Define service boundaries between Jansori, Hermes, and Shared Memory
- Create a unified architecture diagram and API contracts between services
- Configure Docker-based local development and deployment environments
- Build environment variable management, secrets handling, and a CI/CD workflow
- Create logging and observability pipeline
- Set up OpenAI API integration with multi-model routing, cost tracking, and prompt versioning
- Define tool calling abstraction and agent orchestration strategy
- Design long-term memory architecture with vector database, semantic retrieval, and episodic vs semantic memory separation

**Acceptance Criteria:**
- A developer can clone the repo, run one command, and have a working local environment
- Service boundaries and API contracts are documented and agreed upon
- Logs and basic observability are operational
- The AI integration layer can route prompts and track costs

---

## Phase 1 — Jansori MVP (Conversational Companion)

**Goal:** Launch the first usable version of Jansori focused on conversation, reminders, and emotional continuity.

**Action Items:**
- Build a Discord bot connected to the OpenAI API with a working conversation flow
- Implement persistent memory so Jansori recalls past interactions
- Define Jansori's personality profile and "nagging" timing logic
- Create an adaptive emotional tone system balancing encouragement and accountability
- Add a daily check-in system and reminder scheduler
- Implement command structure and configuration system
- Deploy to cloud with monitoring, uptime alerts, and error recovery

**Acceptance Criteria:**
- Jansori can hold a multi-turn conversation in Discord and recall past context
- Reminders fire on schedule and adapt based on user behavior
- Personality feels consistent — slightly annoying but caring, not robotic
- System runs 24/7 with automatic recovery from failures

---

## Phase 2 — Habit, Health & Behavioral Intelligence

**Goal:** Transform Jansori into a behavior-aware lifestyle operating assistant.

**Action Items:**
- Build habit tracking architecture covering workouts, sleep, and nutrition
- Implement streak engine, weekly/monthly review reports, and behavioral scoring
- Integrate with Apple HealthKit and Apple Watch for auto-detection of workouts and inactivity
- Build recovery and fatigue awareness into reminder logic
- Detect recurring unhealthy patterns and productivity cycles
- Create adaptive intervention timing and personalized nudging intensity
- Generate weekly coaching summaries

**Acceptance Criteria:**
- Jansori automatically detects and logs workouts and sleep without manual input
- Weekly reports accurately reflect habit streaks and behavioral trends
- Nudging frequency adapts based on observed patterns, not a fixed schedule
- Users receive a meaningful weekly coaching summary grounded in their actual data

---

## Phase 3 — Hermes Agent (Execution Agent)

**Goal:** Build Hermes as an autonomous execution layer capable of planning and acting on behalf of the user.

**Action Items:**
- Design Hermes architecture with a task planning engine, multi-step execution flow, and async task queue
- Implement tool orchestration with autonomous retry/recovery and an agent state machine
- Integrate with Gmail, Google Calendar, Notion, Slack/Discord, GitHub, and web browsing
- Build productivity automation: meeting summaries, email triage, calendar planning, research automation, follow-up generation
- Implement permission boundaries, human approval workflows, action logging, and failure rollback strategies

**Acceptance Criteria:**
- Hermes can complete a multi-step task (e.g., research → summarize → draft email) end-to-end without manual intervention
- All actions are logged with rollback available for reversible operations
- Human approval is required before any destructive or high-stakes action
- Integrations with at least Gmail, Google Calendar, and Notion are functional

---

## Phase 4 — Unified Personal AI System

**Goal:** Connect Jansori and Hermes into a shared intelligence platform that acts as a cohesive personal AI operating system.

**Action Items:**
- Build a unified memory graph and shared context engine accessible by both agents
- Implement cross-agent communication: Jansori → Hermes delegation and Hermes → Jansori reporting
- Build shared preference modeling, scheduling awareness, and a unified event timeline
- Implement a priority arbitration system and long-horizon planning
- Create daily briefing generation, a life dashboard, and personal analytics
- Build a goal tracking engine with energy/productivity forecasting and context-aware intervention

**Acceptance Criteria:**
- Jansori can delegate tasks to Hermes and receive status updates seamlessly
- Both agents share the same memory and context without duplication or conflict
- Users receive a daily briefing that synthesizes behavioral data, calendar, and task state
- The system can track multi-week goals and proactively surface when they're at risk

---

## Phase 5 — Voice, Presence & Companion Experience

**Goal:** Make the system feel alive, ambient, and continuously present across voice and UI surfaces.

**Action Items:**
- Build a speech-to-text and text-to-speech pipeline with real-time voice interaction
- Implement wake-word detection and emotional voice modulation
- Add Korean/English bilingual support
- Design an avatar system with emotional expression and ambient interaction behaviors
- Build retro-inspired UI with companion interaction loops and presence-aware notifications
- Create desktop app, mobile companion app, and explore wearable/smart home integrations

**Acceptance Criteria:**
- Users can have a full voice conversation with Jansori with under 1s response latency
- Emotional tone is reflected audibly and visually in the companion's responses
- The system supports natural switching between Korean and English mid-conversation
- At least one client (desktop or mobile) ships with a usable companion UI

---

## Phase 6 — Physical AI Companion Device

**Goal:** Create a dedicated hardware device that embodies the system as a physical ambient companion.

**Action Items:**
- Build on Raspberry Pi with embedded Linux, microphone/speaker stack, and local networking
- Implement sensor integrations and an embedded display
- Add always-on, desk companion, and bedside modes
- Build environmental awareness and local wake-word processing
- Experiment with edge inference for low-latency local responses
- Design a physical enclosure with a minimal companion aesthetic and lighting/expression system

**Acceptance Criteria:**
- Device boots reliably, responds to wake-word, and maintains a persistent connection to the AI backend
- At least two ambient modes (desk and bedside) are functional and switch automatically
- Physical design is intentional — not a generic Raspberry Pi box
- Edge inference handles at least simple interactions without round-tripping to the cloud

---

## Continuous Research & Learning

**Goal:** Stay current with the AI/LLM landscape and deepen engineering and product skills to support the project's evolution.

**Action Items:**
- Research and prototype agent architectures, RAG systems, long-term memory systems, and multi-agent coordination patterns
- Study voice pipeline architectures and AI companion UX patterns
- Deepen engineering skills in system scalability, observability, security, infrastructure automation, and data pipelines
- Explore human-AI interaction patterns, emotional design, behavioral psychology, and personal knowledge systems

**Acceptance Criteria:**
- Each research area has a documented summary of findings and a clear link to how it informs the project
- At least one prototype or proof-of-concept is built per major research topic before it is incorporated into a phase

---

## Operating Principles

### Product Direction
- Persistent memory first
- Emotional continuity over gimmicks
- Execution reliability over complexity
- Human-in-the-loop by default
- Modular multi-agent architecture
- Personalization through long-term interaction

### Technical Principles
- API-first architecture
- Tool abstraction layers
- Strong observability
- Separation of memory and execution
- Gradual autonomy expansion
- Privacy-aware design

---

## North Star

Create an AI system that understands the user deeply, remembers continuously, proactively helps, executes reliably, grows more personalized over time, and feels emotionally persistent rather than transactional.
