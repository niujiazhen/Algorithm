class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window T=O(n) S=O(n)
        hash=set()
        l=0
        maxLen=0
        for r in range(len(s)):
            while s[r] in hash:# remove duplicated elements
                hash.remove(s[l])
                l+=1
            hash.add(s[r])
            maxLen=max(maxLen,len(hash))
        return maxLen



if __name__ == '__main__':
    solution=Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))