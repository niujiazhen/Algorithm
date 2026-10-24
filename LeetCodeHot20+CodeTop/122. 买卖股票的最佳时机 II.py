from typing import List

def maxProfit(prices: List[int])->int:
    # Edge Case
    if not prices:
        return 0
    # 贪心：赚取所有上涨空间
    sum=0
    for i in range(len(prices)-1):
        sum+=max(0,prices[i+1]-prices[i])

    return sum


print(maxProfit([7, 1, 5, 3, 6, 4]))