class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        left = 0
        freq = Counter(t)
        needed = len(t)
        matched = 0
        length = float('inf')
        final_r = 0
        final_l = 0
        

        for right in range(len(s)):
            if s[right] in freq :
                
                freq[s[right]]-=1
                if freq[s[right]] >= 0:
                    matched += 1 
                
            while matched == needed :
                if right-left+1 < length :
                    length = right - left + 1
                    start = left 
                            
                if s[left] in freq :
                    freq[s[left]] += 1
                    if freq[s[left]] > 0:
                        matched-=1 
                left+=1 

        if length == float('inf'):
            return ""
        return s[start:start + length]


                
        