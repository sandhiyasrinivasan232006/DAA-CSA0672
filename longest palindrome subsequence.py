def longest_palindromic_subsequence(s):
    n = len(s)
    
    # Create a memoization table to store the length of the longest palindromic subsequence
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the table
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
    return dp, dp[0][n-1]

# Example usage:
s = "bbabcbcab"
dp_table, length_of_lps = longest_palindromic_subsequence(s)

print("Memoization Table:")
for row in dp_table:
    print(row)

print("\nLength of Longest Palindromic Subsequence:", length_of_lps)
