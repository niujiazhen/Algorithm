def lengthOfLongestSubString(s:str)->int:
    # Edge Case
    if not s:
        return 0

    # 双指针+Set实现
    # T=O(n), S=O(n)
    hash=set()
    l=0# l指针记录从左往右起第一个在set中的元素
    maxLen=0
    for r in range(len(s)):# 遍历r指针
        while s[r] in hash:# 若当前元素在set中，则不停删除最左侧的元素直至r元素加入
            hash.remove(s[l])
            l+=1
        hash.add(s[r])
        maxLen=max(maxLen,len(hash))

    return maxLen



print(lengthOfLongestSubString("abcabcbb"))