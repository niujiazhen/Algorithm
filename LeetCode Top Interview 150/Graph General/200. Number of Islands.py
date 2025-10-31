from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #we use dfs T=O(m*n) S=O(m*n)
        if not grid:#edge case
            return 0

        islandNum=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":#means the current element is an unvisited island
                    self.dfs(grid,i,j)
                    islandNum+=1
        return islandNum

    def dfs(self,grid,x,y):
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):#the current coordinate is invalid
            return
        if grid[x][y]=="0":#the current element is water or is a visited island
            return
        grid[x][y]="0"
        self.dfs(grid,x+1,y)
        self.dfs(grid,x,y+1)
        self.dfs(grid,x-1,y)
        self.dfs(grid,x,y-1)




if __name__ == '__main__':
    solution=Solution()
    print(solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))