# every single letter is a TrieNode in the Trie 
class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()
        self.rank = -1

# this class provides insert and startsWith on a Trie DS
class Autocomplete:
    def __init__(self):
        self.root = TrieNode('dummy')

    # insert a word into Trie with its rank on last letter
    def insert(self, word, rank):
        current = self.root
        for letter in word:
            if letter not in current.children:
                node = TrieNode(letter)
                current.children[letter] = node
                current = node
            else:
                current = current.children[letter]
        current.rank = rank

    # search for the words in Trie with prefix and return up to 5 with the highest rank
    def search(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return 'no match found for this prefix'
            current = current.children[letter]

        # dfs from the last char of prefix        
        finding = []
        startNode = current
        startWord = prefix

        def dfs(node, word): # root: current node in Trie, word: word we have built so far
            if node.rank != -1:
                finding.append([word, node.rank])
            for next in node.children:
                dfs(node.children[next], word+node.children[next].letter)
 
        dfs(startNode, startWord)
    
        # up to 5 findings sorted by rank
        finding.sort(key = lambda x:x[1])
        return finding[0:5]


                




