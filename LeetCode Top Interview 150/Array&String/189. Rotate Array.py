from typing import List


class Solution:
    def reverse(self,nums:List[int], start:int, end:int)->None:#to reverse the nums within index start and end
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # T=O(n) S=O(n)
        # n = len(nums)
        # k = k%len(nums)  # make sure to do the easiest rotate
        # ans=[]
        # for i in range(k):
        #     ans.append(nums[n-k+i])
        # for i in range(k,n):
        #     ans.append(nums[i-k])
        # nums[:]=ans[:]

        # T=O(n) S=O(1) using reverse
        n=len(nums)
        k%=n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)











if __name__ == '__main__':
    solution=Solution()
    nums=[1,2,3,4,5,6,7]
    print(solution.rotate(nums,3))
    print(nums)
