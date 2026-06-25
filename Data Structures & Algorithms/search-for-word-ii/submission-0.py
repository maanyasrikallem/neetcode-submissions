class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Build Trie
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        m, n = len(board), len(board[0])
        res = []

        def dfs(r, c, node):

            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                board[r][c] == "#"
            ):
                return

            ch = board[r][c]

            if ch not in node.children:
                return

            node = node.children[ch]

            if node.word:
                res.append(node.word)
                node.word = None  # Avoid duplicates

            temp = board[r][c]
            board[r][c] = "#"

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = temp

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res