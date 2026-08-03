from typing import List

def threeSum(nums: List[int])->List[List[int]]:
    # Edge Case
    if not nums:
        return []

    # 双指针 T=O(n2)
    nums.sort()
    # [-4,-1,-1,0,1,2]
    ans=[]

    for i in range(len(nums)-2):# 遍历第一个元素
        # 剪枝
        if nums[i]>0:# 第一个元素大于0，不可能有sum为0的三元组
            break
        # 第一个元素去重
        if i>0 and nums[i]==nums[i-1]:
            continue
        # if
        # 双指针
        l=i+1
        r=len(nums)-1
        while l<r:
            sum=nums[i]+nums[l]+nums[r]
            if sum>0:
                r-=1
            elif sum<0:
                l+=1
            else:# sum为0，计入ans
                ans.append([nums[i],nums[l],nums[r]])
                # 第二个元素去重
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                # 第三个元素去重
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                # 继续计算下一个可能的三元组
                l+=1
                r-=1

    return ans

if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))