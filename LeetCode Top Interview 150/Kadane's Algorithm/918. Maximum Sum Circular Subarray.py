from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum=nums[0]
        curMaxSum=nums[0]
        minSum=nums[0]
        curMinSum=nums[0]
        totalSum=nums[0]

        for i in range(1,len(nums)):
            #Kadane's Algorithm to calculate maxSubSum
            curMaxSum=max(curMaxSum+nums[i],nums[i])
            maxSum=max(maxSum,curMaxSum)
            # Kadane's Algorithm to calculate minSubSum
            curMinSum=min(curMinSum+nums[i],nums[i])
            minSum=min(minSum,curMinSum)
            totalSum+=nums[i]
        #the actual circularSum
        circularSum=totalSum-minSum
        #Edge Case:all number are negative, the answer should be the whole array
        if circularSum==0:#means all numbera are negative
            return maxSum
        return max(maxSum,circularSum)
if __name__ == '__main__':
    solution=Solution()
    print(solution.maxSubarraySumCircular([5,-3,5]))