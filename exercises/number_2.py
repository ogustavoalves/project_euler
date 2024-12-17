fibo_list = [1, 2]
sum_fibo = 0
for x in range(2, 32):
    fibo_list.append(fibo_list[x-1] + fibo_list[x-2])
    
for x in range(len(fibo_list)):
    if fibo_list[x] % 2 == 0:
        sum_fibo += fibo_list[x]

print(sum_fibo)

