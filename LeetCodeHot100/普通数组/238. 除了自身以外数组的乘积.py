from typing import List

def productExceptSelf(nums: List[int])->List[int]:
    # Edge Case
    if not nums:
        return []

    # 前缀积+后缀积 T=O(n) S=O(n)
    n=len(nums)
    prefixProduct=[1]*n
    suffixProduct=[1]*n

    # 计算前缀积：元素i之前的乘积
    for i in range(1,n):
        prefixProduct[i]=prefixProduct[i-1]*nums[i-1]

    # 计算后缀积：元素i之后的乘积
    for i in range(n-2,-1,-1):
        suffixProduct[i]=suffixProduct[i+1]*nums[i+1]

    ans=[]
    for i in range(n):
        ans.append(prefixProduct[i]*suffixProduct[i])

    return ans

if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))