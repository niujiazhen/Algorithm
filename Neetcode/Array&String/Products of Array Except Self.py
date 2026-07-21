from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n# prefix[i] represents product of elements before i
        suffix=[1]*n# suffix[i[ represents product of elements after i
        res=[0]*n


        for i in range(1,n):
            prefix[i]=nums[i-1]*prefix[i-1]
        for i in range(n-2,-1,-1):
            suffix[i]=nums[i+1]*suffix[i+1]

        for i in range(n):
            res[i]=prefix[i]*suffix[i]

        return res





if __name__ == '__main__':
    solution=Solution()
    print(solution.productExceptSelf([1,2,4,6]))