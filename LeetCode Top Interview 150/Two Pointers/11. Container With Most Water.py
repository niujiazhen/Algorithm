from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Two Pointer T=O()
        nums.sort()
        ans=[]
        for i in range(len(nums)):#fix one num
            if nums[i]>0:#because the list is sorted in ascending order, if the first element is greater than 0, it's impossible to have a triplet = 0
                break
            if i>0 and nums[i]==nums[i-1]:#remove the duplicate first num
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:#remove the duplicate second num
                        l+=1
                    while l<r and nums[r]==nums[r-1]:#remove the duplicate third num
                        r-=1
                    l+=1
                    r-=1
        return ans



if __name__ == '__main__':
    solution=Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))