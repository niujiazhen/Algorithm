from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # T=O(m+n) S=O(m+n)
        num=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                num.append(nums1[i])
                i+=1
            else:
                num.append(nums2[j])
                j+=1
        if i<len(nums1):
            for x in range(i,len(nums1)):
                num.append(nums1[x])
        else:
            for x in range(j,len(nums2)):
                num.append(nums2[x])

        n=len(num)
        if n%2==1:
            return num[n//2]
        else:
            return (num[n//2-1]+num[n//2])/2


if __name__ == '__main__':
    solution=Solution()
    print(solution.findMedianSortedArrays([1,3],[2]))