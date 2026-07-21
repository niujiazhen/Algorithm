class Solution:
    def simplifyPath(self, path: str) -> str:
        #
        pathList=path.split("/")
        stack=[]# we use a stack to record the current directory
        for i in range(len(pathList)):
            if not pathList[i] or pathList[i]==".":
                continue
            elif pathList[i]=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(pathList[i])
        return "/"+"/".join(stack)

if __name__ == '__main__':
    solution=Solution()
    print(solution.simplifyPath("/../"))