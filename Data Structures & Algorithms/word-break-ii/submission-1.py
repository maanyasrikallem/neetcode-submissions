class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordSet = set(wordDict)
        memo = {}

        def dfs(i):

            if i in memo:
                return memo[i]

            if i == len(s):
                return [""]

            ans = []

            for j in range(i + 1, len(s) + 1):

                word = s[i:j]

                if word in wordSet:

                    for suffix in dfs(j):

                        if suffix:
                            ans.append(word + " " + suffix)
                        else:
                            ans.append(word)

            memo[i] = ans

            return ans

        return dfs(0)