import asyncio
import random

async def call_fall_model():
    await asyncio.sleep(0.05) # Fast
    return {"model": "fall", "score": 0.92, "status": "success"}

async def call_faint_model():
    await asyncio.sleep(0.15) # Slower
    return {"model": "faint", "score": 0.4, "status": "success"}

async def call_seizure_model():
    # This model is currently unstable
    await asyncio.sleep(0.1)
    if random.random() < 0.5:
        raise Exception("Model Timeout/Internal Error")
    return {"model": "seizure", "score": 0.1, "status": "success"}