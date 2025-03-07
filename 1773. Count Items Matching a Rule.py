class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        hashmap = {"type": 0, "color": 1, "name": 2}
        search = hashmap[ruleKey]
        count = 0
        for item in items:
            if item[search] == ruleValue:
                count += 1
        return count


        