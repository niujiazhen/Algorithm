from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #T=O(S),S is the sum length of all strs in the list
        commonPrefix=strs[0]
        for i in range(1,len(strs)):
            commonPrefix=commonPrefix[:min(len(commonPrefix),len(strs[i]))]
            for j in range(min(len(commonPrefix),len(strs[i]))):
                if commonPrefix[j]!=strs[i][j]:
                    commonPrefix=commonPrefix[:j]
                    break
        return commonPrefix




if __name__ == '__main__':
    solution=Solution()
    print(solution.longestCommonPrefix(["ab", "a"]))