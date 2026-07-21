from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Kahn Algorithm:use BFS to find a topological order of the graph

        #Step 1 Build adjacency list
        graph=defaultdict(list)
        in_degree=[0]*numCourses#indegree denotes the prerequisite number of course i
        for dest,src in prerequisites:
            graph[src].append(dest)#you should take src before taking dest course
            in_degree[dest]+=1# add one prerequisite to course[dest]

        #Step 2 initialize queue with course with indegree 0(means we can learn these courses without prerequisite)
        queue=deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)#record the index of courses with indegree 0

        topologigal_order_list=[]

        #Step 3 Process the algorithm starting from courses with indegree 0(learn without prerequisite)
        while queue:
            node=queue.popleft()
            topologigal_order_list.append(node)#take one course that can be learned right now

            #decrease other courses' prerequisite of course node
            for neighbor in graph[node]:
                in_degree[neighbor]-=1#cause course node has been learned
                if in_degree[neighbor]==0:#if the course has no prerequisie, means it can be learned right now
                    queue.append(neighbor)

        #Step 4 check if there is a full topological order
        if len(topologigal_order_list)==numCourses:
            return topologigal_order_list
        else:
            return []#there is a cycle in the graph









if __name__ == '__main__':
    solution=Solution()
    print(solution.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))