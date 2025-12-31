from typing import List
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        while i < len(words):
            line = self.getWords(words, i, maxWidth)
            i += len(line)
            res.append(self.createLine(line, i, words, maxWidth))

        return res

    def getWords(self, words: List[str], i: int, maxWidth: int) -> List[str]:
        line = []
        currLen = 0

        # Pack as many words as possible
        while i < len(words) and currLen + len(words[i]) <= maxWidth:
            line.append(words[i])
            currLen += len(words[i]) + 1  # +1 prepares space for next word
            i += 1

        return line

    def createLine(self, line: List[str], i: int, words: List[str], maxWidth: int) -> str:
        # Last line or single-word line -> left justified
        if i == len(words) or len(line) == 1:
            s = " ".join(line)
            return s + " " * (maxWidth - len(s))

        # Calculate base length (mandatory spaces included)
        baseLen = -1
        for w in line:
            baseLen += len(w) + 1

        extraSpaces = maxWidth - baseLen
        gaps = len(line) - 1

        spacesPerGap = extraSpaces // gaps
        extraLeft = extraSpaces % gaps

        # Distribute spaces
        for idx in range(extraLeft):
            line[idx] += " "

        for idx in range(gaps):
            line[idx] += " " * spacesPerGap

        # Join with mandatory single space
        return " ".join(line)



if __name__ == '__main__':
    solution=Solution()
    print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))
