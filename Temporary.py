from typing import List

def subarraySum(nums: List[int], k: int)->int:
    # Edge Case
    if not nums:
        return 0

    # 哈希表+前缀和
    pre_sum={}# prefix[i]=j代表：前缀和为i的子串有j个
    pre_sum[0]=1# 前缀和为0的子串天然有一个，即为空子串
    curSum=0
    ans=0

    for i in range(len(nums)):
        curSum+=nums[i]# 计算前缀和
        ans+=pre_sum.get(curSum-k,0)# 当前前缀和需要减去curSum-k的前缀和，才能凑出值为k的连续子序列，因此ans加上这个curSum-k的频率,没有的话就+0
        pre_sum[curSum]=pre_sum.get(curSum,0)+1# 记录前缀和为curSum的数组有几个


    return ans


if __name__ == '__main__':
    print(subarraySum([1, 2, 3],3))