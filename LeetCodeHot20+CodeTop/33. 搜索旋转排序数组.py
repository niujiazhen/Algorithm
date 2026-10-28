from typing import List

def search(nums: List[int], target: int)->int:
    l,r = 0,len(nums)-1

    # T=O(logn) S=O(1)
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid

        if nums[l]<=nums[mid]:
            # 左半部分有序
            if nums[l]<=target<=nums[mid]:# target在左半部分
                r=mid-1
            else:# target在右半部分
                l=mid+1
        else:
            # 右半部分有序
            if nums[mid]<=target<=nums[r]:# target在右半部分
                l=mid+1
            else:# target在左半部分
                r=mid-1

    return -1




if __name__ == '__main__':
    print(search([4,5,6,7,0,1,2],0))