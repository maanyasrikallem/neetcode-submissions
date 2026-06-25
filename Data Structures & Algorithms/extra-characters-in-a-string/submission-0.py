class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        # Build Trie
        root = TrieNode()

        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isEnd = True

        memo = {}

        def dfs(idx):

            if idx == len(s):
                return 0

            if idx in memo:
                return memo[idx]

            # Option 1: Treat current character as extra
            ans = 1 + dfs(idx + 1)

            # Option 2: Match dictionary words starting at idx
            node = root

            for i in range(idx, len(s)):

                if s[i] not in node.children:
                    break

                node = node.children[s[i]]

                if node.isEnd:
                    ans = min(ans, dfs(i + 1))

            memo[idx] = ans
            return ans

        return dfs(0)