from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # HashMap T=O(n), S=O(n)
        # hash={}
        # for i in range(len(numbers)):
        #     hash[numbers[i]]=i+1
        # for i in range(len(numbers)):
        #     if (target-numbers[i] in hash):
        #         return [i+1,hash[target-numbers[i]]]
        # return []

        # Two Pointer T=O(n), S=O(1)
        l, r = 0, len(numbers)-1
        while l<r:
            sum=numbers[l]+numbers[r]
            if sum==target:
                return [l+1,r+1]
            elif sum>target:
                r-=1
            else:
                l+=1
        return []






if __name__ == '__main__':
    solution=Solution()
    print(solution.twoSum([2,7,11,15],9))
