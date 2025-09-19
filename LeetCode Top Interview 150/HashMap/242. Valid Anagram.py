import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #T=O(n), S=O(n)
        if len(s)!=len(t):
            return False
        hashS=collections.Counter(s)
        hashT=collections.Counter(t)
        return hashS==hashT




if __name__ == '__main__':
    solution=Solution()
    print(solution.isAnagram("anagram", "nagaram"))