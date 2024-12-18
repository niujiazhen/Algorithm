class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            j=0
            while(i+j<len(haystack) and haystack[i+j]==needle[j]):
                j+=1
                if(j==len(needle)):
                    return i
        return -1

        #直接用find函数
        # return haystack.find(needle)





if __name__ == '__main__':
    solution=Solution()
    print(solution.strStr("aaaaaa", "aaaa"))