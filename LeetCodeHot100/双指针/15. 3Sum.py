from typing import List
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # T=O(nlogn) S=O(1)
        nums.sort()# 避免乱序重复
        ans=[]

        for i in range(len(nums)):
            if nums[i]>0:# 如果最小的数都大于0，则不可能凑出triplet=0，直接返回当前答案
                return ans
            # 去重逻辑：对于相同的数字，只选第一次出现的，接下来连续出现的都跳过
            # 元素1的去重
            if i!=0 and nums[i]==nums[i-1]:# 重复了则跳过
                continue

            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:# 找到一个triplet=0
                    ans.append([nums[i],nums[l],nums[r]])
                    # 元素2去重
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    # 元素3去重
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    # 找一对新的数字继续尝试
                    l+=1
                    r-=1

        return ans





if __name__ == '__main__':
    solution=Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))