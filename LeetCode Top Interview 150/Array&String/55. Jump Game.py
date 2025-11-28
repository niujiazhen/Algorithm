from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach=0#denotes the max index can reach currently
        for i in range(len(nums)):
            if i>maxReach:#means we cannot reach the current index from any index before i
                return False
            maxReach=max(i+nums[i],maxReach)
        return True






if __name__ == '__main__':
    solution=Solution()
    print(solution.canJump([0]))

