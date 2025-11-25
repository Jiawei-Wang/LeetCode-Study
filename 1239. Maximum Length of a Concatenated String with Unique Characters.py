class Solution:
    def maxLength(self, strings: List[str]) -> int:
        # dp contains all valid concatenated strings
        dp = [set()] # an empty set representing empty string

        for string in strings:
            # check if string has duplicate chars
            # aka: if string itself is valid
            string_set = set(string)
            if len(string_set) < len(string): 
                continue
            
            # go through current options
            for current in dp[:]:
                if string_set & current: 
                    continue
                dp.append(string_set | current)

                # set_a & set_b: return shared elements (intersection)
                # set_a | set_b: return elements in either set (union)

        return max(len(string) for string in dp)