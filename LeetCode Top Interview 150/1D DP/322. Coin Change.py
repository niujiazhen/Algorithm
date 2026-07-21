from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Complete KnapStack T=O(amount*n) S=O(n)
        #We define DP[i] representing the minimum number of coins needed to make up amount i
        DP=[float("inf")]*(amount+1)
        #Initialize:we need 0 coins to make up 0 amount of money
        DP[0]=0

        for coin in coins:
            for i in range(amount+1):
                if i>=coin:#means we have the chance to use this type of coin to make up i amount of money
                    DP[i]=min(DP[i],DP[i-coin]+1)

        if DP[amount]!=float("inf"):
            return DP[amount]
        else:
            return -1




if __name__ == '__main__':
    solution=Solution()
    print(solution.coinChange([1,2,5],11))