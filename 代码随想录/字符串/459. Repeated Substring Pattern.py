class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss=s+s
        if(ss[1:len(ss)-1].find(s)!=-1):
            return True
        return False





if __name__ == '__main__':
    solution=Solution()
    print(solution.repeatedSubstringPattern("aba"))