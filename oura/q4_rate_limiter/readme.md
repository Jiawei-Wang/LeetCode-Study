The Sliding Window Rate Limiter.

In a backend system for a wearable like Oura, we have to handle millions of devices syncing data. A "Rate Limiter" ensures that a buggy firmware or a malicious actor doesn't overwhelm our ingestion service.