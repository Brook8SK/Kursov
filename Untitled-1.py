# print ( 5 + 2/10)
# print (2/34 + (23/46)**2)
# print (100/25 + 25/100/100/25-10**2 + 100**1/2)
# # print ((2.5-2.25**1/2)/2**2+2.625/3.5)



# print ( 5 +2/10)
# print (2/34   + (23/46)**2)
# print ((2.5 - 2.25**1/2)/2**2 +2.625/3.5 )
# print ((100/25) + (25/100/100/25) - 10**2 + 100**1/2)

# o = input("Твое имя?") 
# print ("Heloo her  ", o)

# u = 35 
# u = str(35)
# print (u  + " KUBAT")

# n = [2 , 3 , 2]

# h = input ("сколько тебе лет? ")
# print (h , "years old")


# Цельсий = float(input("Сколько градусов цельсии? "))
# Фаренгейт = Цельсий*9/5+32
# print (Фаренгейт , "градусов фаренгейта")
# Фаренгейт_1 =float(input("Сколько градусов фарегейта? "))
# Цельсий_1 = (Фаренгейт_1-32)/1.8
# print(Цельсий_1, "градусов цельсия")



# n = int(input("Задай цифру? " ))
# o = int(input("Задай второе число? "))
# print (n + o)
# print("Погода ", 15 ,54, 34 , "." , sep="%")


# fio = "Иванов Иван Иванович"
# last = fio[:7]
# first = fio[7:12]
# middle = fio [12:20] 
# print (last , first , middle)

# date = "2025-09-06"
# yy = date [:4]
# mm = date [5:7]
# dd = date[-2:]
# print (yy,  mm , dd,  sep="\n")

# # kurs_name = "Data Analytics"
# # kol_students = 18
# # middle_check = 1490.5
# # kurs_activate=True

# # s = "PythonRocks"
# # fch = s[:1]
# # tail14 = s[7:]
# # mid = s[1:10]
# # rev = s[::-1]
# # print (fch, tail14, mid, rev, sep="\n")



# num = [4 , 4,32 ,2]
# n = 0 
# for k in num:
#     n += k
# print (n)
# a = 20
# b = 6
# print(a/b, a//b, a+b, a-b, a*b)



# def greet(name):
#     return "hello", (name)
 
# print (greet ("Kubat"))


# def discount(price, pct):
#     return 'mega pct:'  ,(price- pct*100)
# print (discount(1000, 10))



# nums = [1, 3, 5, 7,6, [1,3]]
# nums[0]  = 50
# nums [4] = 20
# print (nums[0])
# print (nums[5])
# print (nums[5][1])


# num = [1, 5,4]
# num.append (4)
# num.insert (1 , True)
# b = [5 ,  4]
# num.append (b)
# num.reverse()
# num.pop()
# num.remove(b)
# # num.clear()

# print (num)
# print (num.count(4))
# print (len(num))

# num = [1,2,3,4,5, True]
# for element in num:
#     element *= 2
#     print(element)


# num = int(input("Enter length: "))
# user = []
# i = 0
# while i < num:
#     string = "Enter element: " + str(1+1) + ";"
#     user.append(input("Enter element: "))
#     i+= 1
# print (user)


# n1 = int(input("num1: "))
# n2 = int(input("num2: "))
# print (n1 / n2 , n1 * n2 , sep="\n")


# n1 = int(input("num1: "))
# n2 = int(input("num2: "))
# n3 = n2
# n4 = n1
# print (n3 , n4)


# n = input("word: ")
# if n == n[::-1]:
#     print ("polindrom")
# else:
#     print ("Ne polindrom")

  

# n1 = int(input("N1: "))
# n2 = int ( input ( "N2:"))
# print (n1 + n2 )

# n1 = (input("Word: "))
# n2 = n1[::-1]
# if n1 == n2:
#     print ("polindrom")
# else: 
#     print ("ne polindrom")


# for i in range (0 , 21 , 2):
#     print (i)

# import random
# secret = random.randint (1, 10)
# guess = None 
# while guess != secret :
#        guess = int(input("Угадайте число от 1 до 10: "))
#        if guess < secret:
#         print("Больше")
#        elif guess > secret:
#         print("Меньше")
#        else:
#         print("Угадано!")


# import random
# n = random.randint(1, 10)
# if n == 5:
#     print("yes ")



# import math 
# n = sum(range(1,101))
# print (n)



# for i  in range(1,31):
#     if i % 3 == 0:
#        print (i)


# total = 0
# num = int(input("Введите число (отрицательное — стоп): "))
# while num >= 0:
#     total += num
#     num = int(input("Введите число (отрицательное — стоп): "))
# print("Сумма:", total)



# n1 = 0
# n2 = int(input ("Num "))
# while n2 !=0:
#     n1 += n2
#     n2 = int(input("Num "))
# print ("Sum ", n1)


# n1 = 0 
# while True:
#     n2 = int(input ())
#     word = input ()
#     if word == "stop":
#         break
#     n1 += n2
# print (n1)




# for i  in range (1,10 ):
#     print (f"{i}* {i} = {i **2} ")


# n = "python"
# n1 = (input ())
# while True  :
#     if n1 != n:
#        n1 = (input ())
#     else:
#        print ("yes")
#        break 

# def even(n):
#    if n % 2 == 0:
#         print (True)
#         return True
#    else:
#         print (False)
#         return False
# even(5)


# for i in range (6):
#     print ("Helloo")

# m = 0
# n = int(input("num: "))
# while n !=0:
#     m += n 
#     n = int (input("num: "))
# print ("sum:  ", m )


# for i in range (1,11):
#     print (i)

# for i in range (2, 21, 2):
#     print (i)


# for i in range (2 , 21):
#     if i % 2 == 0:
#         print (i , "Ч")
#     else:
#         print (i , "Не ч")


# n = 11
# while n != 0:
#     n -= 1
    
#     print (n)

# import math
# n = sum (range (1, 11))
# print (n)

# t = 0 
# for i in range (1, 11):
#     t += i
# print (t)


# n = 2
# while n < 20 :
#     n += 2
#     print (n , end=" ")


# for i in range (3 , 31 , 3):
#     print (i , end=" ")


# for i in range (1 , 51) :
#     if i % 5 == 0 or i % 3  ==  0
#         print  (i , end=" ")

# for i in range(1, 31):
#     if i  % 3 == 0 and i % 5 ==0:
#         print (i, "FizzBuzz")
#     elif i % 5 ==0:
#         print (i ,"Buzz")
#     elif i % 3 ==0: 
#         print (i ,"Fizz")
        

# import math 
# p = 1
# for i in range(2,11,2):
#     p*= i 
# print (p)

# w = input()
# w1 = "ayueioAYUIOE"
# c = 0
# for i in w:
#     if i in w1:
#         c += 1
# print (c)
    


# w = (input())
# if w == w[::-1]:
#     print ("polindrom")
# else:
#     print ("ne polindrom")



# n = list(map(int,input().split()))
# print (max(n))


# w = 0
# n = list(map(int,input().split()))
# for i in n:
#     w += n
# print (n)



# n = list(map(int,input().split()))
# n1 = []

# for i in n:
#     if i > 10:
#         n1.append(1)


# print (len(n1))
# print (n1)

# nech = 0
# ch = 0
# n = list(map(int,input().split()))
# n1 = []
# n2 = []
# for i in n:
#     if i % 2 == 0:
#         ch += i
#     else: 
#         nech += i 
# print (ch ,nech)



# y = int(input("How old are you? "))
# print (f'Тебе {y} лет! ')

 

# print (type(10))
# print (type(3.14))
# print (type("Hello"))
# print (type(True))
# print (type([1, 2, 3]))
# print (type ({"Name":"Nick" }))
# print (type ({1 , 2 ,3}))


# n = int(input("Num: "))
# if n > 10:
#     print (n, ">", 10)
# elif n == 10:
#     print (n ,"=" ,10)
# else:
#     print (n, "<", 10)


# n = int(input("Твой балл: "))
# if n>=90 and n<= 100:
#     print ("A")
# elif n>=80 and n<90:
#     print ("B")
# elif n>=70 and n<80:
#     print ("C")
# elif n>=60 and  n<70:
#     print ("D")
# elif n>= 0 and n<60:
#     print ("Ты не сдал! ")
# else:
#     print ("Таково количества баллов не бывает!!!")


# n = int(input("Num: "))
# if +n%2==0 and n>0:
#     print ("Число положительное и чётное")
# elif +n%2!= 0 and n>0:
#     print ("Число положительное и нечётное")
# elif n<0 and n%2==0:
#     print ("Число отрицательное и чётное")
# elif -n%2!=0 and n<0:
#     print ("Число отрицательное и нечётное")
# elif n==0:
#     print ("Это ноль")


# n = int(input())
# if n %2==0:
#     print ("Ch")
# else:
#     print ("Ne ch")


# n = input()
# for i in n [::2]:
#     print (i)
    


# n = list(map(int,input().split()))
# ch = 0 
# nech = 0
# for i in n:
#     if i % 2 == 0:
#         ch += i 
#     else: 
#         nech += i
# print (ch , nech )


# n = input()
# if n == n[::-1]:
#     print ("polin")
# else :
#     print ("ne polin")

# import math
# import random
# n = int(input("Сколько чисел вывести? "))
# n1 = []
# for _ in range(n):
#     i = random.randint(1, 100)
#     n1.append(i)





# print (max(n1))
# print (min(n1))
# print (sum(n1)/10)




# n = int(input())
# for i in range(1,11):
#     print (f'{n}*{i}={n*i}')


# n = 7
# for i in range(1,51):
#     if i % n == 0:
#         continue
#     print (i)


# n = int (input())

# for i in range (1,n):
#     if i%n==0 and i%1==0:
#         print (i)


# n = int (input())

# for i in range (1,n+1):
#     if n%i==0 :
#         print (i)


# w = input()
# w1 = "ayueioAYUIOE"
# c = 0
# for i in w:
#     if i in w1:
#         c += 1
# print (c)
    

# import random
# n = random.randint(1,10)

# while True:
#     n1 = int(input())
#     if n1 > n:
#         print ("Меньше")
#     elif n1 < n:
#         print ("Больше")
#     elif n1 == n:   
#         print ("YESS")
#         break


# n = (int(input()))
# for i in range(1, 11):
#     print (f'{n}x{i}={n*i}')


# import pandas as pd

# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35],
#     "City": ["New York", "San Francisco", "Los Angeles"]
# }
# df = pd.DataFrame(data)
# print(df)


# n = int(input())
# user = []
# i = 0
# while i <n :
#     user.append(input())
#     i += 1
# print (user)


# word = "itproger, top"
# # # # print (len(word))
# # # # print (word.count ("p"))
# # # print (word.upper())
# # # print (word.islower())
# # # print (word.lower())
# # # print (word.capitalize())
# # # print (word.find("p") )
# w1 =  (word.split(", "))
# # # print (w1[1])


# for i in range (len(w1)):
#     w1[i] = w1[i].capitalize()
  
# print (w1)



# result = ", ".join(w1)
# print (result)


# a = [1,1,2,3,5,8,13,21,34,55,89]
# for i in a:
#     if i < 5:
#         print (i)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 13]
# c = set(a) & set(b)
# print (c)



# a = [1, 9,10 , 11, 12]
# b = a[::-1]
# print (b)
# 
# a = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# print (a[1::2])


# l = int(input("skolko sm"))
# print (f'{l//100}м' )


# m = int (input("kg: "))
# print (f'{m//1000}T')

# b = int(input("b"))
# print (f'{b//1024}k')



# k=int(input("ch: "))
# n= int(input("ch>0"))
# for i in range(1,n):
#     print(k)




# A = int(input())
# B = int (input())
# for i in range(B,A +1):
    
#     print (i)


# A = int(input())
# B = int (input())
# for i in range(B+1,A):
    
#     print (i)



# n = int(input())
# if n% 2 ==0 :
#     print("Ch")
# else:
#     print ("Ne ch")


# n1 = int(input())
# n2 = int(input())
# print (max(n1,n2))



n1 = int(input())
# if n1 > 0:
#     print ("+")
# elif n1<0:
#     print ("-")
# else:
#     print ("=")

# m = 0
# for  i in range(1,n1+1):
#     m += i 
# print(m)


# for i in range:
    
#     print (len(i))


import requests
url = 'https://example.com'
response = requests.get(url)
print(response.text) 