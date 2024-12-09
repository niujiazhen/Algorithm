#用时14：49
class MyQueue:

    def __init__(self):
        self.stack_in=[]#入栈
        self.stack_out=[]#出栈

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if(self.stack_out):
            return self.stack_out.pop()
        else:
            while(self.stack_in):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self) -> int:
        result=self.pop()
        self.stack_out.append(result)
        return result
    def empty(self) -> bool:
        if(self.stack_in or self.stack_out):
            return False
        return True



# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj.pop())
    print(obj.push(5))
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())