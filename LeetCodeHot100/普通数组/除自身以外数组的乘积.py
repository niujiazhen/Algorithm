from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    ans=[1]*len(nums)
    #前缀乘积
    for i in range(len(nums)-1):
        ans[i+1]=ans[i]*nums[i]
    last=nums[len(nums)-1]#后缀元素从1开始
    #后缀乘积
    for i in range(len(nums)-1,0,-1):
        ans[i-1]=last*ans[i-1]
        last*=nums[i-1]

    return ans

if __name__ == '__main__':
    print(productExceptSelf([-1,1,0,-3,3]))