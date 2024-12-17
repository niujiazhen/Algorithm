from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()#排序，从小到大枚举
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):#对于除了循环第一个以外的元素i去重
                continue
            for j in range(i+1,len(nums)):
                if(j>i+1 and nums[j]==nums[j-1]):#对于除了第一个以外的元素j去重
                    continue
                l=j+1
                r=len(nums)-1
                while(l<r):
                    sum=nums[i]+nums[j]+nums[l]+nums[r]
                    if(sum>target):
                        r-=1
                    elif(sum<target):
                        l+=1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        while(l<r and nums[l]==nums[l+1]):#对于l元素去重
                            l+=1
                        while(l<r and nums[r]==nums[r-1]):#对于r元素去重
                            r-=1
                        l+=1
                        r-=1
        return ans





if __name__ == '__main__':
    solution=Solution()
    print(solution.fourSum([1,0,-1,0,-2,2], 0))