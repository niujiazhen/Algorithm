from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # T=O(n2)
        nums.sort()
        result=[]

        # We first fix one number
        for i in range(len(nums)):
            # Edge Case
            if nums[i]>0:
                return result #because there cannot be a triple set in a sorting list to add up = 0
            # avoid duplicated element of the first number
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum==0:
                    result.append([nums[i],nums[l],nums[r]])
                    #avoid duplicated element of the second number
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    # avoid duplicated element of the third number
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif sum>0:
                    r-=1
                else:
                    l+=1

        return result




if __name__ == '__main__':
    solution=Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))