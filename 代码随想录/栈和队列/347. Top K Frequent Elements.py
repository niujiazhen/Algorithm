import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #哈希排序，根据hash的val值倒序排序，然后取前k个元组的第一个元素，时间复杂度O(nlogn)
        # hash={}
        # ans=[]
        # for num in nums:
        #     hash[num]=hash.get(num,0)+1
        # top_k=sorted(hash.items(),key=lambda x:x[1],reverse=True)
        # for i in range(k):
        #     ans.append(top_k[i][0])
        # return ans

        #小顶堆（优先级队列）时间复杂度O(nlogk)
        hash={}
        for num in nums:
            hash[num]=hash.get(num,0)+1
        # 构建小顶堆
        pri_que = []
        for key, freq in hash.items():
            heapq.heappush(pri_que, (freq, key))  # 根据第一个值freq频率来排序
            if (len(pri_que) > k):  # 始终只维护大小为k的优先队列，排序复杂度为logk
                heapq.heappop(pri_que)

        result = [item[1] for item in pri_que]
        result.reverse()
        return result








if __name__ == '__main__':
    solution=Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))