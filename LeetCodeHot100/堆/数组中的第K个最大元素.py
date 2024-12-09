from typing import List
import heapq

def findKthLargest(nums: List[int], k: int) -> int:
    # 初始化小顶堆，将前K个元素插入,维护大小为K的小顶堆，则遍历后小顶堆的根节点即为第K大的元素
    heap = nums[:k]
    heapq.heapify(heap)  # 构建小顶堆
    # 遍历剩余元素
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)  # 弹出堆顶最小元素
            heapq.heappush(heap, num)  # 插入当前元素，调整堆

    # 堆顶即为第K大的元素
    return heap[0]

if __name__ == '__main__':
    print(findKthLargest([3,2,1,5,6,4],2))

