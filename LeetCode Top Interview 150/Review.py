import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # We use minHeap + Dij-like Algorithm
        minHeap=[]# to store currently possible minimum pairs
        visited=set()# to avoid duplicated pairs

        heapq.heappush(minHeap,(nums1[0]+nums2[0],0,0))# the minimum pair must be nums1[0]+nums2[0] because two lists are sorted
        visited.add((nums1[0]+nums2[0],0,0))

        ans=[]# to store the minimum k pairs
        m=len(nums1)
        n=len(nums2)

        while len(ans)<k:
            # We first get the currently minimum pair from minHeap
            currentPairSum,i,j=heapq.heappop(minHeap)
            ans.append([nums1[i],nums2[j]])

            #we append the two possible next minimum pairs
            if i+1<m and (nums1[i+1]+nums2[j],i+1,j) not in visited:
                heapq.heappush(minHeap,(nums1[i+1]+nums2[j],i+1,j))
                visited.add((nums1[i+1]+nums2[j],i+1,j))
            if j+1<n and (nums1[i]+nums2[j+1],i,j+1) not in visited:
                heapq.heappush(minHeap,(nums1[i]+nums2[j+1],i,j+1))
                visited.add((nums1[i]+nums2[j+1],i,j+1))

        return ans



if __name__ == '__main__':
    solution=Solution()
    print(solution.kSmallestPairs([1,7,11],[2,4,6],3))