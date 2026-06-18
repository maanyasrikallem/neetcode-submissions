class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first = 0
        second = 0
        ans = []
        while first < len(word1) or second < len(word2):
            if first < len(word1):
                ans.append(word1[first])            
                first+=1
            if second < len(word2):
                ans.append(word2[second])
                second+=1 

        return "".join(ans)
            
        