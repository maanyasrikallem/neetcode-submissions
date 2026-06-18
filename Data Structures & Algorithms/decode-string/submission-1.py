class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        string = ''
        num = ''

        for i in s :
            if i == ']' :

                while stack[-1] != '[':
                    string = stack.pop() + string
                
                stack.pop()

                num = ''

                while stack and stack[-1].isdigit() :
                    num = stack.pop() + num
                
                num = int(num)

                

                stack.append(string*num)

                string = ''

            else:
                stack.append(i)

        return "".join(stack)



        