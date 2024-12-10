from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                l+=1
            else:
                r-=1
        return -1



if __name__ == '__main__':
    solution=Solution()
    print(solution.search([5], 5))
