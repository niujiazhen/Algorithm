import sys

def longestPalindrome(s: str)->str:
    # Edge Case
    if not s:
        return None

    # 双指针+中心扩展
    # T=O(n2), S=O(1)
    start=0# 记录回文子串开始的下标位置
    maxLen=1# 记录回文子串最大长度

    # 中心扩展函数：从l，r两边扩展，返回可能的最大回文子串长度
    def expand(l: int, r: int)->int:
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return r-l-1# 实际回文子串长度

    # 枚举每个可能的中心位置
    for i in range(len(s)):
        # 奇数子串：以s[i]为中心
        len1=expand(i,i)
        # 偶数子串：以s[i:i+1]为中心
        len2=expand(i,i+1)

        curLen=max(len1,len2)

        if curLen>maxLen:
            maxLen=curLen
            start=i-(curLen-1)//2# 记录最长子串开始的下标位置

    return s[start:start+maxLen]

s=sys.stdin.readline().strip()
print(longestPalindrome(s))