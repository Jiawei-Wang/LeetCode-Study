# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
逻辑：implement一个树
树拥有多个node，每个node也拥有多个节点
将一个node标记为末尾来表示从树根到它的一条路径为一个单词
"""

# create a node class first
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode) # a dict where default value (TrieNode) is given to key if there is none 
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode() # root本身是一个dummy node

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter] 
        current.is_word = True # 最后一个字母标记为结尾

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter) # dict.get()，返回value或者None
            if current is None:
                return False
        return current.is_word # 必须每一步（包括最后一个char）都返回True

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True # 和search的对比在于：同样都使用input string在树里往下走，走不到最后就返回False，但不同之处在于如果走到最后，不需要查看此char的is_word属性


"""
understand
    for letter in word:
        current = current.children[letter]
1. current.children is a ictionary: key = letter, value = TrieNode object
2. current.children[letter] accesses the value for the letter key in children dictionary
3. if key exists, TrieNode object is returned, if not, TrieNode object is created for the key
for example: insert "abc"
1. current points to dummy head
2. dummy.children[a] = a new TrieNode (a is the key in dict, TrieNode is the value)
3. current points to this new TrieNode (accessed by giving a as key)
4. do the same thing for b in a.children, and c in b.children
"""