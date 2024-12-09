from typing import List


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result=[]#结果集
#         path=[]#单个答案结果
#         startIndex=0#避免排列重复
#         self.backtracking(nums,result,path,startIndex)
#         return result
#
#
#
#     def backtracking(self,nums:List[int],result:list,path:list,startIndex:int)->None:
#         result.append(path[:])
#         # if(startIndex>=len(nums)):#递归终止条件，可以不加
#         #     return
#         for i in range(startIndex,len(nums)):
#             path.append(nums[i])
#             self.backtracking(nums,result,path,i+1)
#             path.pop()



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        startIndex=0
        self.backtracking(nums,result,path,startIndex)
        return result





    def backtracking(self,nums,result,path,startIndex)->None:
        result.append(path[:])

        for i in range(startIndex,len(nums)):
            path.append(nums[i])
            self.backtracking(nums,result,path,i+1)
            path.remove(nums[i])






if __name__ == '__main__':
    solution=Solution()
    print(solution.subsets([1,2,3]))