from typing import List


def longestConsecutive(nums: List[int]) -> int:
    # #时间复杂度O(nlogn)
    # nums.sort()
    # hash={}
    # for i in range(len(nums)):
    #     hash[nums[i]]=1
    # last_key=None
    # if(len(nums)==0):
    #     pLen=0
    # else:
    #     pLen=1
    # maxLen=0
    # for key in hash:
    #     if(last_key==None):
    #         last_key=key
    #     else:
    #         if(key-last_key==1):
    #             pLen+=1
    #         else:
    #             maxLen=max(maxLen,pLen)
    #             pLen=1
    #         last_key = key
    # maxLen=max(maxLen,pLen)
    # return maxLen


    #时间复杂度o(n)
    maxLen=0
    pLen=0
    set1=set(nums)
    for num in set1:
        if(num-1 not in set1):#只有当前num是某个连续序列的开头第一个数的时候才会进入内存村换，所以例子中只有-1和3会进入，内存循环遍历的是外层循环跳过的，所以总时间复杂度为O（n）
            current_num=num
            pLen=1
            while(current_num+1 in set1):
                current_num+=1
                pLen+=1
            maxLen=max(maxLen,pLen)
    return maxLen









if __name__ == '__main__':
    print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))