from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #T=O(n2) and S=O(1) TLE
        # maxAns=0 #denotes the max profit
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         maxAns=max(maxAns,prices[j]-prices[i])
        # return maxAns

        #T=O(n) and S=O(1)
        minPrice=float("inf")# denotes the min price before today
        max_profit=0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice=prices[i] # the current min price
            elif prices[i]-minPrice>max_profit:
                max_profit=prices[i]-minPrice
        return max_profit







if __name__ == '__main__':
    solution=Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
