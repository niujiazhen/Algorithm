from typing import List

#第一次15分钟，超时
#第二次看思路做，通过

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen=len(nums)
        if(sum(nums)<target):
            return 0
        else:
            count=0
            l=0
            for r in range(len(nums)):
                count+=nums[r]
                while(count>=target):
                    minLen=min(minLen,r-l+1)
                    count-=nums[l]
                    l+=1
        return minLen




if __name__ == '__main__':
    solution=Solution()
    print(solution.minSubArrayLen(4,[1,4,4]))