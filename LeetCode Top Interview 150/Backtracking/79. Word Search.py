from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=[[False]*len(board[0]) for i in range(len(board))]
        def dfsBacktracking(path:List[str],i:int,j:int)->bool:
            if len("".join(path))==len(word):#means the current path equal to the word
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):#means the index is out of range
                return False
            if visited[i][j]:#means the element is already in the path
                return False
            if board[i][j]!=word[len(path)]:#if the current element is not the needed letter, it's unnecessary to add it
                return False
            visited[i][j]=True
            path.append(board[i][j])
            res= (dfsBacktracking(path,i+1,j) or dfsBacktracking(path,i-1,j) or dfsBacktracking(path,i,j+1) or dfsBacktracking(path,i,j-1))
            visited[i][j]=False
            path.pop()
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfsBacktracking([],i,j):
                    return True
        return False

if __name__ == '__main__':
    solution=Solution()
    print(solution.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]],"BAAAAAAAAAAAAAA"))