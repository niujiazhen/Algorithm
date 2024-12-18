class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip(" ")
        strList=s.split()
        return " ".join(strList[::-1])



if __name__ == '__main__':
    solution=Solution()
    print(solution.reverseWords("  a good   example  "))