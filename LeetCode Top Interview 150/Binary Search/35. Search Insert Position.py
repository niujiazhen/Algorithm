from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Binary Seafch
        #T=O(logn) S=O(1)
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        #if we did not find the target, the loop will terminate at left=right+1, and nums[right]<target<nums[left]
        #so we should insert the target at index left
        return l



if __name__ == '__main__':
    solution=Solution()
    print(solution.searchInsert([1,3,5,6],2))