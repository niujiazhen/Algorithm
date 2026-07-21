from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []

        dist={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result=[]#to store the answer
        path=[]#to store valid letter combination

        def backtracking(path: list, result: list, index: int):
            if len(path) == len(digits):#means there exist a new valid letter combination
                result.append("".join(path))
                return

            possible_letters=dist[digits[index]]#the possible letter can be retrieved
            for letter in possible_letters:
                path.append(letter)
                backtracking(path,result,index+1)#then move to the next possible digit
                path.pop()#backtrack the added letter before moving on to the next

        backtracking(path, result, 0)

        return result







if __name__ == '__main__':
    solution=Solution()
    print(solution.letterCombinations("23"))