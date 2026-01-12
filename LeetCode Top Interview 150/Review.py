from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visited=[[False]*cols for _ in range(rows)]

        def backTracking(path:List[str], x:int, y:int)->bool:
            # End Status
            if len("".join(path))==len(word):
                return True
            # False Case
            if x<0 or x>=rows or y<0 or y>=cols:
                return False# Out of boundary
            if visited[x][y]:
                return False# Already in path
            if board[x][y]!=word[len(path)]:
                return False# the letter is not what we need in current position, just skip it to reduce time complexity

            visited[x][y]=True
            path.append(board[x][y])
            res=backTracking(path,x+1,y) or backTracking(path,x-1,y) or backTracking(path,x,y+1) or backTracking(path,x,y-1)
            visited[x][y]=False
            path.pop()

            return res

        for i in range(rows):
            for j in range(cols):
                if backTracking([],i,j):
                    return True
        return False
if __name__ == '__main__':
    solution=Solution()
    print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))