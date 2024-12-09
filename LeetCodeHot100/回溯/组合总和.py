from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]#存放所有结果用于返回
        path=[]#记录单次结果的元素
        startIndex=0#表示下一层递归从哪个下标开始，为了避免排列问题导致的重复
        self.backtracking(candidates,target,result,path,startIndex)
        return result



    def backtracking(self,candidates:List[int],target:int,result:list,path:list,startIndex:int):
        if(sum(path)>target):#当前path中元素总和已经大于target，则直接抛弃
            return
        elif(sum(path)==target):#当前path中元素总和等于target，可以加入结果集result
            result.append(path[:])
            return
        for i in range(startIndex,len(candidates)):#这里从startIndex开始，代表不允许排列问题导致重复答案
            path.append(candidates[i])
            self.backtracking(candidates,target,result,path,i)#这里不用i+1代表单次结果中元素可以重复
            path.pop()





if __name__ == '__main__':
    solution=Solution()
    print(solution.combinationSum([2,3,5],8))