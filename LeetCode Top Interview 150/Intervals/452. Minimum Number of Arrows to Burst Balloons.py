from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #T=O(nlogn), S=O(1)
        points.sort(key=lambda x:x[1])
        cur_e=points[0][1]#record the currently minimum end point
        arrows=1
        for i in range(1,len(points)):
            if points[i][0]>cur_e:#if the start point of current ballon is greater than the minimum end point, thus we need a new arrow
                arrows+=1
                cur_e=points[i][1]
            #otherwise, we can put the arrow between the start point of current ballon and the cur_e end point
        return arrows




if __name__ == '__main__':
    solution=Solution()
    print(solution.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))