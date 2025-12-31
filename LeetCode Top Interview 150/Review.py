from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Two pointers T=O(n2) S=O(1)
        nums.sort()
        ans=[]
        n=len(nums)

        # We first fix one number
        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:# remove the duplicated elements of first number
                continue
            l=i+1
            r=n-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1

        return ans


if __name__ == '__main__':
    solution=Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))