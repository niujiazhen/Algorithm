def isValid(s: str)->bool:
    # Edge Case
    if not s:
        return True

    # T=O(n) S=O(n)
    stack=[]
    for char in s:
        # 如果是左括号，那就往stack里加入对应右括号
        if char in "([{":
            if char == "(":
                stack.append(")")
            elif char == "[":
                stack.append("]")
            else:
                stack.append("}")

        # 如果是右括号，检查是否匹配
        else:
            # 如果栈不为空且括号匹配，则pop
            if stack and stack[-1] ==char:
                stack.pop()
            else:# 不匹配或者栈为空，都不是valid
                return False
    if stack:# 如果最后还剩下未匹配的左括号，也不是valid
        return False
    return True




print(isValid("([])"))