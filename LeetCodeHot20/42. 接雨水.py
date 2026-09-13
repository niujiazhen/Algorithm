from typing import List
def trap(height: List[int]) -> int:
    # Edge Case
    if not height:
        return 0

    # 双指针+DP
    # T=O(n) S=O(n)
    n=len(height)
    leftMax=[0]*n# 记录i左侧最高的墙，包括他自己
    rightMax=[0]*n# 记录i右侧最高的墙，包括他自己

    # 初始化leftMax
    leftMax[0]=height[0]
    for i in range(1,n):
        leftMax[i]=max(leftMax[i-1],height[i])
    # 初始化rightMax
    rightMax[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        rightMax[i]=max(rightMax[i+1],height[i])

    sum=0
    for i in range(n):
        sum+=(min(leftMax[i],rightMax[i])-height[i])

    return sum

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))