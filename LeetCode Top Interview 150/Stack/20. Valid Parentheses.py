class Solution:
    def isValid(self, s: str) -> bool:
        #T=
        stack=[]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(")")
            elif s[i]=="{":
                stack.append("}")
            elif s[i]=="[":
                stack.append("]")
            else:#
                if not stack:#if there is no item to match, False
                    return False
                elif stack.pop()!=s[i]:#match the pop item,if not match,False
                    return False
        if not stack:#only if the stack is empty means True
            return True
        return False





if __name__ == '__main__':
    solution=Solution()
    print(solution.isValid("([])"))