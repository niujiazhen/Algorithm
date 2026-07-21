from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        return self.DC(grid,0,0,len(grid))
    def DC(self,grid: List[List[int]],x:int,y:int,w:int)->Node:
        if self.allSame(grid,x,y,w):
            #if all nodes are same in current grid, create a node with isLeaf==True
            return Node(val=grid[x][y]==1,isLeaf=True)
        node=Node(isLeaf=False)#current grid is not a leafNode, then we use DC to divide it into four grids with equal size
        node.topLeft=self.DC(grid,x,y,w//2)
        node.topRight=self.DC(grid,x,y+w//2,w//2)
        node.bottomLeft=self.DC(grid,x+w//2,y,w//2)
        node.bottomRight=self.DC(grid,x+w//2,y+w//2,w//2)
        return node
    def allSame(self,grid: List[List[int]],x:int,y:int,w:int)->bool:
        #if all node in current grid are same, then return true
        for i in range(x,x+w):
            for j in range(y,y+w):
                if grid[i][j]!=grid[x][y]:
                    return False
        return True

if __name__ == '__main__':
    solution=Solution()
    print(solution.construct(
        [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]))
