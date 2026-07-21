class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two Pointers + Greedy
        maxVolumn=0
        l=0
        r=len(heights)-1
        while l<r:
            volumn=(r-l)*min(heights[l],heights[r])
            maxVolumn=max(maxVolumn,volumn)
            # when we reduce the length between l and r, the only possible way to get a higher volumn is to replace the shorter bar with a higher bar
            # and since length is reduced, we should get higher min(l,r) to get higher volumn, so we replace the shorter bar
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return maxVolumn




if __name__ == '__main__':
    solution=Solution()
    print(solution.maxArea([1,7,2,5,4,7,3,6]))