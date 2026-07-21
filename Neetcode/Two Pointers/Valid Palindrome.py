class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers
        # T=O(n) S=O(1)
        l=0
        r=len(s)-1

        while l<r:
            # Find the first Alphanumeric left character
            while l<len(s)-1 and not s[l].isalnum():# make sure the index is valid
                l+=1
            # Find the first Alphanumeric right character
            while r>=0 and not s[r].isalnum():# make sure the index is valid
                r-=1
            # start match
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1

        return True



if __name__ == '__main__':
    solution=Solution()
    print(solution.isPalindrome("Was it a car or a cat I saw?"))