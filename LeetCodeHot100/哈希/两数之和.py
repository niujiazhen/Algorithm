from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hash={}
    for i in range(len(nums)):
        hash[nums[i]]=i
    for i in range(len(nums)):
        if(target-nums[i] in hash and i!=hash[target-nums[i]]):
            return [i,hash[target-nums[i]]]











if __name__ == '__main__':
    print(twoSum([3,3],6))