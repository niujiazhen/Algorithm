from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        curGain=0 # denotes the current net change
        ans=0
        for i in range(len(gas)):
            curGain+=(gas[i]-cost[i])
            if(curGain<0):# it means we cannot start at cur ansIndex, we should start over the next station
                curGain=0
                ans=i+1
        return ans





if __name__ == '__main__':
    solution=Solution()
    print(solution.canCompleteCircuit([5,8,2,8], [6,5,6,6]))
