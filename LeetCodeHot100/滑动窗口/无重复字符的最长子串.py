def lengthOfLongestSubstring(s: str) -> int:
    set1=set()
    maxLen=0
    l=r=0
    while(r<len(s)):
        if(s[r] in set1):
            set1.remove(s[l])
            l+=1
        else:
            set1.add(s[r])
            r+=1
        maxLen = max(maxLen, r - l)
    return maxLen


if __name__ == '__main__':
    print(lengthOfLongestSubstring("pwwkew"))
    