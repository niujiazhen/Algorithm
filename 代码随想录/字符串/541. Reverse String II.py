from audioop import reverse


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr=list(s)
        for i in range(0,len(arr),2*k):
            if(i+k<len(arr)):
                self.reverseK(i,i+k,arr)
            else:
                self.reverseK(i,len(arr),arr)
        return "".join(arr)


    def reverseK(self, begin : int, end : int, arr : list)->None:
        for i in range(begin,(begin+end)//2):
            arr[i],arr[end+begin-i-1]=arr[end+begin-i-1],arr[i]





if __name__ == '__main__':
    solution=Solution()
    print(solution.reverseStr("abcd", 2))