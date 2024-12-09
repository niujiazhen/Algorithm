#用时9:53
class Solution:
    def reverseStr(self,s: str, k: int) -> str:
        sList=list(s)
        n=len(sList)
        for i in range(0,n,2*k):
            if(i+k<n):
                self.reversePart(sList,i,i+k)
            else:
                self.reversePart(sList,i,n)
        return ''.join(sList)



    def reversePart(self,sList:list,start:int,end:int):
        sList[start:end]=sList[start:end][::-1]









if __name__ == '__main__':
    solution=Solution()
    print(solution.reverseStr("abcdefg",3))