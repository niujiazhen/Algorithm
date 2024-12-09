from typing import List


def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    n=len(nums1)
    hash={}
    #对nums1、nums2记录哈希值
    for i in range(n):
        for j in range(n):
            if(nums1[i]+nums2[j] in hash):
                hash[nums1[i]+nums2[j]]+=1
            else:
                hash[nums1[i]+nums2[j]]=1

    ans=0
    # 对nums3、nums4记录哈希值
    for i in range(n):
        for j in range(n):
            if(-nums3[i]-nums4[j] in hash):
                ans+=hash[-nums3[i]-nums4[j]]

    return ans

if __name__ == '__main__':
    print(fourSumCount([0],[0],[0],[0]))