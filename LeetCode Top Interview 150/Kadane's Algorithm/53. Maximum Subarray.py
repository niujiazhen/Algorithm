from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #one-dimension Dynamic Programming
        #T=O(n) S=O(n)
        # OPT=[0]*len(nums)#OPT[i] denotes the current max sum of subarray within (0,i)
        # OPT[0]=nums[0]
        # sum=nums[0]
        # for i in range(1,len(nums)):
        #     if sum>0:
        #         OPT[i]=sum+nums[i]
        #         sum+=nums[i]
        #     else:
        #         OPT[i]=nums[i]
        #         sum=nums[i]
        # return max(OPT)

        #Kadane's Algorithm
        current_sum=nums[0]#current_sum denotes the max subarray sum within index(0,i)
        max_sum=current_sum#max_sum denotes the final answer
        for i in range(1,len(nums)):
            current_sum=max(current_sum+nums[i],nums[i])
            max_sum=max(max_sum,current_sum)
        return max_sum



if __name__ == '__main__':
    solution=Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))