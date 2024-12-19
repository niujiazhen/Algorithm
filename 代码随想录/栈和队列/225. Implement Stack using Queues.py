from collections import deque


class MyStack:

    def __init__(self):
        self.queue=deque()
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:#只用popleft实现，类似于队列的出队，不用pop
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())#先将队列除了最后一个的元素分别添加到队尾
        return self.queue.popleft()#返回队首元素，即原队列尾部元素，栈顶

    def top(self) -> int:
        ans=self.pop()
        self.queue.append(ans)
        return ans


    def empty(self) -> bool:
        return not self.queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == '__main__':
    myStack=MyStack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    print(myStack.top())
    print(myStack.pop())
    print(myStack.empty())