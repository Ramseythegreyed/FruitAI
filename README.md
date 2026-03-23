r# FruitAI

**AI-powered wrestling booking, talent analytics, and event operations platform**

FruitAI is a domain-focused AI platform for professional wrestling promotions. It combines booking assistance, storyline continuity, roster intelligence, event planning, and collaboration workflows into a modular enterprise-style application.

The platform is designed for promotions that want to improve creative consistency, operational coordination, and decision support using modern AI patterns such as LLM orchestration, retrieval-augmented generation (RAG), embeddings, and agent-based workflows.

---

## Why FruitAI

Professional wrestling promotions operate as complex creative and operational systems. Match cards, storyline progression, talent availability, crowd engagement, promo quality, venue logistics, and internal communication all have to align.

FruitAI is designed to support that environment with:

- AI-assisted match card generation
- storyline memory and continuity checks
- talent utilization and ranking insights
- event prep collaboration workflows
- retrieval over past shows, promos, notes, and booking history
- future-ready integration with collaboration platforms like Webex

---

## Core Capabilities

### 1. Booking Intelligence
- Generate draft match cards based on roster constraints
- Avoid repeat pairings and overused finishes
- Balance main event, midcard, and developmental matches
- Consider heel/face dynamics and faction alignment

### 2. Storyline Continuity
- Track ongoing feuds, alliances, title scenes, and unresolved angles
- Flag continuity breaks before publishing a card
- Provide creative rationale for recommended match progression

### 3. Talent Analytics
- Score talent momentum based on recent usage
- Evaluate promo sentiment and crowd reaction indicators
- Surface underutilized roster members for creative review

### 4. Collaboration and Event Ops
- Prepare show run sheets
- Integrate event planning hooks for collaboration platforms
- Support future Webex-based show prep, talent check-ins, and production communications

### 5. Retrieval-Augmented Creative Search
- Search prior events, promo transcripts, booking notes, and show summaries
- Use vector similarity to provide context-aware suggestions
- Reduce storyline duplication and creative drift

---

## Example Use Cases

- Generate a weekly event card for a regional promotion
- Review title-feud continuity before finalizing the main event
- Identify which wrestlers are losing momentum due to inconsistent use
- Summarize promo tone and audience response from transcript data
- Search the last six months of booking notes before starting a new feud
- Build collaboration hooks for distributed production teams planning live events

---

## Architecture Overview

```text
                   +----------------------+
                   |   Web / API Clients  |
                   +----------+-----------+
                              |
                              v
                    +--------------------+
                    |   FastAPI Gateway  |
                    +----+----+----+-----+
                         |    |    |
          +--------------+    |    +------------------+
          |                   |                       |
          v                   v                       v
+----------------+  +-------------------+  +--------------------+
| Booking Engine |  | Storyline Agent   |  | Collaboration APIs |
| Constraints    |  | Continuity Memory |  | Webex / Webhooks   |
+-------+--------+  +---------+---------+  +---------+----------+
        |                     |                      |
        v                     v                      v
+----------------+  +-------------------+  +--------------------+
| Talent Models  |  | RAG / Vector Store|  | Event Ops Services |
| Rankings       |  | Past Shows / Notes|  | Run Sheets / Tasks |
+----------------+  +-------------------+  +--------------------+m
