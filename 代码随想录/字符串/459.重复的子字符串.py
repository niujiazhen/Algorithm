def repeatedSubstringPattern(s: str) -> bool:
    doubleStr=s+s
    strList=list(doubleStr)
    finalAns=""
    for i in range(1,len(strList)-1):
        finalAns+=strList[i]

    if(finalAns.find(s)==-1):
        return False
    return True










if __name__ == '__main__':
    s=input()
    print(repeatedSubstringPattern(s))