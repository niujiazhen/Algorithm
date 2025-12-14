import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #We use MinHeap and Dij-like algorithm

        #Edge Case
        if not nums1 or not nums2 or k==0:
            return []

        m,n=len(nums1),len(nums2)
        minHeap=[]#to store the candidate pairs
        visited=set()#to avoid duplicate candidate pairs
        heapq.heappush(minHeap,(nums1[0]+nums2[0],0,0))#the smallest pair must be nums1[0]+nums2[0] because two array are sorted
        visited.add((0,0))

        ans=[]

        while minHeap and len(ans)<k:
            curSmallestSum,i,j=heapq.heappop(minHeap)#get the currently smallest pair
            ans.append([nums1[i],nums2[j]])

            #expand the candidate pair from nums1
            if i+1<m and (i+1,j) not in visited:
                heapq.heappush(minHeap,(nums1[i+1]+nums2[j],i+1,j))
                visited.add((i+1,j))

            #expand the candidate pair from nums2
            if j+1<n and (i,j+1) not in visited:
                heapq.heappush(minHeap,(nums1[i]+nums2[j+1],i,j+1))
                visited.add((i,j+1))

        return ans



if __name__ == '__main__':
    solution=Solution()
    print(solution.kSmallestPairs([-10,-4,0,0,6],[3,5,6,7,8,100],10))