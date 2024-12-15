from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            if(target-nums[i] in hash):#查看是否有和当前元素凑够target的元素在hash中
                return [hash[target-nums[i]],i]#返回下标
            hash[nums[i]]=i#存储下标





if __name__ == '__main__':
    solution=Solution()
    print(solution.twoSum([3,3], 6))