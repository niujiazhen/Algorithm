from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #T=O(m*n) S=O(n) n=len of equations, m=len of queries
        graph=defaultdict(defaultdict)#the graph represented as an adjacency list   graph[a][b] = value means a / b = value

        def backtrack_evaluate(currentNode:str, targetNode:str, product:float, visited:set)->int:
            visited.add(currentNode)
            neighbors=graph[currentNode]
            res=-1# We assume the ans does not exist

            if targetNode in neighbors:
                res=product*neighbors[targetNode]
            else:
                #explore all neighbor recursively
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue
                    res=backtrack_evaluate(neighbor,targetNode,product*neighbors[neighbor],visited)
                    if res!=-1:
                        break# we find the path
            visited.remove(currentNode)
            return res
        #Step1: build the graph from given equations and values
        for equation,value in zip(equations,values):
            graph[equation[0]][equation[1]]=value
            graph[equation[1]][equation[0]]=1/value

        #Step2: answer each query using DFS search
        result=[]
        for (dividend,divisor) in queries:
            if dividend not in graph or divisor not in graph:
                result.append(-1)
            elif dividend==divisor:
                result.append(1)
            else:
                visited=set()
                result.append(backtrack_evaluate(dividend,divisor,1,visited))

        return result






if __name__ == '__main__':
    solution=Solution()
    print(solution.calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))