from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #T=O(n), S=O(1)
        l=r=0
        ans=[]
        while r<len(nums):
            if r<len(nums)-1 and nums[r+1]-nums[r]!=1:#means there is a new range
                if l==r:
                    ans.append(str(nums[l]))
                else:
                    ans.append(str(nums[l])+"->"+str(nums[r]))
                l=r+1
            elif r==len(nums)-1:
                if l==r:
                    ans.append(str(nums[l]))
                else:
                    ans.append(str(nums[l])+"->"+str(nums[r]))
                l=r+1
            r+=1
        return ans



if __name__ == '__main__':
    solution=Solution()
    print(solution.summaryRanges([0,1,2,4,5,7]))