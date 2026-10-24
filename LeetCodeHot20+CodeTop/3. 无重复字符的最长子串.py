
def lengthOfLongestSubstring(s: str) -> int:
    # Edge Case
    if not s:
        return 0

    # T=O(n),S=O(n)
    hash=set()
    l=0
    maxLen=0
    for r in range(len(s)):
        while s[r] in hash:
            hash.remove(s[l])
            l+=1
        hash.add(s[r])
        maxLen=max(maxLen,len(hash))

    return maxLen


print(lengthOfLongestSubstring("pwwkew"))