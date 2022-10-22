def gridTraveler(m, n, memo = {}):
    key1 = str(m) + "," + str(n)
    # key2 = str(n) + "," + str(m) # since gridTraveler(a,b) equals to gridTraveler(b,a) for this problem
    if (key1 in memo): return memo[key1]
    # if (key2 in memo): return memo[key2]
    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0
    memo[key1] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)

    return memo[key1]

w = gridTraveler(18, 18)
print(f"w {w}")