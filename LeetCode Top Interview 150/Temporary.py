from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):#it's impossible to travel around the circuit if sum of gas is smaller than sum of cost
            return -1
        #Otherwise, it's guaranteed to have a ans
        curGain=0#denotes the current net gas
        ans=0#denotes the starting point index
        for i in range(len(gas)):
            curGain+=(gas[i]-cost[i])#we can only start at the station i with gas >= cost
            if curGain<0:#means we don't have enought gas to go further, so we cannot start at index ans
                #Since the curGain<0 from index ans to i is negative
                #All station between [ans,i] is impossible because the station[ans] is with curGain>0
                #if we try to start at ans+1, it's even impossible because curGain at ans >0
                curGain=0
                ans=i+1
        return ans





if __name__ == '__main__':
    solution=Solution()
    print(solution.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))