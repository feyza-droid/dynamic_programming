def fib(n):
    table_len = n+1
    table = [0 for _ in range(table_len)]
    table[1] = 1

    for i in range(table_len):
        if i+1 < table_len: table[i+1] += table[i]
        if i+2 < table_len: table[i+2] += table[i]

    return table[n]

print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(50)) # 12586269025