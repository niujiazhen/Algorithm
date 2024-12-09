from typing import List


class Solution:
    def __init__(self):
        self.letterMap=[
            "",
            "",
            "abc",#2
            "def",#3
            "ghi",#4
            "jkl",#5
            "mno",#6
            "pqrs",#7
            "tuv",#8
            "wxyz",#9
        ]
    def letterCombinations(self, digits: str) -> List[str]:
        result=[]#结果集合
        ans=""#单个字母组合
        index=0#递归深度、ans长度、当前遍历digits字符串的下标位置
        if(len(digits)==0):
            return result
        else:
            self.backtracking(result,ans,digits,index)
            return result





    def backtracking(self,result:list,ans:str,digits:str,index:int):
        if(len(ans)==len(digits)):#如果当前ans的长度已经满足一个字母组合了，则加入result结果集合
            result.append(ans)
            return
        #如果ans还不满组一个字母组合，则开始递归
        s=self.letterMap[int(digits[index])]#数字对应的map字符串
        for i in range(len(s)):
            ans+=s[i]
            self.backtracking(result,ans,digits,index+1)#继续递归下一层ans
            ans=ans[:-1]






if __name__ == '__main__':
    solution=Solution()
    print(solution.letterCombinations("23"))