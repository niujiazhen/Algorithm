from collections import deque


class MyStack:

    def __init__(self):
        self.que=deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        result=self.que.pop()
        self.que.append(result)
        return result

    def empty(self) -> bool:
        if(not self.que):
            return True
        return False


# Your MyStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    print(obj.empty())