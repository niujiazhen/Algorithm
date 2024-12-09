from typing import List


def reverseString( s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n=len(s)
    for i in range(n//2):
        s[i],s[n-i-1]=s[n-i-1],s[i]
    print(s)


reverseString(list("hello"))
