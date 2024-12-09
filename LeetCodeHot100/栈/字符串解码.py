def decodeString(s: str) -> str:
    stack=[]
    ans=''
    i: int=0
    while(i<len(s)):
        if(s[i].isnumeric()):
            #如果是数字，则把本地需要复制的数字全部取出来，知道遇到[为止
            num=''
            while(s[i]!='['):
                num+=s[i]
                i+=1
            stack.append(num)
        elif(s[i].isalpha()):
            #如果是字母，则把遇到]之前的所有字母放入栈内
            while(i<len(s) and s[i].isalpha()):
                stack.append(s[i])
                i+=1
        elif(s[i]==']'):
            #先把第一个数字前所有字符拿出来，用来复制
            ss=[]
            while(stack[-1].isalpha()):
                ss.append(stack.pop())
            num=int(stack.pop())#数字只占一位
            ss=''.join(reversed(ss))
            stack.append(num*ss)
            i+=1
        else:
            i += 1  # 遇到[直接pass
    return ''.join(stack)


if __name__ == '__main__':
    print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
