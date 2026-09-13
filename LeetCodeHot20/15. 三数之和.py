from typing import List
def threeSum(nums:List[int])->List[List[int]]:
    # T=O(n2) S=O(n)
    nums.sort()
    ans=[]

    # 遍历第一个元素
    for i in range(len(nums)):
        # 剪枝
        if nums[i]>0:
            return ans
        # 元素1去重
        if i!=0 and nums[i]==nums[i-1]:
            continue
        # 双指针求元素2和3
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
                # 元素2去重
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                # 元素3去重
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                l+=1
                r-=1
    return ans



print(threeSum([-1, 0, 1, 2, -1, -4]))


