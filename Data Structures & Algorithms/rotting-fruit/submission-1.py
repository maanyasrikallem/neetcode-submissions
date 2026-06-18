class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        q = deque()
        minute = 0

        directions = [(-1,0) , (1,0) , (0,1) , (0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))

        while q :
            for _ in range(len(q)):

                i , j = q.popleft()
                
                for x , y in directions :
                    ni = i + x
                    nj = j + y

                    if (
                        ni < 0 or ni >=m or nj < 0 or nj >= n or grid[ni][nj] != 1
                    ):

                        continue 
                    
                    grid[ni][nj] = 2
                    q.append((ni,nj))
            minute += 1 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return 0 if minute ==0 else minute - 1
                

                



        