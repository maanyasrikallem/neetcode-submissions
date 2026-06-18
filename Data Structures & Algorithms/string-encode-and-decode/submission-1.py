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
        decoded = []
        index = 0
        while index < len(s):
            i = index
            while s[i] != '#':
                i+=1 
            length = int(s[index :i])

            decoded.append(s[i+1:i+1+length])
            index = i+1+length

        

        return decoded 
        


            


