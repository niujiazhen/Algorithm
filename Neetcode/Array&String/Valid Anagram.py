class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge Case
        if len(s) != len(t):
            return False

        # Use fixed length hashmap
        # T=O(m+n) S=O(1)
        hash = [0] * 26  # 26 letters in alphabet

        for i in range(len(s)):
            hash[ord(s[i]) - ord("a")] += 1

        for i in range(len(t)):
            if hash[ord(t[i]) - ord("a")] == 0:
                return False
            hash[ord(t[i]) - ord("a")] -= 1

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram("racecar", "carrace"))
