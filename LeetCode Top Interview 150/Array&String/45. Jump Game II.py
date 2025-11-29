from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        #T=O(n),S=O(1)
        step=0 #records the minimum jump
        curEnd=0#denotes the furthest index can be reached by current jump
        curFur=0#denotes the furthest index can be reached at current index(next jump)

        for i in range(len(nums)-1):
            curFur=max(curFur,i+nums[i])
            if i==curEnd:#the last index i that we have to jump to reach curEnd,ensuring minimum steps
                curEnd=curFur
                step+=1
        return step




if __name__ == '__main__':
    solution=Solution()
    print(solution.jump([1,2,1,1,1]))
