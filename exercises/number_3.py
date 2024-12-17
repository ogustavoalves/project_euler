from math import sqrt

# checa se um número é primo ao dividir ele por todos os valores de 2 até ele mesmo - 1
def is_prime_number (num):
    for x in range(2, int(sqrt(num)) + 1): # checar sempre até a raiz quadrada do número
        if num % x == 0:
            return False
    return True

user_num = 600851475143
dividers = []

for y in range(2, int(sqrt(user_num)) + 1): # checar sempre até a raiz quadrada do número
    if user_num % y == 0 and is_prime_number(y) == True:
        dividers.append(y)

# prime_dividers = list(filter(is_prime_number, dividers))
print(f'maior divisor primo do número {user_num} é: {max(dividers)}')