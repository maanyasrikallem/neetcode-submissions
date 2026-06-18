class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        res = []

        for i in tokens :

            if i == '+' :
                num = stack.pop() + stack.pop()
                stack.append(num)

            elif i == '-' :
                num = - (stack.pop() - stack.pop())
                stack.append(num)

            elif i == '*' :
                num = (stack.pop() * stack.pop())
                stack.append(num)

            elif i == '/' :
                num = int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(num)
            
            else:
                stack.append(int(i))

        return stack[-1]



        