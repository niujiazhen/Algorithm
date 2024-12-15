from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #set
        # return list(set(nums1)&set(nums2))

        #hash_map
        hash={}
        for num in nums1:
            hash[num]=hash.get(num,0)+1

        ans=set()
        for num in nums2:
            if(num in hash):
                ans.add(num)

        return list(ans)








if __name__ == '__main__':
    solution=Solution()
    print(solution.intersection([4,9,5],[9,4,9,8,4]))