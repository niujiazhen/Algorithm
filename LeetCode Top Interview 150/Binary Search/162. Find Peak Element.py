from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # The peak element must be at the end of any rising slope
        # So we should find the end of a rising slope
        # T=O(logn) S=O(1)
        def binarysearch(l:int,r:int)->int:
            if l==r:#we find the peak element
                return l
            mid=(l+r)//2
            if nums[mid]>nums[mid+1]:#means the current point mid is on a falling slope
                return binarysearch(l,mid)#we should search the left part [l,mid] because the mid point might be the peak element
            return binarysearch(mid+1,r)#Otherwise, we search the right part [mid+1,r] because the mid point cannot be the peak element due to mid<mid+1

        return binarysearch(0, len(nums) - 1)


if __name__ == '__main__':
    solution=Solution()
    print(solution.findPeakElement([1,2,1,3,5,6,4]))