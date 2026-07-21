from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two Pointer
        # T=O(n) S=O(1)
        l=r=0 # l指针代表当前处理好的不含0序列结尾，r指针代表遍历的元素

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1

        return


if __name__ == '__main__':
    solution=Solution()
    nums=[0,1,0,3,12]#1,3,12,0,0
    print(solution.moveZeroes(nums))
    print(nums)


    #0,1,0,3,12