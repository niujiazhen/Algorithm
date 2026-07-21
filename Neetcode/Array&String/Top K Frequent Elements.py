from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force T=O(nlogn) S=O(n)
        # hash={}# record the frequency of each element in nums
        # for num in nums:
        #     hash[num]=hash.get(num,0)+1
        #
        # arr=[]# to record the [freq,num] pair
        # for num,freq in hash.items():
        #     arr.append([freq,num])# we put frequency in front in order to sort it by freq
        #
        # arr.sort(reverse=True)
        #
        # res=[]
        # for i in range(k):
        #     res.append(arr[i][1])
        #
        # return res

        # Bucket sort
        hash = {}  # record the frequency of each element in nums
        for num in nums:
            hash[num] = hash.get(num, 0) + 1

        freq=[[] for _ in range(len(nums)+1)]# freq[i] represents all elements that appear i times in nums
        for num,cnt in hash.items():
            freq[cnt].append(num)

        # get top k frequent elements
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return None


if __name__ == '__main__':
    solution=Solution()
    print(solution.topKFrequent([1,2,2,3,3,3],2))