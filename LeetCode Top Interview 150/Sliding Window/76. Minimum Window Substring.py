from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge Case
        if not s or not t:
            return ""

        # Preparation
        need=Counter(t)# The hashMap of string t
        window=Counter()# The hashMap of the current sliding window
        required=len(need)# the number of unique characters in string t
        formed=0# the number of meeted characters in sliding window
        minLen=float("inf")
        minStart=0# the startIndex of valid minWindow
        left=right=0# Two Pointers

        for right in range(len(s)):
            char=s[right]
            window[char]+=1

            # compute how many character frequency are meeted
            if char in need and need[char]==window[char]:
                formed+=1

            #When the window is valid, update the minLen and try to shrink the sliding window size
            while formed==required:
                windowLen=right-left+1
                if windowLen<minLen:
                    minLen=windowLen
                    minStart=left

                #Then we shrink the window to see if it is still valid
                left_char=s[left]
                window[left_char]-=1

                if left_char in need and window[left_char]<need[left_char]:# if the removed number is needed
                    formed-=1

                #Otherwise, the shrinked sliding window is still valid, then keep going
                left+=1

        if minLen==float("inf"):# No valid sliding window
            return ""
        return s[minStart:minStart+minLen]


if __name__ == '__main__':
    solution=Solution()
    print(solution.minWindow("ADOBECODEBANC","ABC"))