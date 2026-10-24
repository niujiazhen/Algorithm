from typing import List
def rotate(matrix: List[List[int]])->None:
    # T=O(n2) S=O(1)
    n=len(matrix)

    # 先矩阵转置：沿主对角线翻转
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    # 再沿y轴翻转
    for i in range(n):
        for j in range(n//2):
            matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]

    return


matrix=[[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)