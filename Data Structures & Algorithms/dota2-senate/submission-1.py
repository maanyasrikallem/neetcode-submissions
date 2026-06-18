class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        freq = Counter(senate)
        n = len(senate)

        if freq['R'] == 0:
            return 'Dire'

        if freq['D'] == 0:
            return 'Radiant'

        i = 0
        count_r = count_d = 0

        q = deque()

        for i in range(n):
            q.append(senate[i])

        while freq['R'] and freq['D']:
            cur = q.popleft()

            if cur == 'R':
                if count_r > 0:
                    count_r -= 1
                    freq['R'] -= 1
                else:
                    count_d += 1
                    q.append(cur)

            else :

                if count_d > 0:
                    count_d -= 1
                    freq['D'] -= 1
                else:
                    count_r += 1
                    q.append(cur)

        return 'Radiant' if freq['R'] else 'Dire'
  
        