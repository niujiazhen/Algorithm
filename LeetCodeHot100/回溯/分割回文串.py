from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]#结果集
        path=[]#单个回文串切割情况
        startIndex=0#开始第一个可以切割的位置,0代表可以在s[0]和s[1]之间切割
        self.backtracking(result,path,s,startIndex)
        return result




    def backtracking(self,result:list,path:list,s:str,startIndex:int)->None:
        if(''.join(path)==s):#递归终止条件：当前path组成的字符串和原字符串相等,且均为回文子串
            result.append(path[:])
            return
        #否则从startIndex开始遍历
        for i in range(startIndex,len(s)):
            if(self.isPalindrome(s[startIndex:i+1])):
                path.append(s[startIndex:i + 1])  # 每次递归切割1~n的回文子串
                self.backtracking(result, path, s, i + 1)
                path.pop()  # 回溯




    def isPalindrome(self,s:str)->bool:
        return s==s[::-1]




if __name__ == '__main__':
    solution=Solution()
    print(solution.partition("aab"))