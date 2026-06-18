class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last = {}

        for i,x in enumerate(s) :
            last[x] = i

        i = 0
        res = []
        last_index = 0

        while i < len(s):

            cur = s[i] 

            last_ind = last[cur]

            j = i+1

            while j < last_ind:
                
                last_ind = max(last_ind , last[s[j]])
                j+=1

            res.append(last_ind - i + 1)
            i = last_ind + 1

        return res            

        