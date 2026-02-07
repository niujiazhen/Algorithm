class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s# we gonna use length+delimiter# to concatenate the strList
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":# we first get the length of current word
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])# get the real word
            i=j+1+length
        return res




if __name__ == '__main__':
    solution=Solution()
