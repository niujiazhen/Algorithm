from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # T=O(n) S=O(1)
        step=0
        curEnd=curFar=0

        for i in range(len(nums)-1):
            curFar=max(curFar,i+nums[i])# curFar denotes the furthest index can be reached
            if i==curEnd:
                step+=1
                curEnd=curFar# curEnd denotes the next End Point to be reached at 1 jump
        return step




if __name__ == '__main__':
    solution=Solution()
    print(solution.jump([1,2,1,1,1]))
