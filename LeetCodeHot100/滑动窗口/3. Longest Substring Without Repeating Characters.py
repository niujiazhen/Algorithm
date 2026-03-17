class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge Case
        if not s:
            return 0

        # Basic Solution：Two Pointers
        # T=O(n) S=O(n)
        l=0
        hash=set()# record appearance of characters in current sliding window
        maxLen=0
        for r in range(len(s)):
            while s[r] in hash:# 若当前字符在set中，则从左不停清除字符，直至当前字符不在set中
                hash.remove(s[l])
                l+=1
            hash.add(s[r])
            maxLen=max(maxLen,len(hash))

        return maxLen


if __name__ == '__main__':
    solution=Solution()
    print(solution.lengthOfLongestSubstring("qrsvbspk"))
    