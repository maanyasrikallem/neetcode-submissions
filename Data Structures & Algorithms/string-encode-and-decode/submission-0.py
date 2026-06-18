class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for string in strs :
            length = len(string)
            ans.append(str(length))
            ans.append('#')
            ans.append(string)
        return "".join(ans)


    def decode(self, s: str) -> List[str]:
        self.decoded = []
        def dec(index):
            if index >= len(s):
                return 
            i = index
            while s[i] != '#':
                i+=1 
            length = int(s[index :i])

            self.decoded.append(s[i+1:i+1+length])
            dec(i+1+length)

        dec(0)

        return self.decoded 
        


            


