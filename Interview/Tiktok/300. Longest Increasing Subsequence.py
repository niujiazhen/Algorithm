import bisect
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # T=O(n2) S=O(n)
        # We Define DP[i] as the longest strictly increasing subsequence end at index i
        # DP=[1]*len(nums)
        #
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j]<nums[i]:
        #             DP[i]=max(DP[j]+1,DP[i])
        #
        # return max(DP)

        # T=O(nlogn) S=O(n)
        # Edge Case
        if not nums:
            return 0
        # We define sub[i] as the minimum tail value of a subsequence with length i+1
        sub=[]

        for num in nums:
            # Find the index of the first element in sub that >= num
            index=bisect.bisect_left(sub,num)
            if index==len(sub):# means the num is greater than all number in sub, so we extend sub
                sub.append(num)
            else:
                # Otherwise, we replace the exsisting value to keep sub optimal (smaller tail value)
                sub[index]=num

        return len(sub)




if __name__ == '__main__':
    solution=Solution()
    print(solution.lengthOfLIS([7,7,7,7,7,7,7]))