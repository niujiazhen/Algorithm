from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Two Poiters + HashTable
        # T=O(n*m) S=O(1) n is length of s and m is length of p
        hash_s=[0]*26
        hash_p=[0]*26

        l=0
        res=[]

        # 先计算字符串p的哈希表
        for ch in p:
            hash_p[ord(ch)-ord("a")]+=1

        # 开始遍历s
        for r in range(len(s)):
            if r<len(p):# 滑动窗口长度还不够
                hash_s[ord(s[r])-ord("a")]+=1
            else:
                hash_s[ord(s[r]) - ord("a")] += 1
                hash_s[ord(s[l]) - ord("a")] -= 1
                l+=1
            if hash_p==hash_s:
                res.append(l)

        return res



if __name__ == '__main__':
    solution=Solution()
    print(solution.findAnagrams("cbaebabacd","abc"))