class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        path = [['.']*n for _ in range(n)]
        res = []

        visited_r = set()
        visited_c = set()
        diag1 = set()
        diag2 = set()


        def bt(row) :

            if row >= n :
                res.append([''.join(r) for r in path])
                return 

            for col in range(n) :

                if row in visited_r or col in visited_c or row-col in diag1 or row+col in diag2 :
                    continue 
                
                path[row][col] = 'Q'
                visited_r.add(row)
                visited_c.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                bt(row+1)

                path[row][col] = '.'
                visited_r.remove(row)
                visited_c.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

        bt(0)
        return res


        