from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]

        def backtracking(path:List[str],left:int, right:int):
            if len(path)==2*n:
                result.append("".join(path))
                return
            if left<n:#we first add ( to the path
                path.append("(")
                backtracking(path,left+1,right)
                path.pop()
            if right<left:#the parenthesis is valid only when the ) is smaller or equal to (
                path.append(")")
                backtracking(path,left,right+1)
                path.pop()

        backtracking([],0,0)
        return result


if __name__ == '__main__':
    solution=Solution()
    print(solution.generateParenthesis(3))