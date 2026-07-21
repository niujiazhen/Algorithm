class Solution:
    def calculate(self, s: str) -> int:
        stack=[]# to store expressions
        power=0
        operand=0

        # Traverse the string from right to left
        for i in range(len(s)-1,-1,-1):
            ch=s[i]

            if ch.isdigit():
                # Build number in reverse order (e.g. "123" -> 3 + 20 + 100), because we first meet 3 in reverse order, so we cannot do like operand*10+int(ch)
                operand=(10**power*int(ch))+operand
                power+=1
            elif ch!=" ":
                # Push the operand into stack when encountering non digit
                if power>0:# representing a digit
                    stack.append(operand)
                    power=0
                    operand=0
                if ch=="(":# start evaluate the expression in the parenthese
                    res=self.evaluate_expr(stack)
                    stack.pop()# to remove the ")"
                    stack.append(res)
                else:
                    stack.append(ch)# push ")" or operators

        # Push the last operand if exists
        if power:
            stack.append(operand)

        # Evaluate any remaining expression in the stack
        return self.evaluate_expr(stack)

    def evaluate_expr(self, stack:[])->int:
        # Handle Cases like -1, (+2)
        # if stack is empty or ends with a operator, prepend 0 to calculate
        if not stack or type(stack[-1])==str:
            stack.append(0)

        #Initialize with first number
        res=stack.pop()
        while stack and stack[-1]!=")":
            sign=stack.pop()
            if sign=="+":
                res+=stack.pop()
            else:
                res-=stack.pop()

        return res

if __name__ == '__main__':
    solution=Solution()
    print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))