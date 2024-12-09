from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    #哈希排序O(nlogn)
    # hash={}
    # for i in range(len(nums)):
    #     hash[nums[i]]=hash.get(nums[i],0)+1
    # ans=sorted(hash.items(),key=lambda item:item[1],reverse=True)
    # result=[item[0] for item in ans]
    # return result[0:k]

    #优先级队列实现小顶堆O(nlogk)
    hash={}
    for i in range(len(nums)):
        hash[nums[i]]=hash.get(nums[i],0)+1

    #构建小顶堆
    pri_que=[]
    for key,freq in hash.items():
        heapq.heappush(pri_que,(freq,key))#根据第一个值freq频率来排序
        if(len(pri_que)>k):#始终只维护大小为k的优先队列，排序复杂度为logk
            heapq.heappop(pri_que)#推出最小堆顶freq最低的元素

    result=[item[1] for item in pri_que]
    result.reverse()
    return result




if __name__ == '__main__':
    print(topKFrequent([1,1,1,2,2,3],2))