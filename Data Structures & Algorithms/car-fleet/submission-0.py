class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_pos = sorted(zip(position , speed) , key = lambda x : x[0])

        n = len(sorted_pos)
        sets = 0
        stack = []

        for i in range(n-1 , -1 , -1) :

            time = (target-sorted_pos[i][0])/sorted_pos[i][1]

            if stack and time  <= stack[-1]:
                continue 
            else:
                stack.append(time)
                sets += 1
                 

        return sets

