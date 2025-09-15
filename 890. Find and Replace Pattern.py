class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # frequency and position both need to match
        # for example pattern = abb
        # then in ["abc","deq","mee","aqq","dkd","ccc"]
        # mee and aqq are good, dkd is not
        def encode(word):
            mapping = {}
            result = []
            index = 0
            for char in word:
                if char not in mapping:
                    mapping[char] = index
                    index += 1
                result.append(mapping[char])
            return result

        pattern_code = encode(pattern)
        return [w for w in words if encode(w) == pattern_code]

