def is_prime(num):
    contador = 0
    i = 1
    for i in range(1, num + 1):
        if num % i == 0:
            contador = contador + 1
    if contador == 2:
        return True
    else:
        return False


print(is_prime(73))
    
