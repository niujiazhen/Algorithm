from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]

        def backtracking(path:List[int],result:list):
            if len(path)==len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtracking(path,result)
                    path.pop()
        backtracking(path,result)
        return result


if __name__ == '__main__':
    solution=Solution()
    print(solution.permute([1,2,3]))