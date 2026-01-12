class Solution:
    def totalNQueens(self, n: int) -> int:
        # We use 3 set
        colSet=set()
        diagSet=set()
        antiDiagSet=set()

        def backTracking(row:int)->int:
            if row==n:# means the current queen position is valid
                return 1
            solution=0# represent the number of solution under current row

            for col in range(n):
                diag=row-col
                antiDiag=row+col

                if col in colSet or diag in diagSet or antiDiag in antiDiagSet:# not valid
                    continue

                colSet.add(col)
                diagSet.add(diag)
                antiDiagSet.add(antiDiag)

                solution+=backTracking(row+1)

                colSet.remove(col)
                diagSet.remove(diag)
                antiDiagSet.remove(antiDiag)

            return solution

        return backTracking(0)


if __name__ == '__main__':
    solution=Solution()
    print(solution.totalNQueens(4))