# Найдите сумму цифр трехзначного числа.
# in
# 123
# out
# 6

# in
# 100
# out
# 1

n = int(input())
res = 0
while n > 0:
    res = res + n % 10
    n = n // 10

print(res)
