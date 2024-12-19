class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(")")
            elif(s[i]=="["):
                stack.append("]")
            elif(s[i]=="{"):
                stack.append("}")
            else:
                if(not stack):#如果没有足够的匹配括号，则不是有效括号
                    return False
                elif(stack.pop()!=s[i]):#如果括号不匹配，则不是有效括号
                    return False
        if(stack):#如果还有多余括号，则不是有效括号
            return False
        return True





if __name__ == '__main__':
    solution=Solution()
    print(solution.isValid("{()}]"))