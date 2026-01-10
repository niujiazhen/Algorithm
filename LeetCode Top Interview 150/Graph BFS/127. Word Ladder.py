from collections import deque
from typing import List
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Edge Case
        if not beginWord or not endWord or endWord not in wordList:
            return 0

        # Preprocessing
        L=len(beginWord)# all words have same length
        allComboDict=defaultdict(list)
        # Preprocess words into generic intermediate states
        # Example: "dog" -> "*og", "d*g", "do*"
        for word in wordList:
            for j in range(L):
                genericWord=word[:j]+"*"+word[j+1:]
                allComboDict[genericWord].append(word)


        queue=deque()
        queue.append((beginWord,1))
        visited=set()
        visited.add(beginWord)

        while queue:
            curWord,steps=queue.popleft()

            if curWord==endWord:
                return steps
            # Iteratively try every possible word with only one letter different
            for i in range(L):
                intermediateWord=curWord[:i]+"*"+curWord[i+1:]
                for word in allComboDict[intermediateWord]:
                    if word not in visited:
                        queue.append((word,steps+1))
                        visited.add(word)


        return 0



if __name__ == '__main__':
    solution=Solution()
    print(solution.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))