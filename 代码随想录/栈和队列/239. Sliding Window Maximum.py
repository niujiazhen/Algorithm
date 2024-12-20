from collections import deque
from time import sleep
from typing import List

class MonotonicQueue:#单调队列（队首最大，队尾最小）只维护区间可能的最大值
    def __init__(self):
        self.queue=deque()

    #模拟pop操作
    def pop(self,value):
        if(self.queue and self.queue[0]==value):#如果当前需要pop的元素在单调队列里，即当前最大元素，则将队首（最大元素）pop
            self.queue.popleft()

    #模拟push操作
    def push(self,value):
        while(self.queue and self.queue[-1]<value):#如果当前需要push的元素大于队尾元素，则将
            self.queue.



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #O(n*k)算法超时
        # ans=[]
        # for i in range(len(nums)-k+1):
        #     ans.append(max(nums[i:i+k]))
        # return ans

        #O(n)算法：单调队列（队首最大，队尾最小）
        ans=[]



if __name__ == '__main__':
    solution=Solution()
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))