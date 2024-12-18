from math import sqrt

# checa se um número é primo ao dividir ele por todos os valores de 2 até ele mesmo - 1
def is_prime_number (num):
    for x in range(2, int(sqrt(num)) + 1): # faixa de números testados de 2 até a raiz quadrada do número + 1
        if num % x == 0:
            return False
    return True

user_num = 600851475143
prime_factors = []

for y in range(2, int(sqrt(user_num)) + 1): # faixa de números testados de 2 até a raiz quadrada do número + 1
    # checa se o número em y é divisor de user_num (user_num % y == 0) e
    # se o número em y é um número primo (retorno de is_prime_number == True)
    if user_num % y == 0 and is_prime_number(y) == True:
        prime_factors.append(y)

# prime_dividers = list(filter(is_prime_number, dividers))
print(f'maior divisor primo do número {user_num} é: {max(dividers)}')