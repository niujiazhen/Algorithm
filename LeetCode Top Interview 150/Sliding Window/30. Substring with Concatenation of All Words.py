from typing import List
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Edge Case
        if not s or not words:
            return []

        # Preperation
        n=len(s)
        k=len(words)
        wordLen=len(words[0])# equal len
        subStringSize=wordLen*k
        wordCount=Counter(words)# HashMap of words
        ans=[]

        def check(i: int)->bool:
            wordVisited=wordCount.copy()
            wordUsed=0# records how many words are used

            for j in range(i,i+subStringSize,wordLen):
                subString=s[j:j+wordLen]
                if subString not in wordVisited or wordVisited[subString]==0:# means the subString is not valid
                    return False
                wordVisited[subString]-=1
                wordUsed+=1

            #Check if all word in words are used
            if wordUsed==k:
                return True
            return False

        for i in range(n-subStringSize+1):
            if check(i):
                ans.append(i)

        return ans




if __name__ == '__main__':
    solution=Solution()
    print(solution.findSubstring("barfoothefoobarman",["foo","bar"]))