from email.policy import default
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Edge Case
        if not strs:
            return [[]]

        # T=O(m*n) n is the length of strs and m is length of longest str
        # S=O(n)
        res=defaultdict(list)# map letter frequency ——> word

        for s in strs:
            freq=[0]*26# O(1)
            for i in range(len(s)):
                freq[ord(s[i])-ord("a")]+=1
            res[tuple(freq)].append(s) # we change list to tuple because list cannot be a key in python

        return list(res.values())
if __name__ == '__main__':
    solution=Solution()
    print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))