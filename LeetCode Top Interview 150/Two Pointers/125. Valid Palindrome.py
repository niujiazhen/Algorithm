class Solution:
    def isPalindrome(self, s: str) -> bool:
        #T=O(n), S=O(n)
        # strr=""
        # s=s.lower()
        # print(s)
        # for i in range(len(s)):
        #     if s[i]>="a" and s[i]<="z" or s[i]>="0" and s[i]<="9":
        #         strr+=s[i]
        # l=0
        # r=len(strr)-1
        # while l<r:
        #     if strr[l]!=strr[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True

        #T=O(n), S=O(1) We use two pointers to check, and do not use extra space
        i,j=0,len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():# find the first letter to be alpha or number from left
                i+=1
            while i<j and not s[j].isalnum():# find the first letter to be alpha or number from right:
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True




if __name__ == '__main__':
    solution=Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))