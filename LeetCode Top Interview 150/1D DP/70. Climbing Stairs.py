class Solution:
    def climbStairs(self, n: int) -> int:
        #T=O(n) S=O(n)
        #Edge Case
        if n==1:
            return 1
        #we use dp to solve the problem
        DP=[0]*(n+1)
        #initialize
        DP[1]=1
        DP[2]=2
        for i in range(3,n+1):
            #each DP[i] equals to DP[i-1]+one step +DP[i-2]+two steps
            DP[i]=DP[i-1]+DP[i-2]
        return DP[n]



if __name__ == '__main__':
    solution=Solution()
    print(solution.climbStairs(2))