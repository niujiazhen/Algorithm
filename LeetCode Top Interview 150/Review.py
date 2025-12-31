from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen=0
        hash=set(nums)
        for num in hash:
            if num-1 not in hash:# means current num is the start of a sequence
                curNum=num
                curLen=1
                while curNum+1 in hash:
                    curNum+=1
                    curLen+=1
                maxLen=max(maxLen,curLen)

        return maxLen






if __name__ == '__main__':
    solution=Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2]))