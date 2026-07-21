from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Edge Case
        if not nums:
            return 0

        #We define OPT[i] as the maximum increasing subsequence that ends at index i
        OPT=[1]*len(nums)
        #Build the dp array from left to right
        for i in range(1,len(nums)):
            #Check all nums before nums[i]
            for j in range(i):
                if nums[j]<nums[i]:#if nums[i] can be appended to the subsequence ending at index j
                    OPT[i]=max(OPT[i],OPT[j]+1)#Update OPT[i] with best possible value

        return max(OPT)

if __name__ == '__main__':
    solution=Solution()
    print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))