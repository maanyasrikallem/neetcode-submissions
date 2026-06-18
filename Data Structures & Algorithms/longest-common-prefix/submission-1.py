class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = float('inf')

        for word in strs:
            min_len = min(min_len , len(word))

        i = 0

        while i < min_len :
            check = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != check :
                    return strs[j][:i]
            i+=1 

        if i != 0:
            return strs[0][:i]
        else:
            return ""
                
        