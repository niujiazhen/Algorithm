from typing import List


def maxArea(height: List[int])-> int:
    # Edge Case
    if not height:
        return 0
    # 双指针 T=O(n)
    l=0
    r=len(height)-1
    maxVolume=0
    while l<r:
        curVolume=(r-l)*min(height[l],height[r])
        maxVolume=max(maxVolume,curVolume)
        # 贪心策略：由于高度取决于两侧最低，所以在收拢边界的情况下，只有移动低的那根边界，才有可能获得更大Volume
        if height[l]<height[r]:
            l+=1
        else:
            r-=1

    return maxVolume



if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))