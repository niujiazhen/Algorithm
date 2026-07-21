class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #T=O(n) S=O(n)
        #Edge Case
        if numRows==1:
            return s

        strRows=[""]*numRows# represent each rows' chararcters
        index=0# denotes the index of strRows
        direction=1# indicates the direction: 1 means moving down 2 means moving up

        for char in s:
            strRows[index]+=char

            #change the direction
            if index==0:
                direction=1
            elif index==numRows-1:
                direction=-1

            #change the insert row
            index+=direction

        return "".join(strRows)





if __name__ == '__main__':
    solution=Solution()
    print(solution.convert("ABC",1))