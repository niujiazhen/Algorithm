from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We use hashtable to solve
        #T=O(n) S=O(n)
        hash={}#hash[i] records the index of nums whose value is i

        for i in range(len(nums)):
            #we first check if target-nums[i] is already in hashtable
            if target-nums[i] in hash:
                #if so, return the answer
                return [i,hash[target-nums[i]]]
            hash[nums[i]]=i




if __name__ == '__main__':
    solution=Solution()
    print(solution.twoSum([2,7,11,15]))