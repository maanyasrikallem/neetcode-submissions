class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        n = len(s)

        dp = [False] * (n)

        if s[n-1] == '1' or s[0] == '1':
            return False 
        
        dp[0] = True 


        for i in range(n):
            if dp[i]:

                for j in range(i+minJump , min(i+maxJump+1 , n)):
                    if s[j] == '0' :
                        dp[j] = True 

        return dp[n-1]


                
        