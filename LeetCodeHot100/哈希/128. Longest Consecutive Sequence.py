from typing import List


def longestConsecutive(nums: List[int]) -> int:
    # Edge Case
    if not nums:
        return 0

    # Basic Solution
    # T=O(n) S=O(n)
    hash=set()# 记录出现过的数字
    maxLen=1# 记录最大长度，至少是1

    # 记录哪些数字出现过
    for i in range(len(nums)):
        hash.add(nums[i])

    # 检测最长连续序列
    for num in hash:
        # 剪枝操作：当num为某个序列开头，则开始检测
        if num-1 not in hash:
            curLen=0
            while num in hash:# 这些连续的数字都记录到极大值内，并且他们在后续不可能进入if num-1 not in hash（由于不是序列开头），所以每个数字只计算1次，O(n)
                curLen+=1
                num+=1
            maxLen=max(maxLen,curLen)

    return maxLen





if __name__ == '__main__':
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))