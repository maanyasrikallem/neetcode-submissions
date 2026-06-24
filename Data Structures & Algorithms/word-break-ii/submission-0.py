class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []

        path = []

        def bt(i) :

            if i == len(s) :
                res.append(" ".join(path))
                return 

            for j in range(i+1,len(s)+1) :

                if s[i:j] in wordDict :

                    word = s[i:j]

                    path.append(word)

                    bt(j)

                    path.pop()
        
        bt(0)

        return res