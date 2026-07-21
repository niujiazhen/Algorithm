class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # HashMap T=O(n), S=O(k)/O(1)
        hash={}
        for i in range(len(s)):
            if s[i] not in hash and t[i] not in hash.values():#if two char are not mapped, add it to the HashMao
                hash[s[i]]=t[i]
            elif s[i] not in hash or hash[s[i]]!=t[i]:# if t[i] is mapped to other char in s, or s[i] is mapped to other char in t, then return False
                return False
        return True




if __name__ == '__main__':
    solution=Solution()
    print(solution.isIsomorphic("paper", "title"))