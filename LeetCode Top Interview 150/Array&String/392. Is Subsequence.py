class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #T=O(n), S=O(1)
        i=j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:# we find a same letter
                i+=1 # then both index +1
            j+=1
        if i==len(s):#if all letters in string s are found in string t
            return True
        return False


if __name__ == '__main__':
    solution=Solution()
    print(solution.isSubsequence("b","c"))