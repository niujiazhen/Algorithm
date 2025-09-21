from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #T=O(n), S=O(n）
        if k==0:
            return False
        hash=set()
        i=0
        for j in range(len(nums)):
            if len(hash)>k:
                hash.remove(nums[i])
                i+=1
            if nums[j] in hash:
                return True
            hash.add(nums[j])
        return False





if __name__ == '__main__':
    solution=Solution()
    print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))