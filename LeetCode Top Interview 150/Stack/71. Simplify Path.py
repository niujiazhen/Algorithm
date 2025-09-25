class Solution:
    def simplifyPath(self, path: str) -> str:
        #T=O(n), S=O(n)
        stack=[]
        pathList=path.split("/")
        for i in range(len(pathList)):
            if pathList[i]=="" or pathList[i]==".":
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