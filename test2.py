def coinChangeTD(coins, amount):
    cache = [None]*amount
    def _dfs(n, c):
        if n == 0:
            return 0
        tmp = []
        for coin in c:
            if coin <= n:
                tmp.append(_dfs(coins,n-coin)+1)
        return min(tmp)
    return _dfs(amount,coins)

print(coinChangeTD([1,3,4,5],7))