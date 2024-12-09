class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if(self.stack):
            lastMin=self.stack[-1][1]
            curMin=min(lastMin,val)
            self.stack.append((val,curMin))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
    # -2,0,-3
    #-2,0