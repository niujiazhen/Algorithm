from typing import List

def maxSubArray(nums:List[int])->int:
    # T=O(n) S=O(n)
    DP=[0]*len(nums)# DP[i]代表到i为止的最大连续子序列和
    DP[0]=nums[0]
    for i in range(1,len(nums)):
        DP[i]=max(nums[i],DP[i-1]+nums[i])# 要么是只要当前nums[i]（代表DP[i-1]为负数，要么就是nums[i]加上DP【i-1s]
    return max(DP)



print(maxSubArray([-1,-1,-1]))