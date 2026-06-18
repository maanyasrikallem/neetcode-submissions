class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = min(len(s) for s in strs)

        for i in range(min_len):

            cur_char = strs[0][i]

            for j in range(1,len(strs)):

                if strs[j][i] != cur_char :
                    return strs[0][:i]

        return strs[0][:min_len]

                
        