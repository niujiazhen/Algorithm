from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:# if the first element is greater than 0, there is no triplet answer
                return ans
            if i>0 and nums[i]==nums[i-1]:# remove the duplicated first element
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum<0:
                    l+=1
                elif sum>0:
                    r-=1
                else:#means the sum=0
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:#remove the duplicated second element
                        l+=1
                    while l<r and nums[r]==nums[r-1]:#remove the duplicated third element
                        r-=1
                    l+=1
                    r-=1
        return ans


if __name__ == '__main__':
    solution=Solution()
    print(solution.threeSum([-100,-70,-60,110,120,130,160]))