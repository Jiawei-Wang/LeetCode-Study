"""
design and implement a small module or package that can take in 
a list of strings and a set of rules to process those strings.

The module should support both predefined rules (built into the package) 
and user-defined rules (custom logic provided by the user). 
The design should use proper abstraction and interfaces so that user-defined rules can be easily plugged in, 
extended, or replaced without changing the core processing logic.

Essentially, the goal is to create a flexible and extensible string processing framework 
where rules can be composed and applied in sequence to transform the input strings.
"""

from abc import ABC, abstractmethod
from typing import List, Callable

# Step 1: Define interface for a Rule
class Rule(ABC):
    @abstractmethod
    def apply(self, s: str) -> str:
        pass

# Step 2: Predefined rules
class ToUpperCaseRule(Rule):
    def apply(self, s: str) -> str:
        return s.upper()

class StripWhitespaceRule(Rule):
    def apply(self, s: str) -> str:
        return s.strip()

# Step 3: Allow user-defined rules via function wrapper
class FunctionRule(Rule):
    def __init__(self, func: Callable[[str], str]):
        self.func = func

    def apply(self, s: str) -> str:
        return self.func(s)

# Step 4: Processor
class StringProcessor:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def process(self, strings: List[str]) -> List[str]:
        result = []
        for s in strings:
            for rule in self.rules:
                s = rule.apply(s)
            result.append(s)
        return result

# Example usage
if __name__ == "__main__":
    strings = ["  hello ", "world123 "]
    rules = [
        StripWhitespaceRule(),
        ToUpperCaseRule(),
        FunctionRule(lambda s: ''.join([c for c in s if not c.isdigit()]))  # remove digits
    ]
    processor = StringProcessor(rules)
    print(processor.process(strings))  # ['HELLO', 'WORLD']
