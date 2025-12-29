class Solution:
    def romanToInt(self, s: str) -> int:
        # T=O(n) S=O(1)
        dict={}
        dict["I"]=1
        dict["V"]=5
        dict["X"]=10
        dict["L"]=50
        dict["C"]=100
        dict["D"]=500
        dict["M"]=1000

        totalSum=dict[s[-1]]#to add the last number

        for i in range(len(s)-1,0,-1):
            if dict[s[i-1]]<dict[s[i]]:
                totalSum-=dict[s[i-1]]
            else:
                totalSum+=dict[s[i-1]]

        return totalSum




if __name__ == '__main__':
    solution=Solution()
    print(solution.romanToInt("MCMXCIV"))