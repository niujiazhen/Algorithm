from typing import List

def merge(intervals:List[List[int]])->List[List[int]]:
    # T=O(n)
    intervals.sort(key=lambda x: x[0])
    i=0
    while i<len(intervals)-1:# 一直合并到倒数第二个
        if intervals[i][1]>=intervals[i+1][0]:# 前一个interval的end值覆盖了后一个interval的start，可以合并
            intervals[i][1]=max(intervals[i+1][1],intervals[i][1])# 合并操作
            intervals.remove(intervals[i+1])#去除被合并的
        else:# 无法合并，当前interval已独立，遍历下一个
            i+=1
    return intervals

print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
