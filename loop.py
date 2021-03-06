#!/usr/bin/env python
# coding: utf-8

# # Циклы

# ## Цикл for

# In[ ]:


# Дан массив целых чисел из N элементов. С помощью цикла найти значение минимального элемента.


# In[ ]:


# Самостоятельно
# Дан массив целых чисел из N элементов. С помощью цикла найти значение максимального элемента.
# В данном массиве найдите два наименьших элемента.


# In[ ]:


# Дан массив целых чисел из N элементов. Найти индекс минимального элемента.


# In[ ]:


# Дано N случайных чисел. Найти индекс последнего четного элемента. Если такого элемента нет, то вернуть -1.


# In[1]:


# Самостоятельно
# Дано N случайных чисел. Найти индекс первого отрицательного элемента. Если такого элемента нет, то вернуть -1.
# Дано N случайных чисел. Найти индекс элемента большего 10. Если такого элемента нет, то вернуть -1.
# Задан массив, состоящий из 16 элементов вещественного типа. За один проход по циклу определить индексы (местоположение) максимального и минимального элементов
# Задан массив, вычислить произведение минимального и максимального элементов.


# In[ ]:


# Подсчитать количество четных и нечетных элементов в заданном списке


# In[ ]:


# Самостоятельно
# Подсчитать количество положительных и отрицательных элементов в заданном списке
# Подсчитать количество элементов кратных 2 и 3 или в заданном списке


# In[ ]:


# Подсчитать сумму элементов в массиве


# In[ ]:


# enumerate
# Дан одномерный массив числовых значений, насчитывающий N элементов. После каждого отрицательного элемента вставить новый элемент, равный квадрату этого отрицательного элемента.


# In[ ]:


# Самостоятельно
# Подсчитать произведение элементов в массиве
# Подсчитать среднее арифметическое положительных и отрицательных элементов в массиве
# Определите количество перемен знаков элементов массива.
# В данном массиве найдите наибольшую серию подряд идущих элементов, расположенных по возрастанию.


# # Домашнее задание
# * Разбить список длиной N на подсписки длиной k. Например список [1, 2, 3, 4, 5, 6, 7, 8] k = 3: [[1, 2, 3], [4, 5, 6], [7, 8]] 
# * Сделать список скользящего среднего для окна длиной k. Например список [1, 2, 3, 4, 5] k = 2: [1.5, 2.5, 3.5, 4.5] 
# * Дан одномерный массив числовых значений, насчитывающий N элементов. Выполнить перемещение элементов массива по кругу вправо, т. е. A[1] → A[2]; A[2] → A[3]; ... A[n] → A[1]. (Использовать слайсирование нельзя, а именно A = A[1:] + A[0])
# * Дан одномерный массив числовых значений, насчитывающий N элементов. Поменять местами первую и вторую половины массива.

# ## Двумерные списки

# In[11]:


def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print("{:2}".format(matrix[row][col]), end=" ")
        print()


# Двумерная матрица представляет собой таблицу. Если одномерная матрица это список, то двумерная это список списков.  

# In[2]:


matrix = [[0] * 5] * 5
matrix


# Тогда чтобы обратиться к элементу нужно использовать двойную индексацию

# In[3]:


matrix[0][0]


# Попробуем изменить матрицу

# In[5]:


matrix[0][0] = 1
matrix


# ### Заполнение матрицы

# In[16]:


correct_matrix = [[i * j for i in range(1, 5)] for j in range(1, 5)]
correct_matrix


# In[17]:


correct_matrix[-1][-1] = 0
print_matrix(correct_matrix)


# In[18]:


zero_matrix = [[0 for _ in range(N)] for j in range(M)]
print_matrix(zero_matrix)


# In[19]:


zero_matrix[0][0] = 1
print_matrix(zero_matrix)


# In[20]:


from random import randint
N = 5
M = 6
random_matrix = [[randint(1, 9) for _ in range(N)] for j in range(M)]
print_matrix(random_matrix)


# In[ ]:


# Дан двухмерный массив N×M. Определить среднее арифметическое каждого столбца, определить максимум и минимум каждой столбца, а также их индексы.


# In[ ]:


# Дан двухмерный массив N×M. Определить среднее арифметическое каждой строки, определить максимум и минимум каждой строки, а также их индексы.


# In[ ]:


# Дана вещественная квадратная матрица порядка 5. Найти наименьший элемент на побочной диагонали
# Дан целочисленный квадратный массив 7×7. Найти строку с наибольшей суммой элементов.


# In[ ]:


# Дана квадратная матрица. Доказать, что она является "магическим" квадратом
magic = [[16,  1, 12,  7], 
         [11,  8, 15,  2], 
         [ 5, 10,  3, 18], 
         [ 4, 17,  6,  9]]


# In[ ]:


# Дан двухмерный массив 5×6. Определить среднее арифметическое положительных элементов каждого столбца.
# В матрице А(4-строки,3-столбца) поменять местами наибольшие элементы в первом и третьем столбцах.
# Задана квадратная матрица А размером N×N (N<=10),состоящая из действительных чисел. Найти произведение наименьших элементов каждого столбца матрицы


# # Домашнее задание
# * Выполнить обработку элементов квадратной матрицы A, имеющей N строк и N столбцов. Определить произведение элементов, расположенных параллельно побочной диагонали (ближайшие к побочной). Элементы побочной диагонали имеют индексы от [N,0] до [0,N].
# * Дано число n. Создайте массив int A[n][n], и заполните его по следующему правилу: числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1; числа, стоящие выше этой диагонали, равны 0; числа, стоящие ниже этой диагонали, равны 2.   
# 0 0 0 1  
# 0 0 1 2  
# 0 1 2 2  
# 1 2 2 2  
# * Дано число n и квадратный массив int A[n][n]. Проверьте, является ли массив симметричным относительно главной диагонали.  
# 0 1 2  
# 1 2 3  
# 2 3 4  
