class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        path = []

        open_cnt = close_cnt = 0

        def bt(open_cnt,close_cnt) :

            if len(path) == 2*n :

                res.append(''.join(path))

                return 

            if open_cnt < n :

                path.append ('(')

                bt(open_cnt+1 , close_cnt)

                path.pop()

            if  close_cnt < open_cnt :

                path.append(')')

                bt(open_cnt , close_cnt + 1)

                path.pop()

        bt(0,0)
        return res
        