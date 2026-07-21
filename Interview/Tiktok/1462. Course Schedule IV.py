from typing import List
from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        def dfs(source: int, destination: int, visited: set)->bool:
            # End Status
            if source==destination:
                return True
            if source in visited:
                return False

            # iteratively traverse all neighbor of current node
            visited.add(source)
            canReach=graph[source]
            for i in range(len(canReach)):
                if dfs(canReach[i],destination,visited):
                    return True

            return False

        # Edge Case
        if not prerequisites:
            return [False]*numCourses

        # Build the graph
        graph=defaultdict(list)
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        result=[]
        for i in range(len(queries)):
            result.append(dfs(queries[i][0],queries[i][1],set()))

        return result






if __name__ == '__main__':
    solution=Solution()
    print(solution.checkIfPrerequisite(3,[[1,2],[1,0],[2,0]],[[1,0],[1,2]]))