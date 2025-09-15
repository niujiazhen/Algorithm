from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Time Complexity=O(n) Space Complexity=O(1)
        insertIndex=0
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:# means there is a new unduplicate element
                if i+1<len(nums) and nums[i]==nums[i+1]:# we can check if there is over 1 element or else
                    nums[insertIndex]=nums[i]
                    nums[insertIndex+1]=nums[i+1]
                    insertIndex+=2
                else:
                    nums[insertIndex] = nums[i]
                    insertIndex+=1
        return insertIndex











if __name__ == '__main__':
    solution = Solution()
    nums=[1,1,1,2,2,3]
    print(solution.removeDuplicates(nums))
    print(nums)





