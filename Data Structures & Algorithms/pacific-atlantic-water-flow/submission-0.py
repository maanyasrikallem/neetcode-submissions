class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m, n = len(heights), len(heights[0])

        pac = set()
        atl = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j, visited):
            visited.add((i, j))

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if (
                    ni < 0 or ni >= m or
                    nj < 0 or nj >= n or
                    (ni, nj) in visited or
                    heights[ni][nj] < heights[i][j]
                ):
                    continue

                dfs(ni, nj, visited)

        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n - 1, atl)

        for j in range(n):
            dfs(0, j, pac)
            dfs(m - 1, j, atl)

        res = []

        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])

        return res