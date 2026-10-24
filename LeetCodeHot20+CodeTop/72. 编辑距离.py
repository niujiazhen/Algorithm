def minDistance(word1: str, word2: str)->int:
    m,n = len(word1), len(word2)

    # 定义DP[i][j]代表把word1的前i个字符串转换为word2的前j个字符串所需的最小次数
    DP=[[0]*(n+1) for _ in range(m+1)]

    # 初始化1：若word2为空字符串，则全部删除
    for i in range(m+1):
        DP[i][0]=i

    # 初始化2：若word1为空字符串，则全部插入
    for j in range(n+1):
        DP[0][j]=j

    # 遍历其余情况
    for i in range(1,m+1):
        for j in range(1,n+1):
            # 比较word1[:i]和word2[:j]的最后一个字符
            if word1[i-1] == word2[j-1]:
                # 如果相同，则可以直接转移
                DP[i][j]=DP[i-1][j-1]
            else:
                DP[i][j]=min(DP[i-1][j],# 删除：把原串前 i - 1 个字符转成目标前 j 个字符
                             DP[i][j-1],# 插入：先把原串前 i 个字符转成目标前 j - 1 个字符，再补上最后一个字符
                             DP[i-1][j-1])+1# 替换：先转换前面的字符，再把原串最后一个字符替换为目标最后一个字符

    return DP[m][n]






if __name__ == '__main__':
    print(minDistance("horse","ros"))