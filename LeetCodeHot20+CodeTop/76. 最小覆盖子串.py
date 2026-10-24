from typing import Counter
def minWindow(s: str, t: str)->str:
    # Edge Case
    if not s or not t:
        return ""

    # 双指针+滑动窗口
    need=Counter(t)# 记录需要的字母
    window=Counter()# 记录当前滑动窗口里的字母
    valid=0# 记录当前滑动窗口里的有效字母数
    l=0# 滑动窗口左指针
    minLen=float("inf")# 记录最小窗口长度
    minStart=0# 记录最小窗口的左指针位置

    # 遍历右指针
    for r,char in enumerate(s):
        # 将有效字母加入window
        if char in need:
            window[char]+=1
            # 当有效字母数量足够,valid+1
            if window[char]==need[char]:
                valid+=1

        # 若当前窗口已经覆盖need，则不断尝试缩小左指针
        while valid==len(need):
            # 更新minLen
            curLen=r-l+1
            if curLen<minLen:
                minLen=curLen
                minStart=l
            # 尝试收缩左边界
            left_char=s[l]
            l+=1
            # 判断收缩后window是否还有效
            if left_char in need:
                window[left_char]-=1
                # 判断字母数量是否还够
                if window[left_char]<need[left_char]:
                    valid-=1
    if minLen==float("inf"):
        return ""
    return s[minStart:minStart+minLen]
print(minWindow("ADOBECODEBANC", "ABC"))