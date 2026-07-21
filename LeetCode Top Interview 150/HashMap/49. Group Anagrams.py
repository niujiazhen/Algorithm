from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #T=O(nklogk), S=O
        ans=[]#output
        hash={}# to record the index of a anagram group in the strs List
        for i in range(len(strs)):
            rearrange="".join(sorted(strs[i]))#O(klogk), k denotes the len of strs[i]
            if rearrange not in hash:
                hash[rearrange]=[]
            hash[rearrange].append(i)
        #iterate the hashMap to generate the answer
        for v in hash.values():
            res=[strs[i] for i in v]
            ans.append(res)
        return ans




if __name__ == '__main__':
    solution=Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))