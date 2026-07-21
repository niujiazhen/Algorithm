from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the pivot element O(logn)
        n=len(nums)
        l=0
        r=n-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<nums[r]:
                r=mid
            else:
                l=mid+1
        pivot=l

        # Find the target element from left part [0,pivot-1]
        l=0
        r=pivot-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        # Find the target element from right part [pivot,n-1]
        l=pivot
        r=n-1
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