from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #We use Kadane's Algorithm twice
        maxSum=nums[0]
        curMaxSum=maxSum
        minSum=nums[0]
        curMinSum=minSum
        totalSum=nums[0]

        for i in range(1,len(nums)):
            # We use Kadane's Algorithm to calculate the maxSubArraySum
            curMaxSum=max(curMaxSum+nums[i],nums[i])
            maxSum=max(maxSum,curMaxSum)
            # We use Kadane's Algorithm to calculate the minSubArraySum
            curMinSum=min(curMinSum+nums[i],nums[i])
            minSum=min(minSum,curMinSum)
            #we calculate the totalSum for circularSum
            totalSum+=nums[i]

        circularSum=totalSum-minSum#the truly circularSum

        #Edge Case:if the totalSum == minSum, which means the whole array is negative, we should return the maxSum because the circularSum is 0 which does not exist
        if totalSum==minSum:
            return maxSum
        return max(maxSum,circularSum)
if __name__ == '__main__':
    solution=Solution()
    print(solution.maxSubarraySumCircular([5,-3,5]))