from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=j=0
        nums1_copy=nums1[:m]
        for _ in range(m+n):
            if j==n or (i<m and nums1_copy[i]<=nums2[j]):
                nums1[i+j]=nums1_copy[i]
                i+=1
            else:
                nums1[i+j]=nums2[j]
                j+=1

        return nums1






if __name__ == '__main__':
    solution=Solution()
    print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
