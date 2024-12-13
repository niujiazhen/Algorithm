from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=r=0
        while(r<len(nums)):
            if(nums[r]!=val):
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1
        return l



if __name__ == '__main__':
    solution=Solution()
    nums=[3,2,2,3]
    print(solution.removeElement(nums, 3))
    print(nums)


