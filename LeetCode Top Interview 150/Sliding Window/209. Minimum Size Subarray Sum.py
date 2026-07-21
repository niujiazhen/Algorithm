from sys import prefix
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #T=O(n), S=O(n)
        # minLen=float("inf")
        # prefixSum=[0]*(len(nums)+1)
        # #calculate the prefix sum
        # for i in range(len(nums)):
        #     prefixSum[i+1]=prefixSum[i]+nums[i]
        # l=0
        # r=1
        # while r<len(prefixSum):
        #     sum=prefixSum[r]-prefixSum[l]
        #     if sum>=target:
        #         minLen=min(minLen,r-l)
        #         l+=1
        #     else:
        #         r+=1
        # if minLen==float("inf"):
        #     return 0
        # return minLen

        #Another way to realize Prefix Sum with S=O(1)
        minLen=float("inf")
        l=0
        r=0
        curSum=0
        for r in range(len(nums)):
            curSum+=nums[r]
            while curSum>=target:
                minLen=min(minLen,r-l+1)
                curSum-=nums[l]
                l+=1
        if minLen==float("inf"):
            return 0
        return minLen


if __name__ == '__main__':
    solution=Solution()
    print(solution.minSubArrayLen(15, [1,2,3,4,5]))
