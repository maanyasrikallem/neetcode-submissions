class MinStack:

    def __init__(self):
        self.stack = []
        self.minim = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minim:
            self.minim.append(val)
        
        elif val <= self.minim[-1] :
            self.minim.append(val)
        
    def pop(self) -> None:
        x = self.stack.pop()

        if x == self.minim[-1]:
            self.minim.pop()
  

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minim[-1]

        
