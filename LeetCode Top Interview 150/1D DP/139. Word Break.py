from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #We use DP and Memorization
        memo=[None]*(len(s))#memo[i] records the status of dp[i] to avoid stackoverflow

        def dp(i:int)->bool:#dp(i) denotes whether s[0:i] is valid to build by wordDict
            #empty string is always valid to build
            if i<0:
                return True
            #if dp(i) is already calculated, just return the memorization
            if memo[i] is not None:
                return memo[i]

            #Otherwise, we start calculated dp(i)
            #We start trying every word in wordDict
            for word in wordDict:
                LEN=len(word)
                if i-LEN+1>=0:#check if the word can end at index i (not longer than dp(i))
                    if s[i-LEN+1:i+1]==word:#check if the substring matches word
                        if dp(i-LEN):#check if the prefix is valid
                            memo[i]=True
                            return True
            memo[i]=False
            return False

        return dp(len(s)-1)





if __name__ == '__main__':
    solution=Solution()
    print(solution.wordBreak("leetcode",["leet","code"]))