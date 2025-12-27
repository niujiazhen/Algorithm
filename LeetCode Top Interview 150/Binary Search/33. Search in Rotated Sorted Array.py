from typing import List
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        #we first find the pivot element (smallest) using binary search
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>nums[-1]:#means the pivot element is at the right part
                l=mid+1
            else:
                r=mid-1#means the pivot element is at the left part
        pivot=l#pivot is the l index nums because nums[mid]>nums[-1]

        #Then we use two binary search to search two parts to find the index of target number
        def binarySearch(l: int, r: int)->int:
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1

        #First search the left part
        ans=binarySearch(0,pivot-1)
        if ans!=-1:
            return ans
        else:
            return binarySearch(pivot,len(nums)-1)






if __name__ == '__main__':
    solution=Solution()
    print(solution.search([4,5,6,7,0,1,2],0))