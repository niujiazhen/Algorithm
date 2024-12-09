from typing import List


def rotate(nums: List[int], k: int) -> None:
    n=len(nums)
    k%=n
    ans_nums=[]
    for i in range(k):
        ans_nums.append(nums[n-i-1])
    ans_nums.reverse()
    for i in range(k,n):
        ans_nums.append(nums[i-k])
    # 将 ans_nums 的值复制给 nums
    nums[:] = ans_nums




if __name__ == '__main__':
    nums=[-1]
    rotate(nums,2)
    print(nums)