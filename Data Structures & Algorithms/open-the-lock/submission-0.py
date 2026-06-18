class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        
        direction = [1,-1]
        visited = set()
        q = deque()
        q.append("0000")
        steps = 0
        deadends = set(deadends)

        if target == '0000':
            return 0
        if '0000' in deadends :
            return -1

        while q :
            for _ in range(len(q)):

                cur_str = q.popleft()
            
                for i in range(4):
                    for di in direction :
                        
                        cur_digit = ( int(cur_str[i]) + di )% 10 
                        new_str = cur_str[:i] + str(cur_digit) + cur_str[i+1:]

                        if new_str == target :
                            return steps + 1

                        if new_str not in deadends and new_str not in visited :
                            visited.add(new_str)
                            q.append(new_str)
            steps+=1

        return -1





        