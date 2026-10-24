from typing import List

def minPathSum(grid: List[List[int]])->int:
    # Edge Case
    if not grid:
        return 0

    m,n = len(grid),len(grid[0])

    # 定义DP[i][j]代表从左上角走到grid[i][j]所需的最小步数
    DP=[[0]*n for _ in range(m)]

    # 初始化行
    for i in range(m):
        DP[i][0]=DP[i-1][0]+grid[i][0]# 只能走边界
    # 初始化列
    for j in range(n):
        DP[0][j]=DP[0][j-1]+grid[0][j]# 只能走边界

    # 状态转移方程
    for i in range(1,m):
        for j in range(1,n):
            DP[i][j]=min(DP[i-1][j],DP[i][j-1])+grid[i][j]

    return DP[m-1][n-1]

if __name__ == '__main__':
    print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))