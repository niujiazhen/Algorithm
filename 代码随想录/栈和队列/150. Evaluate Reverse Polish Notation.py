from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for item in tokens:
            if(item=="+"):
                num1=stack.pop()
                num2=stack.pop()
                stack.append(num2+num1)
            elif(item=="-"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
            elif(item=="*"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2*num1)
            elif(item=="/"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))
            else:
                stack.append(int(item))
        return int(stack.pop())





if __name__ == '__main__':
    solution=Solution()
    print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))