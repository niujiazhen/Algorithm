from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen=0
        num_set=set(nums)
        for num in num_set:
            if num-1 not in num_set:#means the current num is the start of a consecutive sequence
                cur_num=num
                curLen=1
                while cur_num+1 in num_set:
                    curLen+=1
                    cur_num=cur_num+1
                maxLen=max(maxLen,curLen)
        return maxLen







if __name__ == '__main__':
    solution=Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2]))