from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])# make sure the intervals List is sorted under the first num of each item in ascending order
        merged=[]
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:#means the two intervals cannot be merged
                merged.append(interval)
            else:
                if merged[-1][1]>=interval[1]:#means the interval is completely contained in merged[-1]
                    continue
                else:
                    merged[-1][1]=interval[1]#means the end of the interval is greater than the end of merged[-1]
        return merged





if __name__ == '__main__':
    solution=Solution()
    print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))