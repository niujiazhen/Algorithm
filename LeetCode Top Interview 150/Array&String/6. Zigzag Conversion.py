class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows=numRows
        cols=len(s)
        matrix = [["" for _ in range(cols)] for _ in range(rows)]

        i=0
        cur_x=cur_y=0
        while i<len(s):
            while i<len(s) and cur_y<rows:
                matrix[cur_y][cur_x]=s[i]
                cur_y+=1
                i+=1
            cur_x=min(cur_x+1,cols-1)
            cur_y=max(cur_y-2,0)
            while i<len(s) and cur_y>0:
                matrix[cur_y][cur_x]=s[i]
                cur_x+=1
                cur_y-=1
                i+=1
        strAns=""
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]!="":
                    strAns+=matrix[i][j]
        return strAns





if __name__ == '__main__':
    solution=Solution()
    print(solution.convert("ABC",1))