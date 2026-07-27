from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str])->List[List[str]]:
    hash=defaultdict(list)# 新建一个字典列表
    for s in strs:
        # 计算key
        key="".join(sorted(s))
        hash[key].append(s)

    return list(hash.values())

if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))