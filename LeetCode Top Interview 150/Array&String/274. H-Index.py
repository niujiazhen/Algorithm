from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Time Complexity: O(n log n) due to sorting
        # Space Complexity: O(1) (in-place sorting)

        # Step 1: Sort citations in descending order
        citations.sort(reverse=True)

        # Step 2: Iterate over sorted list
        for i in range(len(citations)):
            # If the (i+1)-th paper has fewer than (i+1) citations,
            # then h-index is i
            if citations[i] < i + 1:
                return i

        # Step 3: If all papers have at least n citations,
        # the h-index is the total number of papers
        return len(citations)


if __name__ == '__main__':
    solution=Solution()
    print(solution.hIndex([11,15]))
