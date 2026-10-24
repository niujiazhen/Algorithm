from typing import List

def generateParanthesis(n: int)->List[str]:
    # 记录最后答案
    result=[]

    def backTracking(path: List[str], left: int, right: int)->None:# left代表使用(的次数，right代表使用)的次数
        # 退出条件：path长度足够
        if len(path)==2*n:
            result.append("".join(path))
            return

        # 如果left没用完，可以先添加左括号
        if left<n:
            path.append("(")
            backTracking(path,left+1,right)
            path.pop()
        # 如果right比left小，则还可以加右括号
        if right<left:
            path.append(")")
            backTracking(path,left,right+1)
            path.pop()

    backTracking([],0,0)
    return result



if __name__ == '__main__':
    print(generateParanthesis(3))