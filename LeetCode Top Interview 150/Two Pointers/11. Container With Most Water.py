from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointers T=O(n), S=O(1)
        l,r=0,len(height)-1
        v=0
        while l<r:
            v=max(v,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return v


if __name__ == '__main__':
    solution=Solution()
    print(solution.maxArea([1,2,3,1000,9]))