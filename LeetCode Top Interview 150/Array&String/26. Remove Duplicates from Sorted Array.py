from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time Complexity=O(N), Space Complexity=O(N)
        # i=j=0 #two pointers
        # ans=[]
        # while j<len(nums):
        #     j+=1
        #     while j<len(nums) and nums[j]==nums[i]:
        #         j+=1
        #     ans.append(nums[i])
        #     i=j
        # nums[:len(ans)] = ans[:]
        # return len(ans)

        # Time Complexity=O(N), Space Complexity=O(1)
        inserIndex=1 #we just add the first different element to inserIndex
        i=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:# it means nums[i] is the first different element and can be added to insertIndex
                nums[inserIndex]=nums[i]
                inserIndex+=1
        return inserIndex






if __name__ == '__main__':
    solution=Solution()
    nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(solution.removeDuplicates(nums))
    print(nums)


