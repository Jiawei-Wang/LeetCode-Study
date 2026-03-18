Mock 2: service orchestration

The Setup
In a production environment for Oura, a single "Accident Prediction" might actually be the result of multiple specialized ML models running in parallel (e.g., one for Falls, one for Faints, and one for Seizures). Your job is to build the "Consensus Engine" that talks to these models and makes a final decision.

The Problem
You need to implement an asynchronous function that fetches scores from three different model APIs. Because this is an emergency detection system, latency is life-critical.