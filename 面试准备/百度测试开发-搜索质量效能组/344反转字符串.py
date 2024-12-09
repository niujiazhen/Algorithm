from typing import List

##用时3：16
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # return s.reverse()
        n=len(s)
        for i in range(len(s)//2):
            s[i],s[n-i-1]=s[n-i-1],s[i]









if __name__ == '__main__':
    solution=Solution()
    s=["h","e","l","l","o"]
    solution.reverseString(s)
    print(s)