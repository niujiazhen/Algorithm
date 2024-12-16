from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n=len(nums1)
        ans=0
        hash={}
        #遍历nums1+nums2的哈希值
        for i in range(n):
            for j in range(n):
                hash[nums1[i]+nums2[j]]=hash.get(nums1[i]+nums2[j],0)+1
        #遍历nums3+nums4的哈希值相反数是否在哈希表中
        for k in range(n):
            for l in range(n):
                if(-(nums3[k]+nums4[l]) in hash):
                    ans+=hash[-(nums3[k]+nums4[l])]#如果在的话，由于不考虑重复问题，ans直接添加哈希值即可
        return ans






if __name__ == '__main__':
    solution=Solution()
    print(solution.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))