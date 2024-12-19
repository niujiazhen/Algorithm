class MyQueue:

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def push(self, x: int) -> None:
         self.stack_in.append(x)

    def pop(self) -> int:
        if(self.stack_out):#如果stack_out存在元素，则直接pop
            return self.stack_out.pop()
        else:
            while (self.stack_in):#否则，先把stack_in的元素全部加stack_out里，再pop一个
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:#和pop同理，只不过需要将最后pop的元素添加回队首
        if (self.stack_out):
            ans=self.stack_out.pop()
            self.stack_out.append(ans)
            return ans
        else:
            while (self.stack_in):
                self.stack_out.append(self.stack_in.pop())
            ans = self.stack_out.pop()
            self.stack_out.append(ans)
            return ans


    def empty(self) -> bool:
        if(not self.stack_in and not self.stack_out):
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    myQueue=MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.empty())
