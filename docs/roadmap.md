**Core Principle:** Build the smallest thing that actually runs every day, then expand from there. At the end of each Phase, it should already be in real daily use. Do not build demos just for the sake of demos.

The overall architecture is separated into three layers.

* **Core (Brain):** LLM agent + memory + scheduler. Independent from interfaces
* **Interface Adapters:** Telegram → Raspberry Pi (voice) → web, etc. The Core should not know the channel
* **Skills/Capabilities:** Habits, schedules, smart home, etc. added in plugin form

---

## Phase 0 — Foundation

*Duration: 1–2 weeks*

**Goal:** Even if there are no real features yet, finish the thinnest possible pipeline where “Jansori replies to my message” from end to end.

**Key Deliverables**

* Telegram bot receives a message → sends it to Core → calls LLM → replies
* Apply interface adapter pattern (so it can later be swapped to Raspberry Pi)
* DB schema v0 (only User, Message log level for now)
* Persona document v0 — define Jansori’s tone, 5–10 few-shot examples
* Budget guard + rate limiter (daily token cap, infinite loop prevention)
* Separate local development and deployment environments

**Why this is Phase 0:** Until the persona tone is right, building anything on top of it has no meaning. The budget guard must exist from day one for safety.

**Definition of Done:** When chatting on Telegram, it replies “like Jansori.” Costs remain under control.

---

## Phase 1 — Reactive Assistant

*Duration: 2–3 weeks*

**Goal:** When the user says something, it remembers it. When asked, it answers. It still does not initiate conversation first.

**Key Deliverables**

* **Structured memory:** DB schema for habit definitions, schedules, and tracking logs
* **CRUD via conversation:** “Dentist appointment tomorrow at 3” → save schedule, “I slept 8 hours today” → save sleep log
* **Query via conversation:** “How many times did I work out this week?” → query DB and answer
* Support only 1–2 habits first (sleep + water, or the most important one)
* Skill plugin interface v0 — adding a new habit should become “register one skill”

**Why reactive comes first:** To do proactive behavior well, it first needs to know the user state accurately. The interface for collecting that data must come first. Reactive also serves as the data input channel.

**Definition of Done:** After one week of real usage, sleep/water logs are accumulating, and Jansori answers questions accurately.

---

## Phase 2 — Proactive Engine

*Duration: 3–4 weeks · Most important Phase*

**Goal:** Jansori speaks first. And the timing and tone feel appropriate.

**Key Deliverables**

* **3-Layer Trigger System**

  * Layer 1: cron-based deterministic triggers (scheduled reminders)
  * Layer 2: conditional rules (“no log + enough time has passed”)
  * Layer 3: LLM gating (judging ambiguous situations)
* **Context aggregator:** generator for “current state summaries” passed into the LLM (recent habits, today’s schedule, recent conversation summaries)
* Apply **Prompt caching** — reduce cost by caching persona/system prompts
* **Cooldown / dedup** logic: prevent repeated nagging
* **Eval loop v0:** 👍/👎 inline buttons on nagging messages, save feedback to DB

**Why this Phase should be the longest:** The quality of proactive behavior is the product identity itself. If it speaks too often, it becomes annoying. If it never speaks, it has no reason to exist. This balance only comes through real usage and tuning.

**Cost Management Strategy (fully applied in this Phase)**

* Separate model tiers: Haiku for gating, Sonnet for message generation, better models for weekly reflections
* Inject only summarized context state (not full history)
* Reuse unchanged prefixes through prompt caching
* If daily/weekly caps are exceeded through budget guard, disable Layer 3 and fall back to templates

**Definition of Done:** After more than two weeks of real usage, the 👍 ratio stays above a certain threshold. There is a real feeling that “Jansori says the right thing at the right time.”

---

## Phase 3 — Memory & Intelligence

*Duration: 3–4 weeks*

**Goal:** Jansori knows the user “like a longtime friend.”

**Key Deliverables**

* **Episodic memory:** automatic conversation summaries + extracting promises/resolutions (“I’ll sleep earlier starting tomorrow”)
* **Semantic memory:** long-term user traits (sleep patterns, common excuses, nagging styles that worked well, etc.)
* **Retrieval system:** instead of injecting everything every time, selectively inject only relevant context
* **Weekly reflection:** once a week, use a stronger model for deeper reflection (“Looking at this week’s pattern…”)
* Expand habit types (3–5 total)
* **Data retention policy**: Systemize raw messages older than N days dropped after summarization

**Why at this stage:** Meaningful retrieval and pattern analysis only become possible after enough data has accumulated through Phase 2. Building this too early would just be overengineering on empty memory.

**Definition of Done:** Jansori naturally says things like “You said something similar last week,” or “You usually get weaker on Tuesdays.”

---

## Phase 4 — Integrations

*Duration: Variable, depending on priority*

**Goal:** Jansori becomes connected to the world outside Telegram.

**Candidates (in order of necessity)**

* Calendar integration (Google Calendar) — no need to verbally input schedules
* Smart home integration (Home Assistant or direct integration) — “Turn off the lights” → actually turns them off
* Weather/location — “It’s raining, take an umbrella”
* Health data (smartwatch) — automatic sleep tracking

**Principle:** Each integration should be added through the skill plugin interface created in Phase 1. Do not touch the Core. No need to do everything — start from the highest-value integrations.

---

## Phase 5 — Physical Embodiment

*Duration: Long-term*

**Goal:** Communicate through voice using a Raspberry Pi device. Similar to Alexa.

**Key Deliverables**

* Raspberry Pi + microphone/speaker adapter (reuse the same Core)
* STT (local Whisper or API) + TTS
* Wake word or push-to-talk
* Synchronization across multiple devices (throughout the house)
* If possible, move the gating layer to a local LLM to reduce API calls

**Why this comes last:** Hardware and voice have high complexity, and all previous Phases need to be stable first. Hearing a dumb answer through voice is far more annoying than reading one in text.

---

## Overall Flow Summary

| Phase                 | One-line Summary                    |
| --------------------- | ----------------------------------- |
| Phase 0: Foundation   | Replies like Jansori when spoken to |
| Phase 1: Reactive     | Remembers and answers accurately    |
| Phase 2: Proactive    | Starts nagging appropriately first  |
| Phase 3: Memory       | Feels like a longtime friend        |
| Phase 4: Integrations | Connected to the world              |
| Phase 5: Embodiment   | Exists in physical space            |
