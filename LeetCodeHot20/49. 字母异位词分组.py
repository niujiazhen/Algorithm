from typing import List
from collections import defaultdict
def groupAnagrams(strs:List[str])->List[List[str]]:
    # defaultdict T=O(nlogm) S=O(n)
    hash=defaultdict(list)# 记录每一组字母异位词
    for s in strs:
        # 计算字母异位key
        key="".join(sorted(s))
        hash[key].append(s)

    return list(hash.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# 预期输出： [["bat"],["nat","tan"],["ate","eat","tea"]]
