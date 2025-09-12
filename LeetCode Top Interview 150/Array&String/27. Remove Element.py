from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0;j=len(nums)-1# two pointers
        while i<=j:
            if nums[i]==val:#compare the two elements
                nums[i],nums[j]=nums[j],nums[i] # if equals, then swap
                j-=1
            else:
                i+=1
        nums[:]=nums[:j+1] #j indicates the index of last element which does not equal to val
        return j+1 #return the len





if __name__ == '__main__':
    solution=Solution()
    nums=[1]
    print(solution.removeElement(nums, 1))
    print(nums)
