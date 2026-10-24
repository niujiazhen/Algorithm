from typing import List

def canJump(nums: List[int])->bool:
    # Edge Case
    if not nums:
        return False

    # T=O(n) S=O(1)
    maxReach=0# 目前能达到的最远长度
    for i in range(len(nums)):
        if i>maxReach:# 如果当前下标超过了maxReach，则无法到达
            return False
        # 更新maxReach
        maxReach=max(maxReach,i+nums[i])

    return True

if __name__ == '__main__':
    print(canJump([3, 2, 1, 0, 4]))