import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # T=O(nlogn) S=O(1)
        # nums.sort()
        # n=len(nums)
        # return nums[n//2] # because the majority element always exists, so nums n over 2 must be the majority element

        # HashMap T=O(n), S=O(n)
        counts=collections.Counter(nums) #counts the frequency of each element in nums
        return max(counts.keys(),key=counts.get)






if __name__ == '__main__':
    solution=Solution()
    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
