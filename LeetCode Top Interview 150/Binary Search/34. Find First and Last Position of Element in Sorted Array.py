from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=last=-1
        #First find the index of leftmost target element in the list
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                if mid==0 or nums[mid-1]!=target:#means we find the leftmost target element
                    first=mid
                    break
                else:#not the left most target element
                    r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        #Then find the index of rightmost target element in the list
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid + 1] != target:  # means we find the rightmost target element
                    last = mid
                    break
                else:  # not the right most target element
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [first,last]



if __name__ == '__main__':
    solution=Solution()
    print(solution.searchRange([2,2],2))