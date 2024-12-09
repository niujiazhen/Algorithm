from collections import deque
from typing import List


class myQueue:#单调队列，只维护区间可能的最大值
    def __init__(self):
        self.que=deque()

    #模拟pop操作
    def pop(self,value):
        if(self.que and self.que[0]==value):
            self.que.popleft()

    #模拟push操作
    def push(self,value):
        while(self.que and self.que[-1]<value):
            self.que.pop()
        self.que.append(value)

    #模拟获取最大值操作（返回队列头元素）
    def getMaxValue(self):
        return self.que[0]

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    ans=[]
    que=myQueue()
    for i in range(k):
        que.push(nums[i])
    ans.append(que.getMaxValue())
    for i in range(k,len(nums)):
        que.pop(nums[i-k])
        que.push(nums[i])
        ans.append(que.getMaxValue())

    return ans





if __name__ == '__main__':
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))