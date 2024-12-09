def isValid(s: str) -> bool:
    stack=[]
    for i in range(len(s)):
        if(s[i]=="("):
            stack.append(")")
        elif(s[i]=="["):
            stack.append("]")
        elif(s[i]=="{"):
            stack.append("}")
        elif(not stack or stack[-1]!=s[i]):#括号没有和栈顶元素匹配上、或者栈为空但字符串还没遍历完
            return False
        else:
            stack.pop()
    if(stack):
        return False
    return True

if __name__ == '__main__':
    print(isValid("({[]})("))