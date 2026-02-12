class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Two Pointers T=O(n),S=O(n)
        #AAABBAABBBB k=2 -> 8
        hash={}# record frequency
        maxf=0
        maxLen=0

        l=0
        for r in range(len(s)):
            hash[s[r]]=hash.get(s[r],0)+1
            maxf=max(hash.values())# replace characters that are not the max frequency O(1) because hash is up to 26 letters

            if (r-l+1)-maxf>k:
                hash[s[l]]-=1
                l+=1
                maxf=max(hash.values())
            maxLen=max(maxLen,r-l+1)

        return maxLen




if __name__ == '__main__':
    solution=Solution()
    print(solution.characterReplacement("AAABBAABBBB",2))