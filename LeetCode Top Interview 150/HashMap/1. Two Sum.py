from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #T=O(n), S=O(n)
        hash={}
        for i in range(len(nums)):
            if target-nums[i] in hash:
                return [i,hash[target-nums[i]]]
            hash[nums[i]] = i


if __name__ == '__main__':
    solution=Solution()
    print(solution.twoSum([2,7,11,15],9))