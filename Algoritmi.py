import random


#Bouble Sort con numeri in random
lista1 = []
lista2 = []
lista3 = []
for i in range (10):
    #genero 20 numeri casuali
    numero1 = random.randint(0, 100)
    lista1.append(numero1)
    numero2 = random.randint(0, 100)
    lista2.append(numero2)
    numero3 = random.randint(0, 100)
    lista3.append(numero3)

def bouble_sort(l):
    n = len(l)
    print("ordino la lista con bouble sort")
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                # Scambio degli elementi
                temp = l[j+1]
                l[j+1] = l[j]
                l[j] = temp
        print(i+1, l)
    return l 
bouble_sort(lista1)

def insertion_sort(l):
    n = len(l)
    print("Ordino la lista usando l'Insertion Sort")
    for i in range(1, n):
        current_value = l[i]
        j = i - 1
        while j >= 0 and l[j] > current_value:
            l[j + 1] = l[j]
            j -= 1
        #fine while
        l[j + 1] = current_value
        print(i+1, l)
    return l
insertion_sort(lista2)

def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left_half = l[:mid]
        right_half = l[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                l[k] = left_half[i]
                i += 1
            else:
                l[k] = right_half[j]
                j += 1
            k += 1
            print(l)
        while i < len(left_half):
            l[k] = left_half[i]
            i += 1
            k += 1
            print(l)
        while j < len(right_half):
            l[k] = right_half[j]
            j += 1
            k += 1
        print(l)
print("lista non ordinata prima di merge sort")
print(lista3)
merge_sort(lista3)