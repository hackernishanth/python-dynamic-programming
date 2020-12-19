
def grid(m,n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return  0
    return grid(m-1, n) + grid(m, n-1)

print(grid(2,2)) # 2
print(grid(3,5)) # 15
print(grid(4,5)) # 35
print(grid(3,3)) # 6
print(grid(18,18)) # 2333606220

#------------------------------Dynamic programming--------------------------------

def grid(m, n, memo = {}):
    check = '{},{}'.format(m,n)
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return  0
    if check in memo: return memo[check]
    memo[check] = grid(m-1, n, memo) + grid(m, n-1, memo)
    return memo[check]

print(grid(2,2)) # 2
print(grid(3,5)) # 15
print(grid(4,5)) # 35
print(grid(3,3)) # 6
print(grid(18,18)) # 2333606220
