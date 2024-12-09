def reverseStr(s: str, k: int) -> str:
    s=list(s)
    for i in range(0,len(s),2*k):
        if(i+k<=len(s)):
            reverse(s,i,i+k)
        else:
            reverse(s,i,len(s))
    return ''.join(s)



#反转区间[start,end)内的字符串
def reverse(s:str,start:int,end:int)->None:
    n=end-start#区间长度
    for i in range(start,start+n//2):
        t=s[i]
        s[i]=s[end-i-1+start]
        s[end-i-1+start]=t


print(reverseStr("abcd", 2))

