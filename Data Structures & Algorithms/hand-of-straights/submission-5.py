class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)

        if n%groupSize != 0 :
            return False 

        freq = Counter(hand)
        

        for i in sorted(freq) :

            if freq[i] > 0:

                count = freq[i]

                for nxt in range(i , i + groupSize):
                    if freq[nxt] < count:
                        return False 
                    
                    freq[nxt] -= count 

        return True


        