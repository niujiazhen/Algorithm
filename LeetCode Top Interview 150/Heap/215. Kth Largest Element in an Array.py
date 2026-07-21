import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #T=O(nlogk) S=O(k)
        #We first build a min heap with size k
        heap=nums[:k]
        heapq.heapify(heap)
        #then maintain the heap with k largest element in nums list
        for i in range(k,len(nums)):
            if nums[i]>heap[0]:#means the current num is greater than the smallest element in the heap
                heapq.heappop(heap)#pop the min element of heap
                heapq.heappush(heap,nums[i])#push nums[i] in the min heap and reorganized, T=O(logk)
        return heap[0]#return the smallest element of k size min heap, which denotes the k largest element in nums


if __name__ == '__main__':
    solution=Solution()
    print(solution.findKthLargest([3,2,1,5,6,4],2))