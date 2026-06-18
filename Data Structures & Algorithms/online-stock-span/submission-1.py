class StockSpanner:

    def __init__(self):

        self.stack = []

    def next(self, price: int) -> int:

        if self.stack :
            if self.stack[-1] > price :
                self.stack.append(price)
                return 1 
            else :
                i = len(self.stack) - 1
                while i >= 0 and self.stack[i] <= price :
                    i -= 1
                self.stack.append(price)
                return len(self.stack) - i - 1

        else:
            self.stack.append(price)
            return 1 

            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)