class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Preparation
        need=Counter(t)# t frequency
        window=Counter()# character frequency in the sliding window
        required=len(need)# required characters in word t
        formed=0# formed character in sliding window
        minLen=float("inf")
        minStart=0# the start index of minLen sliding window
        l=0# left point used to shrink the sliding window when it's valid

        for r in range(len(s)):
            window[s[r]]+=1
            char=s[r]

            # calculate how many characters in need are meeted
            if char in need and window[char]==need[char]:
                formed+=1

            # when all characaters are meeted, try shrinking the left pointer until it's not valid
            while formed==required:
                windowSize=r-l+1
                if windowSize<minLen:
                    minLen=windowSize
                    minStart=l
                # Then we try to shrink the sliding window
                leftChar=s[l]
                l+=1
                window[leftChar]-=1

                # check if removing leftmost character will reduce formed character
                if leftChar in need and window[leftChar]<need[leftChar]:
                    formed-=1

        if minLen==float("inf"):
            return ""
        return s[minStart:minStart+minLen]