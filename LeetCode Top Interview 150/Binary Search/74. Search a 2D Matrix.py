from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        nums=[]
        for i in range(row):
            for j in range(col):
                nums.append(matrix[i][j])
        l=0
        r=row*col-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                l+=1
            else:
                r-=1
        return False


if __name__ == '__main__':
    solution=Solution()
    print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))