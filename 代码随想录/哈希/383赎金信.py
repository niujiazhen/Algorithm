def canConstruct(ransomNote: str, magazine: str) -> bool:
    hash=[0]*26
    for i in range(len(magazine)):
        hash[ord(magazine[i])-ord('a')]+=1
    for i in range(len(ransomNote)):
        if(hash[ord(ransomNote[i])-ord('a')]>0):
            hash[ord(ransomNote[i])-ord('a')]-=1
        else:
            return False
    return True






if __name__ == '__main__':
    print(canConstruct("baa","baba"))