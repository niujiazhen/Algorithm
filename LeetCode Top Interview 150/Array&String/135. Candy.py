from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        #T=O(n) S=O(n)
        n=len(ratings)
        leftToRight=[1]*n# only consider the left neighbour
        rightToLeft=[1]*n# only consider the right neighbour

        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                leftToRight[i]=leftToRight[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                rightToLeft[i]=rightToLeft[i+1]+1

        sum=0
        for i in range(n):
            sum+=max(leftToRight[i],rightToLeft[i])

        return sum

if __name__ == '__main__':
    solution=Solution()
    print(solution.candy([1,2,87,87,87,2,1]))