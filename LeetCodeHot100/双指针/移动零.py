from typing import List


def moveZeroes(nums: List[int]) -> None:
    l=r=0
    while(r<len(nums)):
        if(nums[r]!=0):
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
        r+=1


if __name__ == '__main__':
    nums=[0,1,0,3,12]#1,3,12,0,0
    moveZeroes(nums)
    print(nums)


    #0,1,0,3,12