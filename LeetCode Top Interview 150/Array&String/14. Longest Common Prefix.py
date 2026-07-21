from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix) !=0: #means the strs[i] and prefix don't have a common prefix
                prefix=prefix[:len(prefix)-1]# remove the last letter or prefix
        return prefix




if __name__ == '__main__':
    solution=Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))