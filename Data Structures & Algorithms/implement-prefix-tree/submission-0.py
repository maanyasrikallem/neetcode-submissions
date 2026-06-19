class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        node = self.root 

        for ch in word :
            if ch not in node.children :
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True 


    def search(self, word: str) -> bool:

        node = self.find(word)

        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:

        node = self.find(prefix)

        return node is not None

    def find(self,word):

        node = self.root

        for ch in word:

            if ch not in node.children :
                return None

            node = node.children[ch] 
        return node

        
        