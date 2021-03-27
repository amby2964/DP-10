class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        '''
        # DP: TLE
        kn^2
        dp = [[0 for i in range(0,n+1)] for j in range(0,k+1)]
        
        for j in range(1,len(dp[0])):
            dp[1][j] = j
        
        for i in range(2, len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = float("inf")
                for f in range(1,j+1):
                    dp[i][j] = min(dp[i][j], 
                                   1 + max(dp[i-1][f-1], dp[i][j-f])) # break and not break
        
        return dp[-1][-1]
        '''
        # DP- making attempts - eggs table
        # maximum number of attempts: No of floors
        dp = [[0 for i in range(0,k+1)] for j in range(0,n+1)]
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                # 1 + Break egg(j-1, egg is broken) + not broken (j, egg is not broken)  (attempt will be reduced always)
                dp[i][j] = 1 + dp[i-1][j-1] + dp[i-1][j]
            if(dp[i][j]>=n):
                return i
            
        
        return n
