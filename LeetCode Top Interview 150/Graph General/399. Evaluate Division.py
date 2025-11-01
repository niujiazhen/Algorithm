from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #T=O(m*n) S=O(n) n=len of equations, m=len of queries
        graph=defaultdict(defaultdict)#the graph represented as an adjacency list   graph[a][b] = value means a / b = value

        def backtrack_evaluate(curr_node,target_node,acc_product,visited:set)->int:
            visited.add(curr_node)
            neibours=graph[curr_node]
            ret=-1.0 #we assume the answer is not found currently

            if target_node in neibours:#we find the target node, and return the ret
                ret=acc_product*neibours[target_node]
            else:
                #explore all connected neighbours recursively
                for neighbour,value in neibours.items():
                    if neighbour in visited:#the neighbour is already in the path
                        continue
                    ret = backtrack_evaluate(neighbour,target_node,acc_product*value,visited)
                    if ret!=-1.0:#means we find the path
                        break
            visited.remove(curr_node)#backtrack allow other path to use this node later
            return ret

        #Step1: build the graph from given equations and values
        for(dividend,divisor),value in zip(equations,values):#O(n)
            graph[dividend][divisor]=value
            graph[divisor][dividend]=1/value
        #Step2: answer each query using DFS search
        result=[]
        #O(m*n)
        for dividend,divisor in queries:#O(m)
            if dividend not in graph or divisor not in graph:#does not exist
                ret=-1.0
            elif dividend==divisor:#divison by itself is 1
                ret=1.0
            else:#we use dfs to search the path and calculate the value
                visited=set()
                ret=backtrack_evaluate(dividend,divisor,1,visited)#O(n)
            result.append(ret)

        return result






if __name__ == '__main__':
    solution=Solution()
    print(solution.calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))