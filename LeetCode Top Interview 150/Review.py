from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # Initialize a BFS queue with the starting gene and 0 mutations so far
        queue=deque()
        queue.append((start,0))
        visited=set()
        visited.add(start)

        while queue:
            # pop the current str
            node,steps=queue.popleft()
            if node==end:
                return steps
            for char in "ACGT":
                for i in range(len(node)):
                    newNode=node[:i]+char+node[i+1:]
                    if newNode not in visited and newNode in bank:
                        queue.append((newNode,steps+1))
                        visited.add(newNode)

        return -1

if __name__ == '__main__':
    solution=Solution()
    print(solution.minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]))