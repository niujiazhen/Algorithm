from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i=0 # track the line combination
        result=[]

        while i<len(words):
            line=self.getWords(i,maxWidth,words)
            i+=len(line)
            result.append(self.createLine(i,maxWidth,words,line))
        return result

    def getWords(self,i: int, maxWidth: int, words: List[str])->List[str]:
        currLen=0
        line=[]

        while i<len(words) and currLen+len(words[i])<=maxWidth:
            line.append(words[i])
            currLen+=len(words[i])+1# extra one space for minimum gap
            i+=1

        return line



    def createLine(self, i: int, maxWidth: int, words: List[str], line: List[str])->str:
        # Edge Case
        if i==len(words) or len(line) ==1:# if it's last line or single line -> left-justified
            s=" ".join(line)
            s+=" "*(maxWidth-len(s))
            return s

        #Basic Case
        baseLen=-1
        for word in line:
            baseLen+=len(word)+1 # normal space

        extraSpace=maxWidth-baseLen
        gaps=len(line)-1

        spacePerGap=extraSpace//gaps
        extraLeft=extraSpace%gaps

        for index in range(extraLeft):
            line[index]+=" "
        for index in range(gaps):
            line[index]+=" "*spacePerGap

        return " ".join(line)

if __name__ == '__main__':
    solution=Solution()
    print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"],16))