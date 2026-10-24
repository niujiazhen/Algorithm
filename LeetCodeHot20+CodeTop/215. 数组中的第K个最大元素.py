import heapq
from typing import List

def findKthLargest(nums: List[int], k: int)->int:
    # 建一个大小为K的minHeap，维护数组中前K大的元素，堆顶为当前第K大元素
    minHeap=nums[:k]
    heapq.heapify(minHeap)

    # 遍历剩下n-k个元素
    for num in nums[k:]:
        if num>minHeap[0]:#如果num大于minHeap里最小元素，则替换
            heapq.heappop(minHeap)# 弹出最小元素，并替换
            heapq.heappush(minHeap,num)

    return minHeap[0]

print(findKthLargest([3,2,1,5,6,4],2))