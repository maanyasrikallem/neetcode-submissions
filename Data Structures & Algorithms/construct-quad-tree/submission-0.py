"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf,
                 topLeft, topRight,
                 bottomLeft, bottomRight):

        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        n = len(grid)

        prefix = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):

                prefix[i + 1][j + 1] = (
                    grid[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        def getSum(r, c, size):

            r2 = r + size
            c2 = c + size

            return (
                prefix[r2][c2]
                - prefix[r][c2]
                - prefix[r2][c]
                + prefix[r][c]
            )

        def dfs(r, c, size):

            s = getSum(r, c, size)

            if s == 0:

                return Node(
                    False,
                    True,
                    None,
                    None,
                    None,
                    None
                )

            if s == size * size:

                return Node(
                    True,
                    True,
                    None,
                    None,
                    None,
                    None
                )

            m = size // 2

            topLeft = dfs(r, c, m)

            topRight = dfs(r, c + m, m)

            bottomLeft = dfs(r + m, c, m)

            bottomRight = dfs(r + m, c + m, m)

            return Node(
                True,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return dfs(0, 0, n)