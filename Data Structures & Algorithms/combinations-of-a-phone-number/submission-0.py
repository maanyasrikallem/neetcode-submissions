class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        path = []
        
        if not digits :
            return []
        children = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def bt(idx) :

            if idx == len(digits) :
                res.append(''.join(path))
                return 


            digit = digits[idx]

            for child in children[str(digit)] :

                path.append(child)

                bt(idx+1)

                path.pop()

        bt(0)
        return res
        