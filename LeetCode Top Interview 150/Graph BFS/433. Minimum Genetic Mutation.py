from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # Initialize a BFS queue with the starting gene and 0 mutations so far
        queue = deque([(start, 0)])

        # Keep track of all visited genes to avoid revisiting
        seen = {start}

        # Perform BFS
        while queue:
            node, steps = queue.popleft()  # Get the current gene and the number of mutations

            # If we have reached the target gene, return the number of steps (minimum mutations)
            if node == end:
                return steps

            # Try changing each position in the gene to one of the four possible characters
            for c in "ACGT":
                for i in range(len(node)):
                    # Generate a new possible gene by mutating one position
                    neighbor = node[:i] + c + node[i + 1:]

                    # Check if the new gene is valid and hasn't been visited yet
                    if neighbor not in seen and neighbor in bank:
                        # Add it to the BFS queue with one more mutation
                        queue.append((neighbor, steps + 1))
                        # Mark it as visited
                        seen.add(neighbor)

        # If BFS finishes without finding the end gene, it's unreachable
        return -1


if __name__ == '__main__':
    solution=Solution()
    print(solution.minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]))