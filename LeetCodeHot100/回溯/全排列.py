from typing import List


class Solution:
    def backtracking(self, nums: List[int], result: list, used: list, path: list) -> None:
        if (len(path) == len(nums)):  # 如果出现一个排列则放入result结果集
            result.append(path[:])
            return
        # 否则遍历查找同层元素
        for i in range(len(nums)):
            if (used[i]):
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, result, used, path)
            path.pop()
            used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)  # 用来记录哪些元素用过了
        result = []  # 存放所有排列
        path = []  # 存放一个排列的答案
        self.backtracking(nums, result, used, path)
        return result


if __name__ == '__main__':
    solution=Solution()
    print(solution.permute([1, 2, 3]))