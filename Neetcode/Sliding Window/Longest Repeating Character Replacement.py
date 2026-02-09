class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Two Pointers T=O(n),.S=O(n)
        #AAABBAABBBB k=2 -> 6
        hash={}# record letter frequency
        maxLen=0
        l=0
        maxFreq=0# record the max frequency letter in the sliding window

        for r in range(len(s)):
            hash[s[r]]=hash.get(s[r],0)+1 #record frequency
            maxFreq=max(hash.values())# this is O(1) because hash could only have 26 values

            # check if the sliding window is valid
            while (r-l+1)-maxFreq>k:
                hash[s[l]]-=1
                l+=1
                maxFreq=max(hash.values())
            maxLen=max(maxLen,r-l+1)

        return maxLen


if __name__ == '__main__':
    solution=Solution()
    print(solution.characterReplacement("XYYX",2))