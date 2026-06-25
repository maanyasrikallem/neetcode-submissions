class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        arr = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # length of interval
        for length in range(1, n + 1):

            # starting index
            for i in range(1, n - length + 2):

                j = i + length - 1

                # assume k is the last balloon to burst
                for k in range(i, j + 1):

                    coins = (
                        dp[i][k - 1]
                        + arr[i - 1] * arr[k] * arr[j + 1]
                        + dp[k + 1][j]
                    )

                    dp[i][j] = max(dp[i][j], coins)

        return dp[1][n]