class Solution:
    def tribonacci(self, n: int) -> int:

        prev1 = 0
        prev2 = 1
        prev3 = 1
        
        if n == 0:
            return 0
        if n==1 or n==2 :
            return 1 

        for i in range(3,n+1):
            cur = prev1+prev2+prev3
            prev1 = prev2
            prev2 = prev3 
            prev3 = cur 

        return cur 
        