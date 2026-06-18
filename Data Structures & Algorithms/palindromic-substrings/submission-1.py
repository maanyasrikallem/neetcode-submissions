class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        final_count = 0

        def expand(left , right):
            count = 0

            while left >=0 and right <= n-1 and s[left] == s[right] :
                left-=1
                right+=1
                count += 1 

            return count 

        for i in range(n):

            final_count += expand(i,i) + expand(i,i+1)

        return final_count 
        