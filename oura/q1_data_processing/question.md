Mock 1: The "Signal Buffer & Validator" Scenario: 

The Oura Ring sends accelerometer data in small batches. Before the ML model can predict an "accident," the data must be cleaned and "windowed" (the model needs exactly 50 continuous samples).

Files provided: 
* src/processor.py (You edit this)
* src/models.py (Pydantic schemas provided)
* tests/test_processor.py (A suite of unit tests)


Your Task: 
1.  Validation: Use the provided Pydantic model to validate incoming JSON packets. If a packet is missing timestamp or accel_z, log an error and skip it.
2.  State Management: Implement a SlidingWindow class that stores the last 50 valid packets.
3.  Missing Data: If the gap between two timestamps is $> 100\text{ms}$, the "window" is considered broken. Clear the buffer and start over.

It tests your ability to handle Python types, class state, and real-world sensor logic rather than an abstract algorithm.