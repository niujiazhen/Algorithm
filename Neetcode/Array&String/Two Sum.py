from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HashMap
        # T=O(n) S=O(n)
        hash={}

        for i in range(len(nums)):
            if target-nums[i] in hash:
                return [hash[target-nums[i]],i] # hash[target-nums[i]] must be the smaller index because it's in the hashmap before
            hash[nums[i]]=i

if __name__ == '__main__':
    solution=Solution()
    print(solution.twoSum([4,5,6],10))