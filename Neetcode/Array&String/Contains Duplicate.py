from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T=O(n) S=O(n)
        # We use set
        hash=set()
        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            hash.add(nums[i])

        return False


if __name__ == '__main__':
    solution=Solution()
    print(solution.hasDuplicate([1,2,3,3]))