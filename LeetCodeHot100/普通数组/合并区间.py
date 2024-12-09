from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals=sorted(intervals,key=lambda x:x[0])
    i=0
    while(i<len(intervals)-1):
        if(intervals[i][1]>=intervals[i+1][0]):
            intervals[i][1]=max(intervals[i+1][1],intervals[i][1])
            intervals.remove(intervals[i+1])
        else:
            i+=1
    return intervals


if __name__ == '__main__':
    print(merge([[1,4],[4,5]]))