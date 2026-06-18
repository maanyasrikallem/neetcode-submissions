class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        if n==1 :
            return 1 
        left = 0
        seen = {}
        length = 0

        for right in range(n):

            if s[right] in seen and seen[s[right]] >= left :
                length = max(length , right-left)
                left = seen[s[right]]+1
                del seen[s[right]]

            
            seen[s[right]] = right 
            length = max(length , right - left+1)

        return length 
                


        