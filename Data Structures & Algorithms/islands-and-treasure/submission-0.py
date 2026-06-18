from collections import deque

class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            i, j = q.popleft()

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if (
                    ni < 0 or ni >= m or
                    nj < 0 or nj >= n or
                    rooms[ni][nj] != 2147483647
                ):
                    continue

                rooms[ni][nj] = rooms[i][j] + 1
                q.append((ni, nj))