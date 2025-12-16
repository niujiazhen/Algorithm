from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        #T=O(n) S=O(n)
        #Edge Case
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        DP=[0]*n
        #Initialize
        DP[0]=nums[0]
        DP[1]=max(nums[0],nums[1])#the OPT of first two houses is the bigger one of two houses

        for i in range(2,n):
            DP[i]=max(DP[i-1],DP[i-2]+nums[i])
        return DP[n-1]



if __name__ == '__main__':
    solution=Solution()
    print(solution.rob([2,1]))