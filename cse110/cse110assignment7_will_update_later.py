# -*- coding: utf-8 -*-
"""CSE110Assignment7-will update later.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ODAELDSGQQ2eyNN6ZqS6BdyvfL1uVQeC
"""

#task1
def  sorting(my_list):
    for i in range(len(my_list)):
      for j in range(len(my_list) - i - 1):
          if my_list[j] > my_list[j + 1]:
              temp = my_list[j]
              my_list[j] = my_list[j + 1]
              my_list[j + 1] = temp

    print(my_list)

my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
sorting(my_list)

#task2
def sorting1(my_list):
  for i in range(len(my_list)):
    minpos = i
    for j in range(i, len(my_list)):
      if my_list[i] > my_list[j]:
        minpos = j
    temp = my_list[i]
    my_list[i] = my_list[minpos]
    my_list[minpos] = temp
  print(my_list)

sorting1(my_list)

my_list= [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

#task3
def  sorting3(my_list):
    for i in range(len(my_list)):
      for j in range(len(my_list) - i - 1):
          if my_list[j] < my_list[j + 1]:
              temp = my_list[j]
              my_list[j] = my_list[j + 1]
              my_list[j + 1] = temp

    print(my_list)

my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
sorting3(my_list)

#task4
def  sorting(my_list):
    for i in range(len(my_list)):
      if i % 2 == 0:
        for j in range(len(my_list) - i - 1):
          if j % 2 == 0:
            try:
              if my_list[j] > my_list[j + 2]:
                  temp = my_list[j]
                  my_list[j] = my_list[j + 2]
                  my_list[j + 2] = temp
            except:
              pass
      else:
        for j in range(len(my_list) - i - 1):
          if j % 2 != 0:
            try:
              if my_list[j] < my_list[j + 2]:
                  temp = my_list[j]
                  my_list[j] = my_list[j + 2]
                  my_list[j + 2] = temp
            except:
              pass

    print(my_list)

my_list = [10,30,20,70,11,15,22,16,58,100,12,56,70,80]
sorting(my_list)

#task5
my_list = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]

def sorting (my_list, pos):
    for i in range (len(my_list)):
        for j in range(len(my_list)- i- 1):
            if my_list[j][pos]<my_list[j+1][pos]:

                for index in range(4):
                    temp = my_list[j][index]
                    my_list[j][index]= my_list[j + 1][index]
                    my_list[j + 1][index] = temp
    for name in my_list:
        print (name[0])
c= input ()

if c== 'CSE110' :
    sorting(my_list, 1)
elif c =='PHY111':
    sorting(my_list, 2)
elif c =='MAT110':
    sorting(my_list, 3)

#task6

my_list=[4,2,3,1,6,5]
new_list=[]

for i in my_list:
    new_list.append(i)
my_list.sort()
count=0
for j in range(0,len(my_list)) :
    if (my_list[j]!=new_list[j]):
        count+=1
print(count)

#task7

import statistics
list_one = []
list_two = []

n = int(input("Element count  in list_one : "))
for i in range(0, n):
    element1 = int(input())
    list_one.append(element1)
print("list_one =",list_one)

n2 = int(input("Element count  in list_two : "))
for i in range(0, n2):
    element2 = int(input())
    list_two.append(element2)
print("list_two =",list_two)

list_three = list_one+list_two
list_three.sort()
print("sorted list =", list_three)
print("Median =  ",(statistics.median(list_three)))

#task8

def near_zero(list1):
    min_sum = None

    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            n1 = int(list1[i])
            n2 = int(list1[j])
            sum = n1 + n2
            if min_sum == None:
                min_sum = sum
            elif abs(sum) < abs(min_sum):
                min_sum = sum
                a = n1
                b = n2

    return "Two pairs which have the smallest sum = ",a,b

print(near_zero(input().split(",")))

#task9

point=[(5,3), (2,9), (-2,7), (-3,-4), (0,6), (7,-2)]
new1=point[0][0]
second1=point[0][1]
min_distance=(new1**2+second1**2)**0.5
for i in point:
    a,b=i
    distance=(a**2+b**2)**0.5
    if distance<min_distance:
        min_distance=distance
        closer=i
print("Minimum Distance:",min_distance)
print("Here the closet point is",closer,"which has a distance of",min_distance,"from the origin")

