class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        n = len(s)
        if n%2 == 1:
            return False

        for i in s :

            if i == '(' or i =='[' or i =='{':
                stack.append(i)

            elif i == '}' :
                if stack and stack[-1] == '{' :
                    stack.pop()
                else:
                    return False 

            elif i == ']' :

                if stack and stack[-1] == '[' :
                    stack.pop()
                else:
                    return False
            elif i == ')' :
                if stack and stack[-1] == '(' :
                    stack.pop()
                else:
                    return False
            else:
                return False

        return not stack


        