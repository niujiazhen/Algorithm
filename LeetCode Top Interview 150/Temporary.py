from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Two pointers T=O(n) S=O(1)
        l=0
        r=len(height)-1
        v=0
        while l<r:
            v=max(v,min(height[l],height[r])*(r-l))#we calculate the max volumn
            if height[l]<height[r]:#this is because the volumn depend on the shorter side, only by adjust the shorter one, we have the chance to increase the volumn
                l+=1
            else:
                r-=1
        return v

if __name__ == '__main__':
    solution=Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))