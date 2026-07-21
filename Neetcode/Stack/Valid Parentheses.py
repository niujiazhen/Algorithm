class Solution:
    def isValid(self, s: str) -> bool:
        # Stack T=O(n)
        stack=[]
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif not stack:
                return False
            elif s[i]==")" and stack[-1]!="(":
                return False
            elif s[i]=="]" and stack[-1]!="[":
                return False
            elif s[i]=="}" and stack[-1]!="{":
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True




if __name__ == '__main__':
    solution=Solution()
    print(solution.isValid("([{}])"))