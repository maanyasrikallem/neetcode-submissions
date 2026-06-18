class Solution:
    def simplifyPath(self, path: str) -> str:

        cur = ''
        stack = []

        for i in path :

            if i == '/' :
                if not cur:
                    continue 

                if cur == '.' :
                    cur = ''
                    continue 
                elif cur == '..' :
                    if stack:

                        stack.pop()
                else:
                    stack.append(cur)

                cur = ''

            else:
                cur += i

        if cur :
            if cur == '..':
                if stack :
                    stack.pop()

            elif cur != '.':

                stack.append(cur)


        return '/' +'/'.join(stack)

            





    