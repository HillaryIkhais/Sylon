# DSN X BCT LLM Agent Challenge — Task A Solution Paper
**Team Name:** Cascade
**Candidate Name:** Ikhais Hillary
**Project Name:** Sylon
**Task:** Task A (User Modeling)

1. Overview

Most recommendation and user-modeling systems treat people like static data points — vectors, scores, or rows in a matrix. But real people are inconsistent. Their preferences change, emotions affect decisions, and context matters.

Sylon approaches this differently through what I call Grounded Generative Personas.

Instead of building rigid user profiles from ratings alone, Sylon analyzes raw customer reviews from datasets like JSON, CSV, PDFs, or plain text and turns them into realistic behavioral personas. The goal is not just to know what users like, but why they react the way they do.

What makes this especially important is the Nigerian context. Customer behavior here is shaped by things many traditional systems completely ignore — patience for delays, expectations around service, environmental issues like generator noise, communication tone, and even local slang like abeg or omo. Sylon reflects those realities directly in the generated personas.


---

2. System Architecture — Behavioral Synthesis Engine

Sylon uses a multi-agent architecture designed to keep outputs flexible while still grounded in real customer data.

The Archaeologist Agent

The first stage is handled by the Archaeologist Agent.

When a business uploads customer reviews, the system breaks the data into chunks and processes them through a Map-Reduce pipeline using large language models like Cerebras Llama-3 and Qwen.

From this, the system extracts recurring complaints, compliments, emotional patterns, and behavioral trends. It then builds structured persona objects containing:

A narrative personality profile based on real reviews

Behavioral changes over time

Rating behavior and consistency

Direct grounding quotes pulled from the dataset


For example, a persona might begin as someone tolerant of slow delivery but gradually become more impatient after repeated bad experiences. These shifts are captured as part of the user model instead of being ignored.


---

The Simulator Agent

Once personas are generated, the Simulator Agent predicts how those personas would react to a new product, service, or business scenario.

The system performs what Sylon calls a Collision Analysis — comparing the behavioral profile of the persona against the unseen scenario.

Using the persona’s narrative traits and grounded review history, the Simulator predicts likely friction points, emotional tone, and star ratings while staying consistent with the user’s historical behavior.

The result is a simulated review that feels realistic because it is tied directly to real patterns extracted from the dataset.


---

3. Handling API Limits and Failover

Processing large datasets can easily trigger API quota errors, especially during high-volume ingestion.

To avoid interruptions, Sylon includes an automatic failover system. If Cerebras reaches its token quota limit, requests are automatically rerouted to Gemini 2.0 Flash using exponential backoff and retry logic.

The system also dynamically adjusts response formatting to maintain strict JSON schema consistency across providers. This allows ingestion to continue smoothly even during provider outages or rate limits.


---

4. Evaluation and Behavioral Accuracy

Sylon’s personas remain highly grounded because they are directly tied to:

Verbatim customer quotes

Historical ratings

Consistent behavioral patterns extracted from the dataset


The system does not invent random personality traits or reactions. Instead, it projects known preferences and frustrations onto new scenarios to simulate believable customer responses.

This produces outputs that feel significantly more human, culturally aware, and context-sensitive than traditional recommendation systems.

To test Task A inside Sylon, open the Chat interface and select “Simulate Audience Reaction.”