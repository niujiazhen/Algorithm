from typing import List

def twoSum(nums: List[int], target: int)->List[int]:
    # T=O(n) S=O(n)
    hash={}# 存储value->index
    for i in range(len(nums)):
        if target-nums[i] in hash:# 如果当前nums[i]需要的数字在hash中，直接返回答案
            return [hash[target-nums[i]],i]
        hash[nums[i]]=i# 加入哈希值

if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))