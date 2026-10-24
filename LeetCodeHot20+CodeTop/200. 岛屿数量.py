from typing import List
def numIsland(grid: List[List[str]])->int:
    # Edge Case
    if not grid:
        return 0

    sum=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="1":# 发现一块新大陆
                dfs(grid,i,j)# 每当发现一块新大陆，dfs遍历周围所有邻接大陆，全部计算到一块大陆中
                sum+=1

    return sum


def dfs(grid: List[List[str]], x: int, y: int)->None:
    # 越界
    if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
        return
    # 已经访问过
    if grid[x][y]=="0":
        return
    grid[x][y]="0"
    dfs(grid,x+1,y)
    dfs(grid,x,y+1)
    dfs(grid,x-1,y)
    dfs(grid,x,y-1)



print(numIsland([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
