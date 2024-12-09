from collections import defaultdict
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    pre = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        pre[i+1]=pre[i]+nums[i]

    ans = 0
    cnt = defaultdict(int)
    for sj in pre:
        ans += cnt[sj - k]
        cnt[sj] += 1
    return ans

if __name__ == '__main__':
    print(subarraySum([-1,-1,1],0))