def replaceNumber(s:str)->None:
    ansStr=""
    for i in range(len(s)):
        if(s[i].isnumeric()):
            ansStr+="number"
        else:
            ansStr+=s[i]
    print(ansStr)







replaceNumber("a1b2c3")