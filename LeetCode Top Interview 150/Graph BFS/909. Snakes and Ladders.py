from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # BFS
        n=len(board)

        #we use cell array to store the position of board labeled i
        cells=[None]*(n*n+1)
        label=1
        columns = list(range(0, n))

        #build the mapping from label(1..n**2) to (row,col)
        for row in range(n-1,-1,-1):
            for column in columns:
                cells[label]=(row,column)
                label+=1
            columns.reverse()

        #dist[i] will store the minimum steps to reach cell i from 1
        dist=[-1]*(n*n+1)
        queue=deque()
        queue.append(1)
        dist[1]=0

        while queue:
            curr=queue.popleft()
            #try moving 1~6 steps
            for next_cell in range(curr+1,min(curr+6,n*n)+1):
                row,col=cells[next_cell]
                if board[row][col]!=-1:#means there is a ladder/snake
                    destnation=board[row][col]
                else:
                    destnation=next_cell
                if dist[destnation]==-1:#the first path is the shortest path(BFS property)
                    dist[destnation]=dist[curr]+1
                    queue.append(destnation)

        return dist[n*n]







if __name__ == '__main__':
    solution=Solution()
    print(solution.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))