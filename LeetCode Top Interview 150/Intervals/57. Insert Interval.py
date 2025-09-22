from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged=[]#final output
        intervals.append(newInterval)
        for i in range(len(intervals)-1,0,-1):
            if intervals[i][0]<intervals[i-1][0]:
                intervals[i],intervals[i-1]=intervals[i-1],intervals[i]
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:#means the two elements cannot be merged:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])
        return merged





if __name__ == '__main__':
    solution=Solution()
    print(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))