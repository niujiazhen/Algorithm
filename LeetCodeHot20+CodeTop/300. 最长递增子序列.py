from typing import List

def lengthOfLIS(nums: List[int])->int:
    # Edge Case
    if not nums:
        return 0

    # T=O(n2) S=O(n)
    OPT=[1]*len(nums)# OPT[i]代表以i结尾的子序列的最长严格递增长度

    for i in range(1,len(nums)):
        for j in range(i):# 检查下标i之前的元素
            # 如果比结尾元素小，则有可能增加OPT[i]
            if nums[j]<nums[i]:
                OPT[i]=max(OPT[i],OPT[j]+1)

    return max(OPT)
if __name__ == '__main__':
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))