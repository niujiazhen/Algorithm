from typing import List

#用时：8：23
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        result=nums[:]
        nums[:k]=result[n-k:n]
        nums[k:n]=result[:n-k]



if __name__ == '__main__':
    solution=Solution()
    nums=[1,2,3,4,5,6,7]
    solution.rotate(nums,3)
    print(nums)