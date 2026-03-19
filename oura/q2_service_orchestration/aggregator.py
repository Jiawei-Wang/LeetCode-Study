import asyncio
from clients import call_fall_model, call_faint_model, call_seizure_model

class ConsensusEngine:
    def __init__(self, timeout=0.2):
        self.timeout = timeout

    async def get_consensus(self):
        """
        TODO:
        1. Execute all three model calls (fall, faint, seizure) concurrently.
        2. Wrap the execution in a timeout (self.timeout). 
        3. If a model fails (exception) or times out, ignore its result.
        4. Logic:
           - If ANY model returns a score > 0.9, return "CRITICAL_ALERT".
           - Else if the average of all successful/timely scores is > 0.5, return "WARNING".
           - Otherwise, return "NORMAL".
        5. Return a tuple: (final_status, list_of_contributing_model_names)
        """
        tasks = [
            call_fall_model(),
            call_faint_model(),
            call_seizure_model()
        ]

        results = []
        contributing_models = []

        try:
            completed_tasks = await asyncio.wait_for(asyncio.gather(*tasks, return_exceptions=True), timeout=self.timeout)
            for result in completed_tasks:
                if isinstance(result, Exception):
                    continue  # Ignore failed models
                results.append(result["score"])
                contributing_models.append(result["model"])
        except asyncio.TimeoutError:
            pass  # Ignore timeout

        if any(score > 0.9 for score in results):
            return "CRITICAL_ALERT", contributing_models
        elif results and (sum(results) / len(results)) > 0.5:
            return "WARNING", contributing_models
        else:
            return "NORMAL", contributing_models


# test directly in the file
if __name__ == "__main__":
    example = ConsensusEngine()
    result = asyncio.run(example.get_consensus())
    print(result)