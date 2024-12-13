from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen=99999999999999
        l=r=0
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]
            while(sum>=target):
                minlen=min(minlen,r-l+1)
                sum-=nums[l]
                l+=1
        if(minlen==99999999999999):
            return 0
        return minlen

if __name__ == '__main__':
    solution=Solution()
    print(solution.minSubArrayLen(4, [1,4,4]))
