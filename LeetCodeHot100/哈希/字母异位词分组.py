import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # hash1={}
    # for i in range(len(strs)):
    #     sorted_str=''.join(sorted(strs[i]))
    #     if(sorted_str in hash1):
    #         hash1[sorted_str].append(str(i))
    #     else:
    #         hash1[sorted_str] = [str(i)]
    # result=[]
    # for value in hash1.values():
    #     partial_result=[]
    #     for i in range(len(value)):
    #         partial_result.append(strs[int(value[i])])
    #     result.append(partial_result)
    # return result

    mp=collections.defaultdict(list)

    for i in range(len(strs)):
        key="".join(sorted(strs[i]))
        mp[key].append(strs[i])
    return list(mp.values())









if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat","ac","bd","aac","bbd","aacc","bbdd","acc","bdd"]))