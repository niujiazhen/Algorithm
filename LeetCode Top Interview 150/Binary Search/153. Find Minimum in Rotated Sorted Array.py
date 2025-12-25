from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        #we should find the pivot element, which is the minimum element
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>nums[-1]:#means the pivot element is within [mid+1,n-1]
                l=mid+1
            else:#means the pivot element is within [0,mid-1]
                r=mid-1
        return nums[l]#after the binary search, the index of pivot element is l


if __name__ == '__main__':
    solution=Solution()
    print(solution.findMin([3,4,5,1,2]))