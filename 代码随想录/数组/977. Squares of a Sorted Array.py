from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        LEN=len(nums)-1
        l,r=0,len(nums)-1
        while(l<=r):
            if(abs(nums[l])<abs(nums[r])):
                ans[LEN]=nums[r]**2
                r-=1
            else:
                ans[LEN]=nums[l]**2
                l+=1
            LEN-=1
        return ans





if __name__ == '__main__':
    solution=Solution()
    print(solution.sortedSquares([-7,-3,2,3,11]))
