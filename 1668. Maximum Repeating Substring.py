# class Solution:
#     def maxRepeating(self, sequence: str, word: str) -> int:
#         s = len(sequence)
#         w = len(word)

#         counter = 0
#         global_longest = 0
        
#         index = 0
#         while index <= s - w:
#             if sequence[index:index+w] == word:
#                 counter += 1
#                 global_longest = max(counter, global_longest)
#                 index += w
#             else:
#                 counter = 0
#                 index += 1
#         return global_longest

"""
above answer fails 1 test case out of 212:
sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
Output 4
Expected 5
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        # Keep checking if 'word' repeated (k + 1) times is in the sequence
        while (word * (k + 1)) in sequence:
            k += 1
            
        return k