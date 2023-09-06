import random
def list_new_rand_int(N):
    list_rand = []
    for i in range(N):
        list_rand.append(random.randint(0, 10))
    return(list_rand)

N = int(input ("Введите количество элементов массива: "))
min_N = int(input ("Введите нижнюю границу: "))
max_N = int(input ("Введите верхнюю границу: "))
list_N = list_new_rand_int(N)
list_ind = []
for i in range(N):
    if (list_N[i] >= min_N) & (list_N[i] <= max_N):
        list_ind.append(i)
print(list_N)
print(list_ind)