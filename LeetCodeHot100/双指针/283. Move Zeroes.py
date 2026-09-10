from typing import List


def moveZeroes(nums: List[int])->None:
    # Edge Case
    if not nums:
        return

    # Basic Solution
    # T=O(n) S=O(1)
    l=0# l代表最后一个非0元素的位置+1
    r=0# r来遍历列表
    for r in range(len(nums)):
        if nums[r] != 0:# 如果当前元素非0，则交换
            nums[l],nums[r]=nums[r],nums[l]
            l+=1

    return




if __name__ == '__main__':
    nums=[0,1,0,3,12]
    moveZeroes(nums)
    print(nums)