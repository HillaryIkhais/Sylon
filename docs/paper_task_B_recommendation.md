# DSN X BCT LLM Agent Challenge: Task B Solution Paper
**Team Name:** Cascade
**Team/Candidate:** Ikhais Hillary
**Project:** Sylon
**Task:** Task B (Recommendation)


## 1. Overview
Traditional recommendation systems depend heavily on collaborative filtering and user item interaction data. While effective at scale, these systems struggle with two major problems:
They cannot explain why a recommendation was made

They perform poorly during cold start situations where little or no user data exists

Sylon approaches recommendation as a contextual reasoning problem rather than a ranking problem. Using the personas and behavioral insights generated in Task A, Sylon’s Strategist Agent recommends products, business decisions, and operational improvements through conversational reasoning instead of static scoring systems.

The goal is not just to recommend something relevant, but to explain the reasoning behind it in a way businesses can actually understand and act on.


## 2. System Architecture — Contextual Recommendation Workflow
Every recommendation request first passes through the Intent Router, powered by Gemini 2.0 Flash.

The router checks recent conversation history to understand context and determine what the user is trying to achieve. Once the request is classified as a recommendation task, it routes the request to the recommendation engine.

This allows the system to maintain conversational continuity instead of treating every request as isolated.

--The Recommendation Engine
The recommendation engine combines:
Business context

Extracted customer pain points

Generated behavioral personas

These are injected into a tightly controlled prompt for the language model. Instead of relying on embeddings or large interaction matrices, the model reasons directly from customer behavior.

For example, if a persona consistently complains about noise, delays, or poor customer treatment, the system can recommend products or operational changes specifically designed to solve those frustrations.

Recommendations become more than “users also bought this.” They become behavior aware strategic suggestions grounded in customer psychology and local context.

Solving the Cold Start Problem
One of the biggest weaknesses of traditional recommenders is the cold start problem.

Sylon handles this using a Synthetic Persona Factory.
If a business has little or no historical customer data, the business owner simply provides a category and location, for example, “Lounge in Lekki, Lagos.”

From there, Sylon generates realistic, culturally grounded Nigerian customer personas based on likely demographics, spending habits, lifestyle patterns, and local behavior.

Examples include personas like:

“The Tech Bro Remote Worker”

“The Friday Night High Roller”

These synthetic personas allow the system to begin generating meaningful recommendations immediately, even before real customer data exists.


## 3. Conversational Recommendation Experience
Unlike traditional recommendation dashboards, Sylon uses a conversational voice and chat interface powered by ElevenLabs.

The system maintains memory using an active SQLite business session, which allows users to challenge or refine recommendations naturally.

For example, if Sylon suggests creating a premium quiet-zone experience, the business owner can respond with:

> “My space is too small for that.”

The system retains previous context and generates an updated recommendation that better fits the business constraints.

This creates a recommendation experience that feels collaborative rather than static.


## 4. Evaluation
Sylon’s recommendations are grounded directly in extracted customer frustrations, desires, and behavioral patterns.

The system also explains its reasoning transparently. For example:

> “Persona A repeatedly complained about long wait times, so introducing faster service options would likely improve retention.”

Because recommendations are tied to real behavioral evidence, they achieve stronger contextual relevance and are easier for businesses to trust and apply.

To test Task B inside Sylon, open the Chat interface and select “Request Product Recommendations.”

## 5. Roadmap for Future Improvements
*This section addresses the hackathon requirement regarding "what could be done with more time."*

While the current architecture successfully validates the concept of LLM-driven behavioral modeling, deploying Sylon at an enterprise scale requires several architectural upgrades. If given more time, we would implement the following roadmap:

### 1. Enterprise Telecom Integration (Offline Data Ingestion)
**The Problem:** Currently, Sylon relies on CSV uploads or digital review platforms, excluding a massive portion of the Nigerian informal economy.
**The Improvement:** We would integrate **Telecom APIs (USSD / SMS)** directly into the Ingestion Engine. Customers could text a shortcode (e.g., *123*5#) after visiting a business to leave an SMS review. Sylon would automatically transcribe, translate (handling Pidgin and dialects), and ingest this offline data into the persona-generation pipeline in real-time.

### 2. Event-Driven Architecture (Real-Time Streaming)
**The Problem:** The current system uses batch-processing via a REST API, introducing latency if a business uploads massive datasets at once.
**The Improvement:** Transition the backend to an event-driven microservices architecture using **Apache Kafka** or **RabbitMQ**. Customer feedback streams would be published to topics, allowing the Map-Reduce agents to process data asynchronously.

### 3. Migration to a Native Vector Database (RAG Optimization)
**The Problem:** Sylon currently persists behavioral data in a local SQLite database (`persistence.py`), which bottlenecks semantic querying at scale.
**The Improvement:** Implement a dedicated Vector Database (e.g., **Pinecone** or **Milvus**) alongside a robust Retrieval-Augmented Generation (RAG) pipeline. This would allow Sylon to instantly retrieve highly specific, semantically similar historical reviews to ground the language model's recommendations.

### 4. Multi-Agent Orchestration (Agentic Swarm)
**The Problem:** Currently, Sylon operates as a single "Strategist" agent for recommendations.
**The Improvement:** Upgrade the architecture to a **Multi-Agent Swarm** using frameworks like AutoGen. 
- **The Ops Agent:** Monitors wait-time complaints and recommends supply chain tweaks.
- **The Marketing Agent:** Automatically drafts SMS marketing campaigns specifically tailored to the "Loyalty Skeptic" persona.
These agents would debate each other before presenting a unified recommendation to the business owner.