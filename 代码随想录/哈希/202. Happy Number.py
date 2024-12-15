class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set=set()
        while(1):
            if(n in hash_set):
                return False
            hash_set.add(n)
            sum=0
            while(n>0):
                num=n%10
                sum+=num**2
                n//=10
            if(sum==1):
                return True
            n=sum







if __name__ == '__main__':
    solution=Solution()
    print(solution.isHappy(2))