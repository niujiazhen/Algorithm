from typing import List

def rotate(nums:List[int], k:int)->List[int]:
    # Edge Case
    if not nums:
        return []

    n=len(nums)
    k%=n

    # Basic Solution
    # T=O(n) S=O(1)
    nums[:n-k]=nums[:n-k][::-1]
    nums[n-k:n]=nums[n-k:n][::-1]
    nums[:]=nums[::-1]

print(rotate([1, 2, 3, 4, 5, 6, 7],3))