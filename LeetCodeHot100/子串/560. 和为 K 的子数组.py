from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Edge Case
        if not nums:
            return 0
        # Basic Solution: Hash Table + Prefix Sum
        prefix_sum={}# prefix_sum[i]=j 代表当前前缀和为i的连续子序列有j个
        prefix_sum[0]=1# 前缀和为0的子序列有1个，即空序列
        cur_sum=0
        ans=0

        for num in nums:
            cur_sum += num# 记录当前的前缀和
            ans += prefix_sum.get(cur_sum-k,0) # 当前前缀和需要减去curSum-k的前缀和，才能凑出值为k的连续子序列，因此ans加上这个curSum-k的频率,没有的话就+0
            prefix_sum[cur_sum]=prefix_sum.get(cur_sum,0)+1

        return ans





if __name__ == '__main__':
    solution=Solution()
    print(solution.subarraySum([-1,-1,1],0))