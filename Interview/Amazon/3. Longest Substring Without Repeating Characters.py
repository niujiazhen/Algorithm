class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding Window+HashSet
        #T=O(n) S=O(n)
        hash=set()#to record distinct chararcters
        l=r=0#two pointers
        maxLen=0#store the maxLen of substring
        for r in range(len(s)):
            while s[r] in hash:#we need to remove enough charracters from hashSet to add s[r] in it
                hash.remove(s[l])
                l+=1
            hash.add(s[r])
            maxLen=max(maxLen,len(hash))#calculate the maxLen
        return maxLen


if __name__ == '__main__':
    solution=Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))