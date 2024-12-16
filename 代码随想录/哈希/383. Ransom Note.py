class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash={}
        #记录magazine中所有letter的出现次数（可使用次数）
        for letter in magazine:
            hash[letter]=hash.get(letter,0)+1
        #遍历ransomNote所需的所有letter
        for letter in ransomNote:
            if(hash.get(letter,0)==0):#如果ransomNote中存在hash表中没有的letter，或者可使用次数为0，直接返回False
                return False
            hash[letter]=hash.get(letter,0)-1#否则当前字母可使用次数-1
        return True





if __name__ == '__main__':
    solution=Solution()
    print(solution.canConstruct("a", "b"))