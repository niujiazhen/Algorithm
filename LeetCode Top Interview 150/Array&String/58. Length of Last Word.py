class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        parts=s.split()
        print(parts)
        return len(parts[-1])




if __name__ == '__main__':
    solution=Solution()
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))