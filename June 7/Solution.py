class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways=[0 for i in range(0,amount+1)]
        ways[0]=1
        for i in range(0,len(coins)):
            for j in range(coins[i],amount+1):
                ways[j]+=ways[j-coins[i]]
        return ways[amount]