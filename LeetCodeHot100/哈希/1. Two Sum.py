from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # No Edge Case

        # Basic Solution
        # T=O(n) S=O(n)
        hash={}# value->index
        for i in range(len(nums)):
            if target-nums[i] in hash:
                return [hash[target-nums[i]],i]
            hash[nums[i]]=i


if __name__ == '__main__':
    solution=Solution()
    print(solution.twoSum([2,7,11,15],9))