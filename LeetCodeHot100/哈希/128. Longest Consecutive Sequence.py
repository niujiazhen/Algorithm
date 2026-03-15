from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge Case
        if not nums:
            return 0

        # Basic Solution
        hash=set()
        maxLen=0

        for num in nums:
            hash.add(num)

        for num in hash:
            if num-1 not in hash: # 当前num是某个数字序列的开头，则开始计算长度
                curLen = 0
                curNum = num
                while curNum in hash:
                    curLen+=1
                    curNum+=1
                maxLen=max(maxLen,curLen)

        return maxLen



if __name__ == '__main__':
    solution=Solution()
    print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))