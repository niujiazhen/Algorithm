from typing import List


def maxSubArray(nums: List[int]) -> int:
    n=len(nums)
    dp=[0]*n
    dp[0]=nums[0]
    ans=dp[0]
    for i in range(1,n):
        dp[i]=max(dp[i-1]+nums[i],nums[i])
        ans=max(ans,dp[i])
    return ans

if __name__ == '__main__':
    print(maxSubArray([5,4,-1,7,8]))