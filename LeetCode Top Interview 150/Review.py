from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #T=O(n2) S=O(n)
        # We define DP[i] as the longest strictly increasing subsequence in nums[0:i+1]
        DP=[1]*len(nums)

        for i in range(1,len(nums)):
            for j in range(i):
                #Check all pre numbers
                if nums[i]>nums[j]:
                    DP[i]=max(DP[i],DP[j]+1)
        return max(DP)


if __name__ == '__main__':
    solution=Solution()
    print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))