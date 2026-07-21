from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build Graph
        adj=[[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        inStack=[False]*numCourses# represent which nodes are in the current path
        visited=set()

        # To find if there exists a cycle in adj
        for i in range(numCourses):
            if self.findCycle(i,inStack,visited,adj):
                return False

        return True

    def findCycle(self, index: int, instack: List[bool], visited: set, adj: List[List[int]])->bool:
        # End Status
        if instack[index]:
            return True# means there exists a cycle
        if index in visited:
            return False # means the current node is already visited and did not make a cycle, just skip it

        instack[index]=True
        visited.add(index)

        neighbors=adj[index]

        for neighbor in neighbors:
            if self.findCycle(neighbor,instack,visited,adj):
                return True

        instack[index]=False

        return False


if __name__ == '__main__':
    solution=Solution()
    print(solution.canFinish(2,[[1,0]]))