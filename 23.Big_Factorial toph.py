def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number=int(input())
a=str(factorial_iterative(number))
print(a[-4: ])