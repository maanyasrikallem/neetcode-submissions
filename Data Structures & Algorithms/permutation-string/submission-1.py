class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        set_s1 = Counter(s1)

        for right in range(k-1,len(s2)):

            if Counter(s2[right-k+1:right+1]) == set_s1:
                return True 
            
        return False 

            
        