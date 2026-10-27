import random

l1 = random.sample(range(1000), 300) #Для пузырька
a = random.choice(l1)
counter_bin = 0 #Счетчик для бинарного
counter_lin = 0 #Счетчик для линейного
ind_lin = 0 #индекс искомого в линейном
ind_bin = 0 #индекс искомого в бинармном

for  i in range(300):
    counter_lin +=1
    if l1[i] == a:
        ind_lin = a
        break

print("Номер искомого элемнта" , ind_lin )
print("Количество оппераций по линейному поиску:" , counter_lin)

temp =0 # индекс ищущий элемент а
l_ind = 0 #правый индекс
r_ind = 299 #левый индекс
while l_ind <= r_ind:
    temp = l_ind + (r_ind - l_ind) // 2
    if l1[temp] == a:
        ind_bin = l1[temp]
        break
    elif l1[temp] < a:
        l_ind= temp+1
    elif l1[temp] > a:
        r_ind = temp-1
    counter_bin+= 1

print("Номер искомого элемнта" , ind_bin )
print("Количество оппераций по поиску линейкой:" , counter_bin)
