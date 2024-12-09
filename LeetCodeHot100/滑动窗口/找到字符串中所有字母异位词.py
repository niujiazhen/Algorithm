from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    result=[]
    if(len(s)<len(p)):
        return result
    hash_s=[0]*26
    hash_p=[0]*26
    for i in range(len(p)):
        hash_s[ord(s[i])-ord("a")]+=1
        hash_p[ord(p[i])-ord("a")]+=1
    if(hash_s==hash_p):
        result.append(0)
    for i in range(len(p),len(s)):
        hash_s[ord(s[i-len(p)])-ord("a")]-=1
        hash_s[ord(s[i])-ord("a")]+=1
        if(hash_s==hash_p):
            result.append(i-len(p)+1)
    return result





if __name__ == '__main__':
    print(findAnagrams("aaaaaaaaaa", "aaaaaaaaaaaaa"))