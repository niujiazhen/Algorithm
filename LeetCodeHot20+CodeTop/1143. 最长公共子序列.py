def longestCommonSubsequence(text1: str, text2: str)->int:
    m,n = len(text1),len(text2)

    # 定义DP[i][j]表示text1[:i]和text2[:j]的最长公共子序列
    DP = [[0]*(n+1) for _ in range(m+1)]

    # 状态转移 T=O(mn) S=O(mn)
    for i in range(1,m+1):
        for j in range(1,n+1):
            # 若text1[i-1]和text2[j-1]相等，则最长公共子序列+1
            if text1[i-1] == text2[j-1]:
                DP[i][j]=DP[i-1][j-1]+1
            else:
                # 否则DP[i][j]取DP[i-1][j]和DP[i][j-1]最大的
                DP[i][j]=max(DP[i-1][j],DP[i][j-1])

    return DP[m][n]


if __name__ == '__main__':
    print(longestCommonSubsequence("abcde","ace"))