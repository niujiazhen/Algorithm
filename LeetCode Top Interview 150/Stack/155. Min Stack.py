class MinStack:

    def __init__(self):
        self.stack=[]#records the standard stack
        self.minStack=[]#records the currently minimum number

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1]>=val:
            self.minStack.append(val)

    def pop(self) -> None:
        popNum=self.stack.pop()
        if self.minStack and self.minStack[-1]==popNum:
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
