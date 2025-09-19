class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #T=O(n), S=O(n)
        maxLen=0
        charSet=set()
        l,r=0,0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            maxLen = max(maxLen, len(charSet))
        return maxLen





if __name__ == '__main__':
    solution=Solution()
    print(solution.lengthOfLongestSubstring("qrsvbspk"))