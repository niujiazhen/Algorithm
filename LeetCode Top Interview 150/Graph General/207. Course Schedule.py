from typing import List


class Solution:
    def dfs(self,node,adj,visit,inStack)->bool:
        if inStack[node]:#means the node is already in the dfs path, and there is a cycle
            return True
        if visit[node]:#means the current node is already been visited and is not in the inStack, just skip it
            return False

        # Mark the node as visited and add it to the current recursion stack.
        visit[node] = True
        inStack[node] = True

        # Visit all the neighbors of the current node.
        for neighbor in adj[node]:
            # If any neighbor leads to a cycle, return True.
            if self.dfs(neighbor, adj, visit, inStack):
                return True

        # Remove the node from the recursion stack after exploring all neighbors.
        inStack[node] = False
        return False


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #we should build a graph and then check whether there is a cycle, if yes then the courses cannot be finished
        adj=[[] for _ in range(numCourses)]#build a adjacency list where adj[a] means all courses depends on course a
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        # Arrays to track visited nodes and recursion stack.
        visit = [False] * numCourses #denotes whether the node has been visited globally
        inStack = [False] * numCourses #denotes whether the node is in current dfs path(to detect the cycle)

        for i in range(numCourses):
            if self.dfs(i,adj,visit,inStack):# if a cycle is detected, its impossible to finish all courses
                return False
        return True#no cycle in the adj graph


if __name__ == '__main__':
    solution=Solution()
    print(solution.canFinish())