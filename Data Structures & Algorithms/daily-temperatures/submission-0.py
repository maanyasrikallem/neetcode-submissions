class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)

        res = [0]*n
        stack = [(temperatures[n-1] , n-1)]

        
        
        for i in range(n-2 , -1 , -1) :

            while stack and temperatures[i] >= stack[-1][0] :
                stack.pop()

            if not stack :
                res[i] = 0
                stack.append((temperatures[i] , i))
            
            else:
                _ , idx = stack[-1]

                res[i] = idx - i 

                stack.append((temperatures[i] , i))

        return res


        