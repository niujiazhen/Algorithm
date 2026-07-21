from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #T=O(n) S=O(1)
        currMin=prices[0]
        maxGain=0
        for i in range(1,len(prices)):
            maxGain=max(maxGain,prices[i]-currMin)
            currMin=min(currMin,prices[i])

        return maxGain




if __name__ == '__main__':
    solution=Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))