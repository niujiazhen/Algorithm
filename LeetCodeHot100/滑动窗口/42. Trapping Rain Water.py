from typing import List

def trap(height: List[int])->int:
    # Edge Case
    if not height:
        return 0

    # 动态规划+双指针
    n=len(height)
    leftMax=[0]*n# leftMax[i]代表下标i左侧最高的墙壁，包含他自己
    rightMax=[0]*n# rightMax[i]代表下标i右侧最高的墙壁，包含他自己
    # 初始化
    leftMax[0]=height[0]
    rightMax[n-1]=height[n-1]

    # 计算leftMax
    for i in range(1,n):
        leftMax[i]=max(leftMax[i-1],height[i])# 当前下标i左侧最高要么等于前一个，要么等于他自己
    # 计算rightMax
    for i in range(n-2,-1,-1):
        rightMax[i]=max(rightMax[i+1],height[i])# 当前下标i右侧最高要么等于后一个，要么等于他自己

    sum=0
    # 计算总共的接水量：每个下标i的接水量=leftMax[i]和rightMax[i]最小值-当前高度height[i]
    for i in range(n):
        sum+=(min(leftMax[i],rightMax[i])-height[i])

    return sum


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))