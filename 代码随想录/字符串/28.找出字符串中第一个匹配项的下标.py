import re


def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)
    # ansIndex=re.search(needle,haystack)
    # if(ansIndex):
    #     return ansIndex.start()
    # else:
    #     return -1







if __name__ == '__main__':
    h=input()
    n=input()
    print(strStr(h, n))