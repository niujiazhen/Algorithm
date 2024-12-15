class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        hash=[0]*26
        for i in range(len(s)):
            hash[ord(s[i])-ord("a")]+=1
            hash[ord(t[i])-ord("a")]-=1
        for i in range(len(hash)):
            if(hash[i]!=0):
                return False
        return True









if __name__ == '__main__':
    solution=Solution()
    print(solution.isAnagram("rat", "car"))