from typing import List

def maxProfit(prices: List[int])->int:
    # Edge Case
    if not prices:
        return 0

    # T=O(n) S=O(n)
    curMin=prices[0]# 记录当前最低股价
    maxGain=0# 记录历史最大利润

    for i in range(1,len(prices)):
        maxGain=max(maxGain,prices[i]-curMin)# 先计算在当前股价下最多能赚多少利润
        curMin=min(curMin,prices[i])# 更新curMin

    return maxGain


print(maxProfit([7,1,5,3,6,4]))