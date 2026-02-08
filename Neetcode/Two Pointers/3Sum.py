from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # T=O(n2) S=O(1)
        nums.sort()# help use a binary search to reduce time complexity O(nlogn)
        ans=[]
        n=len(nums)

        for i in range(len(nums)):
            # Edge Case
            if nums[i]>0:#because it's impossible to form a triplet with sum 0 in a sorted list
                return ans
            # avoid duplicated element of first num
            if i!=0 and nums[i]==nums[i-1]:# we should choose the first element of same num to pass testcase like [0,0,0]
                continue
            l=i+1
            r=n-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:#sum=0
                    ans.append([nums[i],nums[l],nums[r]])
                    # avoid duplicated element of second num
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    # avoid duplicated element of third num
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1

        return ans




if __name__ == '__main__':
    solution=Solution()
    print(solution.threeSum([1,-1,-1,0]))