from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]>0):#如果最小数都大于0，说明不可能有新的答案了，则直接返回答案
                return ans
            if(i>0 and nums[i]==nums[i-1]):#对于元素i进行去重, 不能有重复的三元组，但三元组内的元素是可以重复的！不能写nums[i]==nums[i+1](否则会导致三元组内元素无法重复）
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):#后两个元素也不能相等
                sum=nums[i]+nums[j]+nums[k]
                if(sum<0):#若sum偏小，则元素j需要增加
                    j+=1
                elif(sum>0):#若sum偏大，则元素k需要缩小
                    k-=1
                else:#如果sum=0
                    ans.append([nums[i],nums[j],nums[k]])#添加答案
                    #对元素j去重
                    while(j<k and nums[j]==nums[j+1]):
                        j+=1
                    #对元素k去重
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1
                    j+=1
                    k-=1
        return ans






if __name__ == '__main__':
    solution=Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
