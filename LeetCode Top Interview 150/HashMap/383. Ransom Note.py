import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #HashMap T=O(n), S=O(k)/O(1)
        # if len(ransomNote)>len(magazine):#check for the obvious failure
        #     return False
        # hash=[0]*26
        # for i in range(len(magazine)):
        #     hash[ord(magazine[i])-ord("a")]+=1
        # for i in range(len(ransomNote)):
        #     if hash[ord(ransomNote[i])-ord("a")]==0:
        #         return False
        #     hash[ord(ransomNote[i]) - ord("a")]-=1
        # return True

        #use Counter
        letters=collections.Counter(magazine)
        for i in range(len(ransomNote)):
            if letters[ransomNote[i]]==0:
                return False
            letters[ransomNote[i]]-=1
        return True




if __name__ == '__main__':
    solution=Solution()
    print(solution.canConstruct("a", "b"))