# 从words中找到所有string对，这对string组成的新string是palindrome，[words[i], words[j]]的意思是将i放在前面，j放在后面组成的string是palindrome
# 限制条件：words中至少有一个string，每个string的长度不为负但可以为0

# 思考：
# 1. 两个string组合有两种方式：A + B 或者 B + A
# 两个string能组合成palindrome有两种方式：一方是另一方翻过来，或者一方是另一方翻过来+自己尾部substring是一个palindrome
# 2. 其实简单的对比方式是直接 A + B 或者 B + A，然后查看string是否从中间可以剖开
# 这样时间复杂度为 n^2 * k，k为字符长度
# 所以为了降低时间复杂度，应该从减少对比次数上入手

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word):
            return word == word[::-1]
        
        output = []
        word_to_index = {word: i for i, word in enumerate(words)}
        for i, word1 in enumerate(words):
            for j in range(len(word1)+1):
                # Case 1 - Find all words, B, shorter than or the same size as
                # word1, that can be prepended so B + word1 is a palindrome.
                x_reversed = word1[j:][::-1]
                rest = word1[0:j]
                if isPalindrome(rest) and x_reversed in word_to_index and word_to_index[x_reversed] != i:
                    output.append([word_to_index[x_reversed], i])
                # Case 2 - Find all words, B, shorter than word1 that can be appended
                # so word1 + B is a palindrome.
                if j == len(word1): continue
                x_reversed = word1[:j][::-1] 
                rest = word1[j:]
                if isPalindrome(rest) and x_reversed in word_to_index and word_to_index[x_reversed] != i:
                    output.append([i, word_to_index[x_reversed]])
        return output




# Trie
def isPalindrome(word):
    return word == word[::-1]

class Trie:
    def __init__(self):
        # letter -> next trie node.
        self.paths = defaultdict(Trie)
        # If a word ends at this node, then this will be a positive value
        # that indicates the location of the word in the input list.
        self.wordEndIndex = -1
        # Stores all words that are palindromes from this node to end of word.
        # e.g. if we are on a path 'a','c' and word "babca" exists in this trie
        # (words are added in reverse), then "acbab"'s index will be in this
        # list since "bab" is a palindrome.
        self.palindromesBelow = []

    # Adds a word to the trie - the word will be added in 
    # reverse (e.g. adding abcd adds the path d,c,b,a,$index) to the trie.
    # word - string the word to be added
    # index - int index of the word in the list, used as word identifier.
    def addWord(self, word, index):
        trie = self
        for j, char in enumerate(reversed(word)): 
            if isPalindrome(word[0:len(word)-j]):
                trie.palindromesBelow.append(index)
            trie = trie.paths[char]
        trie.wordEndIndex = index

    def makeTrie(self, words):
        trie = Trie()
        for i, word in enumerate(words):
            trie.addWord(word, i)
        return trie
    


class Solution:
    # Takes the trie, a word, and its index in the word array 
    # and returns the index of every word that could be appended
    # to it to form a palindrome.
    def getPalindromesForWord(self, trie, word, index):
        # Walk trie. Every time we find a word ending,
        # we need to check if we could make a palindrome.
        # Once we get to the end of the word, we must check
        # all endings below for palindromes (they are already
        # stored in 'palindromesBelow').
        output = []
        while word:
            if trie.wordEndIndex >= 0:
                if isPalindrome(word):
                    output.append(trie.wordEndIndex)
            if not word[0] in trie.paths:
                return output
            trie = trie.paths[word[0]]
            word = word[1:]

        if trie.wordEndIndex >= 0:
            output.append(trie.wordEndIndex)
        output.extend(trie.palindromesBelow)
        return output

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        T = Trie()
        trie = T.makeTrie(words)
        output = []
        for i, word in enumerate(words):
            candidates = self.getPalindromesForWord(trie, word, i)
            output.extend([[i, c] for c in candidates if i != c])
        return output