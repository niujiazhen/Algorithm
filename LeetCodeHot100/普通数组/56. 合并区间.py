from typing import List

def merge(intervals: List[List[int]])->List[List[int]]:
    # 首先intervals按照第一个元素顺序排序，保证比较interval是否能合并的时候，开头是顺序的
    intervals.sort(key=lambda x: x[0])
    merged=[]

    for i in range(len(intervals)):
        # 如果第一次遍历或当前区间无法合并，直接添加
        if not merged or merged[-1][1]<intervals[i][0]:
            merged.append(intervals[i])
        # 否则合并，区间结尾为两个interval结尾最大的
        else:
            merged[-1][1]=max(merged[-1][1],intervals[i][1])

    return merged

if __name__ == '__main__':
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))