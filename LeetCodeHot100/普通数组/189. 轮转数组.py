from typing import List

def rotate(nums: List[int], k: int)->None:
    # Edge Case
    if not nums:
        return []

    # 三次reverse模拟轮转 T=O(n) S=O(1)
    n=len(nums)
    k=k%n# 避免过多轮转

    nums[:n-k]=nums[:n-k][::-1]# 第一次反转前n-k个元素
    nums[n-k:n]=nums[n-k:n][::-1]# 第二次反转后k个元素
    nums.reverse()# 第三次整体反转

    return




if __name__ == '__main__':
    nums=[1,2,3,4,5,6,7]
    rotate(nums,3)
    print(nums)