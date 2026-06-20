class Solution:
    def partition(self, s: str) -> List[List[str]]:

        path = []
        res = []

        def is_palin(s):
            return s == s[::-1]

        def bt(idx):

            if idx == len(s):

                res.append(path[:])
                return 

            for i in range(idx , len(s)) :

                cur = s[idx:i+1]

                if is_palin(cur) :

                    path.append(cur)

                    bt(i+1)

                    path.pop()

        bt(0)
        return res
        
        