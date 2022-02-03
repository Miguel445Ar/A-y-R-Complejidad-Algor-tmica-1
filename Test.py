def MatchStrings(string: str, pattern: str):
    cache = {}
    def dfs(i,j):
        if (i,j) in cache:
            return cache[(i,j)]
        if i >= len(string) and j >= len(pattern):
            return True
        if j >=  len(pattern):
            return False
        
        match = i < len(string) and (string[i] == pattern[j] or pattern[j] == ".")
        if (j + 1) < len(pattern) and pattern[j + 1] == "*":
            cache[(i,j)] = ((match and dfs(i + 1, j)) or dfs(i,j+2))
            return cache[(i,j)]
        if match:
            cache[(i,j)] = dfs(i+1,j+1)
            return cache[(i,j)]
        cache[(i,j)] = False
        return False
    return dfs(0,0)

print(MatchStrings("aba","a*ba"))