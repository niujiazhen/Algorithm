from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        index=1
        curLen=len(nums)-1
        start_x=start_y=0
        while(index<len(nums)**2):
            #right
            for j in range(start_y,start_y+curLen):
                nums[start_x][j]=index
                index+=1
            start_y+=curLen
            #down
            for i in range(start_x,start_x+curLen):
                nums[i][start_y]=index
                index+=1
            start_x+=curLen
            #left
            for j in range(start_y,start_y-curLen,-1):
                nums[start_x][j] = index
                index+=1
            start_y-=curLen
            #up
            for i in range(start_x,start_x-curLen,-1):
                nums[i][start_y]=index
                index+=1
            start_x-=curLen
            start_x+=1
            start_y+=1
            curLen-=2

        if(n%2==1):
            nums[start_x][start_y]=index
        return nums




if __name__ == '__main__':
    solution=Solution()
    print(solution.generateMatrix(5))