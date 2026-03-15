from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T=O(n*mlogm) S=O(n): m is the longest length of string in strs
        hash=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            hash[key].append(s)

        return list(hash.values())


if __name__ == '__main__':
    solution=Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))