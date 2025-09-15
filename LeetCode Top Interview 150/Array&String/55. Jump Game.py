from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maxReach=0 #denotes the max element can reach

        for i in range(n):
            if i>maxReach:# the current element cannot be reached
                return False
            maxReach=max(maxReach,i+nums[i])
        return True






if __name__ == '__main__':
    solution=Solution()
    print(solution.canJump([0]))

