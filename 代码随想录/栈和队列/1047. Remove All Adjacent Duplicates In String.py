class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if(stack and stack[-1]==s[i]):#如果栈内有元素且和当前s[i]相等，则出栈
                stack.pop()
            else:
                stack.append(s[i])#否则是不匹配，或者栈为空，入栈
        return "".join(stack)



if __name__ == '__main__':
    solution=Solution()
    print(solution.removeDuplicates("azxxzy"))