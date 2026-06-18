class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]
        inorder = [0]*n

        for a,b in trust :
            graph[a-1].append(b-1)
            inorder[b-1] += 1

        for i in range(n):
            if inorder[i] == n-1 and not graph[i] :
                return i+1 

        return -1
        