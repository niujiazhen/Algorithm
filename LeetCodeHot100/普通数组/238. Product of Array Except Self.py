from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    # T=O(n), S=O(1)
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    # the iteration of prefix product
    for i in range(n - 1):
        prefix[i + 1] = prefix[i] * nums[i]
    # the iteratio of suffix product
    for i in range(n - 1, 0, -1):
        suffix[i - 1] = suffix[i] * nums[i]
    ans = []
    for i in range(n):
        ans.append(prefix[i] * suffix[i])
    return ans


print(productExceptSelf([1, 2, 3, 4]))