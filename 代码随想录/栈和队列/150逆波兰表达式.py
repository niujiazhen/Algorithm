from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack=[]
    for i in range(len(tokens)):
        if(tokens[i] in '+-*/'):
            num2=stack.pop()
            num1=stack.pop()
            if(tokens[i]=='+'):
                stack.append(num1+num2)
            elif (tokens[i] == '-'):
                stack.append(num1 - num2)
            elif (tokens[i] == '*'):
                stack.append(num1 * num2)
            else:
                result=num1/num2
                if(result<0):
                    stack.append(-int(abs(result)))
                else:
                    stack.append(num1 // num2)
        else:
            stack.append(int(tokens[i]))
    return stack[-1]


if __name__ == '__main__':
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))