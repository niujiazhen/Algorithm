import heapq
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # We use maxHeap
        maxHeap=[]
        project=list(zip(capital,profits))
        project.sort()

        n=len(project)
        i=0

        for _ in range(k):
            while i<n and project[i][0]<=w:# current project can be added into maxHeap
                heapq.heappush(maxHeap,-project[i][1])
                i+=1
            if maxHeap:
                w-=heapq.heappop(maxHeap)
            else:
                break

        return w



if __name__ == '__main__':
    solution=Solution()
    print(solution.findMaximizedCapital(2,0,[1,2,3],[0,9,10]))