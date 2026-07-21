from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointers
        # T=O(n) S=O(1)
        l=0
        r=len(height)-1
        maxWater=0
        while l<r:
            maxWater=max(maxWater,(r-l)*min(height[l],height[r]))
            # only by changing the shorter side can we get more water
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxWater


if __name__ == '__main__':
    solution=Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))