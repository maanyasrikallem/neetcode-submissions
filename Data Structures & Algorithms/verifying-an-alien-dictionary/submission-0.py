class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordering = {ch : i for i,ch in enumerate(order)}

        for i in range(len(words)-1):
            w1 , w2 = words[i] , words[i+1]

            for j in range(min(len(w1),len(w2))):
                if w1.startswith(w2):
                    return False 
                if w1[j] != w2[j]:
                    if ordering[w1[j]] > ordering[w2[j]]:
                        return False 
                    else:
                        break

        return True 


        
        