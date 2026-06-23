class Solution:
    def calcEquation(self, equations, values, queries):

        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):

            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(c, d, visited):

            if c == d:
                return 1

            visited.add(c)

            for x, value in graph[c]:

                if x in visited:
                    continue

                ans = dfs(x, d, visited)

                if ans != -1:
                    return value * ans

            return -1

        res = []

        for c, d in queries:

            if c not in graph or d not in graph:
                res.append(-1.0)

            else:
                res.append(dfs(c, d, set()))

        return res