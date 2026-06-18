class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)

        if n%groupSize != 0 :
            return False 

        freq = Counter(hand)
        

        for i in sorted(freq) :
            while freq[i] > 0:
                
                freq[i] -= 1
                cur = i
                for _ in range(groupSize-1):
                    if cur+1 not in freq or freq[cur+1] == 0:
                        return False 
                    
                    freq[cur+1] -= 1
                    cur+=1

        return True


        