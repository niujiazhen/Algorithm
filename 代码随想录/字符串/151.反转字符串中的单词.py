def reverseWords(s: str) -> str:
    wordList=s.split()
    n=len(wordList)
    wordList.reverse()
    # for i in range(n//2):
    #     wordList[i],wordList[n-i-1]=wordList[n-i-1],wordList[i]
    return " ".join(wordList)


print(reverseWords("a good   example"))