class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1]>=val:
            self.minStack.append(val)

    def pop(self) -> None:
        t=self.stack.pop()
        if self.minStack[-1]==t:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    minstack=MinStack()
    minstack.push(-2)
    minstack.push(0)
    minstack.push(-3)
    minstack.getMin()
    minstack.pop()
    minstack.top()
    minstack.getMin()
