class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        found = [0]*3

        for i in range(len(triplets)) :

            a1 = triplets[i][0]
            b1 = triplets[i][1]
            c1 = triplets[i][2]

            if a1 > target[0] or b1 > target[1] or c1 > target[2] :
                continue 

            if a1 == target[0] :
                found[0] = 1
            if b1 == target[1] :
                found[1] = 1
            if c1 == target[2] :
                found[2] = 1 

        for j in range(3):
            if found[j] == 0:
                return False 

        return True 



            

        