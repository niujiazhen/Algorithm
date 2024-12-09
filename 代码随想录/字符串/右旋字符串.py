def rightRotationStr(s:str,k:int)->str:
    ansStr=""
    n=len(s)
    for i in range(n-k,n):
        ansStr+=s[i]
    for i in range(n-k):
        ansStr+=s[i]

    return ansStr







if __name__ == "__main__":
    k=int(input())
    s = input()
    print(rightRotationStr(s, k))
