import random

l1 = random.sample(range(1000), 300) #Для пузырька
l2 = random.sample(range(1000), 300) #Для выборки
counter_b = 0 #Счетчик для пузырька
counter_s = 0 #Счетчик для выборки
a = [] #Пустой масив для отсортированых элементов

for i in range(300) :
    for j in range (300-1): #Диапазон 99, т.к у 100-того элемента нету следующего за ним
        if l1[j+1] > l1[j]: 
            l1[j+1] , l1[j] = l1[j] , l1[j+1]
            print(l1) #После каждой опперации показываем состояние
        counter_b +=1 
print(counter_b)


for i in range(300):
    min = 0 
    for j in range(300-i): 
        if l2[j] > l2[min] : 
            min = j  
        counter_s += 1
    a.append(l2[min]) #Добавляем в новую
    l2.pop(min) #Удаляем из старой
    print(a)