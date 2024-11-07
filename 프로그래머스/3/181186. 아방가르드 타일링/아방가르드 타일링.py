def solution(n):
    dp = [0, 1, 3, 10, 23, 62, 170] + [0]* (100001 - 7)
    
    for i in range(7, n+1):
        dp[i] = (dp[i-1] + dp[i-2] * 2 + dp[i-3] * 6 + dp[i-4] - dp[i-6]) % 1000000007 

    return dp[n]