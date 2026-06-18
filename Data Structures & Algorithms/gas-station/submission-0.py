class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        i = start = 0
        tot_gas = 0
        n = len(gas)
        count = 0

        if sum(gas) < sum(cost) :
            return -1

        while True :

            tot_gas += gas[i]

            if tot_gas >= cost[i] :
                tot_gas -= cost[i]
                count += 1 
                i = (i+1)%n
            else :
                tot_gas = 0
                count = 0
                start = i + 1 
                i = (i+1) % n

            if count == n :
                return i 




        