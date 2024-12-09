from typing import List

#单调栈(单调递减）
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result=[0]*len(temperatures)
    stack=[]
    for i in range(len(temperatures)):
        while(stack and temperatures[stack[-1]]<temperatures[i]):
            pre_index=stack.pop()
            result[pre_index]=i-pre_index
        stack.append(i)
    return result





if __name__ == '__main__':
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))