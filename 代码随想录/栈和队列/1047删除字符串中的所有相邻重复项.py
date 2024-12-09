def removeDuplicates(s: str) -> str:
    stack=[]
    for i in range(len(s)):
        if(len(stack)==0):
            stack.append(s[i])
        else:
            if(stack[-1]==s[i]):
                stack.pop()
            else:
                stack.append(s[i])
    return ''.join(stack)

if __name__ == '__main__':
    print(removeDuplicates("azxxzy"))