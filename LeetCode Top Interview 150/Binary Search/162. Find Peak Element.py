from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Recursive Binary Search
        #the peak could only be at the end of a rising slope, so we should find the rising slope range first
        return self.binarySearch(nums,0,len(nums)-1)
    def binarySearch(self,nums:List[int],l:int,r:int)->int:
        if l==r:#we find the peak
            return l
        mid=(l+r)//2
        if nums[mid]>nums[mid+1]:#the current element nums[mid] is in a falling slope
            return self.binarySearch(nums,l,mid)#the peak coule possibly be within index at (l,mid) because (l,mid) might be a rising slope
        return self.binarySearch(nums,mid+1,r)#the peak could possibly be with index at (mid+1,r) because (mid+1,r) might be a rising slope

if __name__ == '__main__':
    solution=Solution()
    print(solution.findPeakElement([1,2,1,3,5,6,4]))