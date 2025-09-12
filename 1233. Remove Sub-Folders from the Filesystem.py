# solution 1: trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder):
        # Build Trie
        root = TrieNode()
        for path in folder:
            current = root
            parts = path.split("/")[1:]
            skip = False
            for p in parts:
                if current.is_end:  # already a folder, so skip inserting subfolder
                    skip = True
                    break
                if p not in current.children:
                    current.children[p] = TrieNode()
                current = current.children[p]
            if not skip:
                current.is_end = True
        
        # DFS to collect valid folders
        res = []
        def dfs(node, path):
            if node.is_end:
                res.append("/" + "/".join(path))
                return  # don't go deeper, since deeper are subfolders
            for p, child in node.children.items():
                dfs(child, path + [p])
        
        dfs(root, [])
        return res


# solution 2: sorting 
class Solution:
    def removeSubfolders(self, folder):
        folder.sort()
        res = []
        prev = ""
        for f in folder:
            # check if current folder starts with prev + "/"
            if not prev or not f.startswith(prev + "/"):
                res.append(f)
                prev = f
        return res
