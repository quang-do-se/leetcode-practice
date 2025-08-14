
# Online Python - IDE, Editor, Compiler, Interpreter

def pow(base, exp):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res *= base

        base *= base

        exp //= 2
    return res

print(pow(2, 0) == 1)
print(pow(2, 1) == 2)
print(pow(2, 5) == 32)
