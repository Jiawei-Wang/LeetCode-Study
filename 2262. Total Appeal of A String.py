class Solution:
    def appealSum(self, s: str) -> int:
        """
        let dp[i] be the sum of appeal of all substrings ending at index i
        for example we have "abb", and when index i = 2:
        we have substrings: "abb", "bb", "b"
        dp[2] = appeal of "abb" + appeal of "bb" + appeal of "b"

        when we move from index i-1 to index i, we add s[i] to all substrings
        if a substring already contains s[i]: no change
        if a sbustring doesn't contain s[i]: appeal += 1

        we use a variable to keep track of last seen index of s[i]: last_pos[s[i]]
        all sustrings starting after last_pos[s[i]] up to i: appeal += 1

        so in total:
        dp[i] = dp[i-1] + (i - last_pos[s[i]])
        """

        last_pos = {}
        total_appeal = 0
        current_dp = 0
        
        for i, char in enumerate(s):
            current_dp += (i - last_pos.get(char, -1)) # if a char has never been seen, index is treated as -1
            total_appeal += current_dp
            last_pos[char] = i
            
        return total_appeal