from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    result=[]
    n=len(nums)
    nums.sort()
    for i in range(n):
        #如果最小的元素都大于0，则不可能凑出三数之和=0的三元组，直接返回当前结果
        if(nums[i]>0):
            return result
        #第一个元素的去重
        if(i>0 and nums[i]==nums[i-1]):
            continue
        l=i+1
        r=n-1
        while(l<r):
            if(nums[i]+nums[l]+nums[r]>0):
                r-=1
            elif(nums[i]+nums[l]+nums[r]<0):
                l+=1
            else:
                result.append([nums[i],nums[l],nums[r]])
                #第二个元素去重
                while(l<r and nums[l]==nums[l+1]):
                    l+=1
                #第三个元素去重
                while(l<r and nums[r]==nums[r-1]):
                    r-=1
                l+=1
                r-=1
    return result












if __name__ == '__main__':
    print(threeSum([1,-1,-1,0]))