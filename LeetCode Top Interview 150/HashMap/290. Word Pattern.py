class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #T=O(n), S=O(n)
        hash={}
        n=len(pattern)
        sList=s.split()
        if len(pattern) !=len(sList):
            return False
        for i in range(n):
            if pattern[i] not in hash and sList[i] not in hash.values():# means there is a new map to be added into the hash
                hash[pattern[i]]=sList[i]
            elif pattern[i] not in hash or hash[pattern[i]]!=sList[i]:# means sList[i] in hash.value but pattern[i] not in hash, or pattern[i] in hash but the value is not sList[i]
                return False
        return True




if __name__ == '__main__':
    solution=Solution()
    print(solution.wordPattern("aaa","aa aa aa aa"))