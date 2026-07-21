from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # We only need to iterate over the top-left quarter of the matrix.
        # Each iteration rotates a group of four cells.
        #
        # For rows:        0 to n//2 - 1
        # For columns:     0 to (n+1)//2 - 1
        #
        # This ensures every element is moved exactly once.
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # Save the top element
                temp = matrix[i][j]

                # Move left element to top
                # (n-1-j, i) -> (i, j)
                matrix[i][j] = matrix[n - 1 - j][i]

                # Move bottom element to left
                # (n-1-i, n-1-j) -> (n-1-j, i)
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]

                # Move right element to bottom
                # (j, n-1-i) -> (n-1-i, n-1-j)
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]

                # Move saved top element to right
                # temp -> (j, n-1-i)
                matrix[j][n - 1 - i] = temp


if __name__ == '__main__':
    solution=Solution()
    print(solution.rotate([[1,2,3],[4,5,6],[7,8,9]]))