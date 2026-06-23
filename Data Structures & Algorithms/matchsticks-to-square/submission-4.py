class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total = sum(matchsticks)

        if total%4 != 0 :
            return False

        target = total // 4 

        sides = [0]*4

        matchsticks.sort(reverse = True)

        def bt(idx):

            if idx == len(matchsticks):
                return all(side == target for side in sides)

            for i in range(4):

                if sides[i] + matchsticks[idx] <= target :
                    sides[i] += matchsticks[idx]

                    if bt(idx+1) :
                        return True 
                    
                    sides[i] -= matchsticks[idx]

                if sides[i] == 0:
                    break
                
            return False 
        
        return bt(0)
                