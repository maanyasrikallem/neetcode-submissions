class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []
        path = []

        def bt(idx) :

            if idx == len(s) :
                res.append(' '.join(path))
                return 

            for i in range(idx , len(s)) :

                word = s[idx : i+1] 

                if word in wordDict :

                    path.append(word) 

                    bt(i+1)

                    path.pop()

        bt(0)

        return res 


            