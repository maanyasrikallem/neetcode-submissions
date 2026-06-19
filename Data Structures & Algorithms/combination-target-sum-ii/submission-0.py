class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []

        candidates.sort()

        def bt(idx):

            if sum(path) > target :
                return 

            if sum(path) == target :
                res.append(path[:])
                return 

            for i in range(idx , len(candidates)) :

                if i > idx and candidates[i] == candidates[i-1] :
                    continue

                path.append(candidates[i])

                bt(i+1)

                path.pop()

        bt(0)
        return res

        