Mock 3: The Incident Deduplicator (State & Storage)

In a real-world scenario, if a user falls, their Oura Ring might trigger the "Accident Model" 10 times in a single minute. Your backend must ensure we don't spam the user (or emergency services) with 10 separate alerts.

The Problem
You need to implement an AlertManager that decides whether an alert should actually be dispatched. For this mock, we will use a base class that simulates a database or a shared cache (like Redis).