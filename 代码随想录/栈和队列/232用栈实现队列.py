class MyQueue:

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def push(self, x: int) -> None:
        self.stack_in.append(x)
    def pop(self) -> int:
        #如果出栈为空，则先把入栈全部放入出栈，再pop一个
        if(not self.stack_out):
            while(self.stack_in):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        #否则直接po一个
        else:
            return self.stack_out.pop()


    def peek(self) -> int:
        pop_element=self.pop()
        self.stack_out.append(pop_element)#把pop出来的元素重新放到stack_out列表的第一个
        return pop_element

    def empty(self) -> bool:
        if(not self.stack_in and not self.stack_out):
            return True
        return False



# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())