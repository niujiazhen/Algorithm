from audioop import reverse
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #使用双指针
        # n=len(s)
        # for i in range(n//2):
        #     s[i],s[n-i-1]=s[n-i-1],s[i]

        #使用reversed+切片
        s[:]=reversed(s)


if __name__ == '__main__':
    solution=Solution()
    solution.reverseString(["H","a","n","n","a","h"])