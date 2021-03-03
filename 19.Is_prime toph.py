def is_prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
    return True


num = int(input())
check_prime = is_prime(num)
if check_prime:
    print('Yes')
else:
    print('No')
