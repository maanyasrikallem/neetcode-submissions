from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        
        # sort in reverse so we can pop smallest efficiently
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        res = []
        
        def dfs(node):
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            res.append(node)
        
        dfs("JFK")
        return res[::-1]