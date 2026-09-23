def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n], dp
def build_lcs(X, Y, dp):
    i = len(X)
    j = len(Y)
    result = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    result.reverse()
    return "".join(result) if isinstance(X, str) else result
X = "NILESH"
Y = "RANE"
length, dp_table = lcs_length(X, Y)
lcs_str = build_lcs(X, Y, dp_table)
print(f"LCS Length: {length}") 
print(f"LCS Sequence: {lcs_str}") 