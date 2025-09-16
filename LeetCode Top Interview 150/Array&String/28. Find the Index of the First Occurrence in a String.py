class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #T=O(n*m) S=O(1)
        return haystack.find(needle)

        #KMP method T=O(n+m)



if __name__ == '__main__':
    solution=Solution()
    print(solution.strStr("sadbutsad","sad"))