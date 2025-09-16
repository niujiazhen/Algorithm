class Solution:
    def intToRoman(self, num: int) -> str:
        dict={}
        dict["1"]="I"
        dict["5"]="V"
        dict["10"]="X"
        dict["50"]="L"
        dict["100"]="C"
        dict["500"]="D"
        dict["1000"]="M"
        dict["4"]="IV"
        dict["40"]="XL"
        dict["400"]="CD"
        dict["9"]="IX"
        dict["90"]="XC"
        dict["900"]="CM"
        ans=[]
        base=1
        while num>0:
            cur=num%10 #denotes the current number
            strr=""
            if cur==4:
                strr=dict[str(cur*base)]
            elif cur==9:
                strr = dict[str(cur * base)]
            else:
                if cur >= 5:
                    strr += dict[str(5 * base)]
                    cur-=5
                strr += cur * dict[str(base)]

            ans.append(strr)
            base*=10
            num//=10
        ans.reverse()
        return "".join(ans)


if __name__ == '__main__':
    solution=Solution()
    print(solution.intToRoman(3749))