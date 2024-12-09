from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)

        #先沿主对角线翻转
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #再沿着y轴翻转
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]










if __name__ == '__main__':
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    solution=Solution()
    solution.rotate(matrix)
    print(matrix)