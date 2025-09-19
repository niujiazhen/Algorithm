import math


class Solution:
    def isHappy(self, n: int) -> bool:
        #T=O(logn), S=O(logn)
        s=set()
        while 1:
            sum=0
            while n>0:
                sum+=pow(n%10,2)
                n//=10
            if sum==1:
                return True
            elif sum in s:
                return False
            s.add(sum)
            n=sum


if __name__ == '__main__':
    solution=Solution()
    print(solution.isHappy(2))