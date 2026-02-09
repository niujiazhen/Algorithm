class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP T=O(n) S=O(1)
        curMin=float("inf")
        maxProfit=0
        for i in range(len(prices)):
            maxProfit=max(maxProfit,prices[i]-curMin)
            curMin=min(curMin,prices[i])

        return maxProfit

if __name__ == '__main__':
    solution=Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))