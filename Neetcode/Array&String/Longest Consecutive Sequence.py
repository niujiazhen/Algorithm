from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # T=O(n) S=O(n)
        # Edge Case
        if not nums:
            return 0

        # Normal Situation
        hash=set()# to record if a num exist in nums
        for num in nums:
            hash.add(num)

        maxLen=0

        for num in hash:
            if num-1 not in hash:# represents that current num might be the start of a consecutive sequence
                curLen=0
                while num in hash:
                    curLen+=1
                    num+=1
                maxLen=max(maxLen,curLen)

        return maxLen



if __name__ == '__main__':
    solution=Solution()
    print(solution.longestConsecutive([2,20,4,10,3,4,5]))