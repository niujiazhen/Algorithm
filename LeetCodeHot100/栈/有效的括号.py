def isValid(s: str) -> bool:
    stack=[]
    for i in range(len(s)):
        if(s[i]=="("):
            stack.append(")")
        elif(s[i]=="["):
            stack.append("]")
        elif(s[i]=="{"):
            stack.append("}")
        elif(not stack):#栈中没有足够的右括号来匹配
            return False
        elif(stack[-1]!=s[i]):#栈中最上层的右括号不匹配
            return False
        else:#否则将栈顶匹配的右括号弹出
            stack.pop()
    if(stack):#如果字符串遍历完，栈中还有右括号也说明匹配失败
        return False
    return True

if __name__ == '__main__':
    print(isValid("()"))