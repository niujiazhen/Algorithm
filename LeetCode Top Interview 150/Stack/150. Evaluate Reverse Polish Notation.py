import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                num1=numStack.pop()
                num2=numStack.pop()
                numStack.append(num2+num1)
            elif tokens[i]=="-":
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num2 - num1)
            elif tokens[i]=="*":
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num2 * num1)
            elif tokens[i]=="/":
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(int(num2/num1))#use int symbol to deal with the  truncates toward zero
            else:
                numStack.append(int(tokens[i]))
        return numStack[-1]



if __name__ == '__main__':
    solution=Solution()
    print(solution.evalRPN(["4","-2","/","2","-3","-","-"]))