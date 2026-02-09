from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # T=O(n)
        # Edge Case
        # if len(nums)==1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     if nums[i]<nums[i-1]:
        #         return nums[i]

        # Follow-up T=O(logn) Binary Search
        # Edge Case
        if len(nums)==1:
            return nums[0]
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<nums[r]:# means the minimum element is within [l,mid]
                r=mid
            else:# means the minimum element is within [mid+1,r]
                l=mid+1

        return nums[l]




if __name__ == '__main__':
    solution=Solution()
    print(solution.findMin([4,5,6,7]))