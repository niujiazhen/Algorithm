from typing import List
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        #We first use binary search to find the pivot element index
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>nums[-1]:#if the mid element is greater than the last element, then the pivot element is in range [mid+1,n-1]
                l=mid+1
            else:
                r=mid-1#if the mid element is smaller than the last element, then the pivot element is in range [0,mid-1]
        pivot=l#after the binary search, the index of pivot element is l

        #we can use two binary search to find the target element
        ans=self.binarySearch(nums,0,pivot-1,target)
        if ans!=-1:
            return ans
        return self.binarySearch(nums,pivot,len(nums)-1,target)

    def binarySearch(self,nums:List[int],left:int,right:int,target:int)->int:
        l=left
        r=right
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return -1






if __name__ == '__main__':
    solution=Solution()
    print(solution.search([4,5,6,7,0,1,2],0))