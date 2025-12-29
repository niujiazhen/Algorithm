from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        # We define leftMax[i] as the maximum height within [0,i]
        leftMax=[0]*n
        # We define rightMax[i] as the maximum height within [i,n-1]
        rightMax=[0]*n

        #Initialize
        leftMax[0]=height[0]
        rightMax[n-1]=height[n-1]

        # Compute leftMax
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1],height[i])
        # Compute rightMax
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],height[i])

        # Calculate the sum water volumn
        sum=0
        for i in range(n):
            sum+=min(leftMax[i],rightMax[i])-height[i]

        return sum


if __name__ == '__main__':
    solution=Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))