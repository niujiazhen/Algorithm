from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]#to record the final ans
        def backtracking(index:int,sum:int,path:List[int]):
            if sum==target:#means the num in result meets target, then add the path to result
                result.append(path[:])
                return
            if sum>target:#means it's impossible to meet the target continuing backtracking, so return
                return
            for i in range(index,len(candidates)):#we start backtracking at index because the number can be duplicated
                sum+=candidates[i]
                path.append(candidates[i])
                backtracking(i,sum,path)
                sum-=candidates[i]
                path.pop()
        backtracking(0,0,[])
        return result




if __name__ == '__main__':
    solution=Solution()
    print(solution.combinationSum([2,3,5],8))