# -*- coding: utf-8 -*-
"""CSE110-Lab-Assignment-6-will update later.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19mcg0OjyHYbG0RpqymYX9tKIoDfxmhZ4

# CSE110 Lab Assignment 6
This assignment is to guide you to solve everything you have learned so far by implementing functions in Python.



Write your name, student id and CSE110 section below:
"""

#STUDENT NAME: aninda  debnath
#STUDENT ID: 21301211
#CSE110 SECTION: 10

"""**<font color='red'>[MUST MAINTAIN VARIABLE NAMING CONVENTIONS FOR ALL THE TASKS]</font>**

## Write the Python code of the following problems:

### Task 1
Write a function called **even_checker** that takes a number as an argument and prints whether the number is even or odd **inside the function**.

===================================

**Example1:** \
**Function Call:**\
even_checker(5)\
**Output:**\
Odd!!

=============================

**Example2:** \
**Function Call:**\
even_checker(2)\
**Output:**\
Even!!


"""

# to do

def even_checker(num):
    if num%2==0:
        print("Even!!")

    else:
        print("Odd!!")

even_checker(9)

"""### Task 2
Write a python function that takes the limit as an argument of the Fibonacci series and prints till that limit.

===================================

**Function Call:**\
fibonacci(10)\
**Output:**\
0 1 1 2 3 5 8\
======================\
**Function Call:**\
fibonacci(5)\
**Output:**\
0 1 1 2 3 5
"""

# to do
def fibonacci(value):
    x=0
    print(x,end=" ")
    y=1
    print(y,end=' ')
    sum=x+y
    while(sum<=value):
        print(sum,end=' ')
        x=y
        y=sum
        sum=x+y
fibonacci(10)

"""### Task 3
Write a function called **foo_moo** that takes a number as an argument and **returns** the following statements according the below mentioned conditions. Then, finally prints the statement in the function call.

* 	If the number is divisible by 2, it should return "Foo".
*   If the number is divisible by 3, it should return "Moo".
*   If the number is divisible by both 2 and 3, it should return "FooMoo".
*   Otherwise, it returns "Boo".

===================================

**Example1:** \
**Function Call:**\
foo_moo(5)\
**Output:**\
Boo

=================


**Example2:** \
**Function Call:**\
foo_moo(4)\
**Output:**\
Foo

=================


**Example3:** \
**Function Call:**\
foo_moo(6)\
**Output:**\
FooMoo


"""

# to do

def foo_moo(num):

       if  num%2==0 and num%3==0:
           return "FooMoo"
       elif num%2==0 :
           return "Foo"
       elif num % 3 == 0:
           return "Moo"

       else:
           return "Boo"

print(foo_moo(3))

"""### Task 4
Write a python function that takes a string as an argument. Your task is to calculate the number of uppercase letters and lowercase letters and print them in the function.

===================================

**Function Call:**\
function_name('The quick Sand Man')\
**Output:**\
No. of Uppercase characters : 3\
No. of Lowercase Characters: 12\
============================\
**Function Call:**\
function_name('HaRRy PotteR')\
**Output:**\
No. of Uppercase characters : 5\
No. of Lowercase Characters: 6

"""

# to do
# counter_upper=0
# counter_lower=0
def count_upper_lower_part(string1):
    counter_upper=0
    counter_lower=0


    for i in range(len(string1)):
        if string1[i]>= "A" and string1[i] <= "Z":
            counter_upper += 1
        elif string1[i]>="a" and string1[i]<= "z":
            counter_lower += 1
    print("No. of Uppercase characters :",counter_upper)
    print("No. of Lowercase Characters:",counter_lower)




count_upper_lower_part('HaRRy PotteR')

"""### Task 5
Write a function called **calculate_tax** that takes 3 arguments: your age, salary, and current job designation.


Your first task is to take these arguments as user input and pass these values to the function.

Your second task is to implement the function and calculate the tax as the following conditions:
*  **NO TAX IF YOU ARE LESS THAN 18 YEARS OLD.**
*  **NO TAX IF YOU ARE THE PRESIDENT OF THE COMPANY**
*  No tax if you get paid less than 10,000
*  5% tax if you get paid between 10K and 20K
*  10% tax if you get paid more than 20K


Finally return this tax value. Then print the returned value in the function call.

===================================

**Hints:**\
Here the job designation is a string, so it can be written in both uppercase and lower cases. So, you need to check the value ignoring the case.

===================================

**Example1:** \
**Input:**\
16\
20000\
Student\
**Function Call:**\
calculate_tax(16, 20000, 'Student')\
**Output:**\
0

===================================

**Example2:** \
**Input:**\
20\
18000\
assistant manager\
**Function Call:**\
calculate_tax(20, 18000, 'assistant manager')\
**Output:**\
900.0


===================================

**Example3:** \
**Input:**\
20\
22000\
assistant manager\
**Function Call:**\
calculate_tax(20, 22000, 'Assistant manager')\
**Output:**\
2200.0

===================================


**Example4:** \
**Input:**\
20\
122000\
president\
**Function Call:**\
calculate_tax(20, 122000, 'president')\
**Output:**\
0




"""

# to do
def calculate_tax(age,salary,current_job):


    if age<18:

        return 0
    elif salary<10000:

        return 0
    elif current_job=="president":

            return 0
    elif salary>=10000 or salary<=20000:

        return salary*0.05

    elif salary>20000:
        return salary*(10//100)


age=int(input("Enter Your age: "))
salary= int(input("Enter your salary number:  "))
current_job=input("Enter your job name: ")
print(calculate_tax(age,salary,current_job))

"""### Task 6
Write a function which will take 1 argument, number of days.

Your first task is to take the number of days as user input and pass the value to the function.

Your second task is to implement the function and calculate the total number of years, number of months, and the remaining number of days as output. No need to return any value, print inside the function.

**Note:** Assume, each year to be 365 days and month to be 30 days.

=====================================================

**Hint(1):** \
Divide and mod the main input to get the desired output.

**Hint(2):**
This task’s calculation is similar to Assignment-1’s seconds to hours, minutes conversion.

=====================================================

**Example01**

**Input:**\
4330\
**Function Call:**\
function_name(4330)\
**Output:**\
11 years, 10 months and 15 days

================================

**Example02**

**Input:**\
2250\
**Function Call:**\
function_name(2250)\
**Output:**\
6 years, 2 months and 0 days



"""

# todo
def calculation_time(Days):
    year=Days//365
    left_days=Days%365
    month=left_days//30
    rem_days=left_days%30
    print(year,"years,",month,"months and",rem_days,"days")
Days=int(input("Enter the days number: "))
calculation_time(Days)

"""### Task 7
Write a function called **show_palindrome** that takes a number as an argument and then returns a palindrome string. Finally, prints the returned value in the function call.

=====================================================

**Example1:** \
**Function Call:**\
show_palindrome(5)\
**Output:**\
123454321

===================

**Example2:** \
**Function Call:**\
show_palindrome(3)\
**Output:**\
12321

"""

# to do

def show_palindrome(num):
    ans=""
    for i in range(1,num+1):
        ans+=str(i)
    for j in range(num-1,0,-1):
        ans+=str(j)
    return ans

print(show_palindrome(5))

"""### Task 8
Write a function called **show_palindromic_triangle** that takes a number as an argument and prints a Palindromic Triangle in the function.

**<font color='blue'>[Must reuse the show_palindrome() function of the previous task]</font>**



=====================================================

**Hints(1):** \
Need to use both print() and print( , end = " ") functions


=====================================================

**Example1:** \
**Function Call:**\
show_palindromic_triangle(5)\
**Output:**

&emsp; &emsp; &emsp; &emsp; 1\
&emsp; &emsp; &emsp; 1 &nbsp; 2 &nbsp; 1 \
&emsp; &emsp; 1 &nbsp; 2 &nbsp; 3 &nbsp; 2 &nbsp; 1 \
&emsp; 1 &nbsp; 2 &nbsp; 3 &nbsp; 4 &nbsp; 3 &nbsp; 2 &nbsp; 1 \
1 &nbsp; 2 &nbsp; 3 &nbsp; 4 &nbsp; 5 &nbsp; 4 &nbsp; 3 &nbsp; 2 &nbsp; 1

=============================================================


**Example2:** \
**Function Call:**\
show_palindromic_triangle(3)\
**Output:**

&emsp; &emsp; 1 \
&emsp; 1 &nbsp; 2 &nbsp; 1 \
1 &nbsp; 2 &nbsp; 3 &nbsp; 2 &nbsp; 1



"""

# to do
def show_palindromic_triangle(num):
    for line in range(1,num+1):
        space_number=num-line
        for space in range(1,space_number+1):
            print("#",end="")

        print(show_palindrome(line))

num=int(input("Enter the number: "))
show_palindromic_triangle(num)

n=int(input("enter the number: "))
for line in range(1,n+1):
    space_count=n-line  #3
    for space in range(1,space_count+1):  #(1,4) 1 2 3
        print(" ",end=" ")
    for col in range(1,line+1):
        print(col,end=" ")
    for col in range(line-1,0,-1):
        print(col,end=' ')
    print()r

"""### Task 09
Write a function called **area_circumference_generator** that takes a radius of a circle as a  function parameter and calculates its circumference and area. Then returns these two results as a **tuple** and prints the results using tuple unpacking in the function call accorrding to the given format.

<font color='blue'>**[Must use tuple packing & unpacking]** </font>

=====================================================

**Example1:** \
**Function Call:**\
area_circumference_generator(1)\
**Output:**\
(3.141592653589793, 6.283185307179586)\
Area of the circle is 3.141592653589793 and circumference is 6.283185307179586

====================================

**Example2:** \
**Function Call:**\
area_circumference_generator(1.5)\
**Output:**\
(7.0685834705770345, 9.42477796076938)\
Area of the circle is 7.0685834705770345 and circumference is 9.42477796076938

====================================


**Example3:** \
**Function Call:**\
area_circumference_generator(2.5)\
**Output:**\
(19.634954084936208, 15.707963267948966)\
Area of the circle is 19.634954084936208 and circumference is 15.707963267948966

"""

# to do
def area_circumference_generator(radius):
    import math
    area=math.pi*radius**2
    circumference=2*math.pi*radius

    ans=(area,circumference)

    return ans


result=area_circumference_generator(2.5)
print(result)
area,circumference=result
print("Area of the circle is",area,"and circumference is",circumference)

"""### Task 10
Write a function called **make_square** that takes a tuple in the parameter as a range of numbers (starting point and ending point (included)). The function should **return a dictionary** with the numbers as keys and its squares as values.

=====================================================

**Hints:** \
You need to declare a dictionary to store the result. You should use the range function to run the “for loop”.


=====================================================

**Example1:** \
**Function Call:**\
make_square((1,3))\
**Output:**\
{1: 1, 2: 4, 3: 9}

====================================

**Example2:** \
**Function Call:**\
make_square((5,9))\
**Output:**\
{5: 25, 6: 36, 7: 49, 8: 64, 9: 81}




"""

def make_square(tup):
    ans={}
    val1,val2=tup
    for i in range(val1,val2+1,1):
        product=i**2
        ans[i]=product
    return ans
print(make_square((1,3)))

"""### Task 11
Write a function called **rem_duplicate** that takes a tuple in the parameter and **return a tuple** removing all the duplicate values. Then print the returned tuple in the function call.

<font color='red'>**[Cannot use remove() or removed() for this task]** </font>

=====================================================

**Hints:** \
Unlike lists, tuples are immutable so, the tuple taken as an argument cannot be modified. But list can be modified and lastly for returning the result use type conversion. You need to use membership operators (in, not in) for preventing adding any duplicates values.

=====================================================


**Example1:** \
**Function Call:**\
rem_duplicate((1,1,1,2,3,4,5,6,6,6,6,4,0,0,0))\
**Output:**\
(1, 2, 3, 4, 5, 6, 0)

====================================

**Example2:** \
**Function Call:**\
rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))\
**Output:**\
('Hi', 1, 2, 3, 'a', [1, 2])




"""

# to do
def  rem_duplicate(tup):
    ans = []

    for i in tup:
        if i not in ans:
            ans.append(i)
    temp=tuple(ans)
    return temp

print(rem_duplicate(('Hi', 1, 2, 3, 'a', [1, 2])))

"""### Task 12
Write a python function that takes a list as an argument. Your task is to create a new list where **each element can be present at max 2 times**. Inside the function, print the number of elements removed from the given list. Finally, return the new list and print the result.

=====================================================

**Hint:** Use list_name.count(element) to count the total number of times an element is in a list. list_name is your new list for this problem.

=====================================================

**Function Call:**\
function_name([1, 2, 3, 3, 3, 3, 4, 5, 8, 8])\
**Output:**\
Removed: 2\
[1, 2, 3, 3, 4, 5, 8, 8]\
================================\
**Function Call:**\
function_name([10, 10, 15, 15, 20])\
**Output:**\
Removed: 0\
[10, 10, 15, 15, 20]
"""

def max_two_count(list1):
    ans=[]
    remove=0
    for i in list1:

        if ans.count(i)>=2:
            remove+=1
        else:
            ans.append(i)
    print("Removed:",remove)

    return ans
list1=[1, 2, 3, 3, 3, 3, 4, 5, 8, 8]
print(max_two_count(list1))

"""### Task 13
Write a python function that will perform the basic calculation (addition, subtraction, multiplication and division) based on 3 arguments. They are:
- Operator ('+', '-', '/', '*')
- First Operand (any number)
- Second Operand (any number)

Your first task is to take these arguments as user input and pass the values to the function parameters.

Your second task is to write a function and performs the calculation based on the given operator. Then, finally return the result in the function call and print the result.

=====================================================

**Input:**\
"+"\
10\
20\
**Function Call:**\
function_name("+", 10, 20)\
**Output:**\
30.0

================================

**Input:**\
"*"\
5.5\
2.5\
**Function Call:**\
function_name("*", 5.5, 2.5)\
**Output:**\
13.75

"""

# to do
def calculation_argumand(operator,first_operand,second_operand):
    if (operator=='+', '-', '/', '*'):
        if operator=="+":
            return first_operand+second_operand

        elif operator=="-":
            return first_operand-second_operand
        elif operator=="/":
            return  first_operand/second_operand
        else:
            return first_operand*second_operand

operator=input("Enter your operator: ")
first_operand=int(input("Enter the first number:"))
second_operand=int(input("Enter the second number: "))
print(calculation_argumand(operator,first_operand,second_operand))

"""### Task 14
Write a function which will take 2 arguments. They are:
- Sentence
- position

Your first task is to take these arguments as user input and pass these values to the function parameters.

Your second task is to implement the function and remove the characters at the index number which is divisible by the position (Avoid the index number 0 as it will always be divisible by the position, so no need to remove the index 0 character).
Finally, add the removed characters at the end of the new string.

Return the value and then finally, print the new string at the function call.

<font color='red'>**[Cannot use remove() or removed() for this task]** </font>

=====================================================

**Input:**\
"I love programming."\
3\
**Function call:**\
function_name("I love programming.", 3)\
**Output:**\
I lveprgrmmngo oai.

==============================================

**Input:**\
"Python is easy to learn. I love python."\
6\
**Function call:**\
function_name("Python is easy to learn. I love python.", 6)\
**Output:**\
Pythonis eay to earn.I lov pythn. sl eo

"""

#todo
def function_name(Sentence,position):

    ans=Sentence[0]+''
    add=''


    for i in range(1,len(Sentence)):
        if i%position!=0:
            ans+=Sentence[i]
        elif i%position==0:
            add+=Sentence[i]

    temp=ans+add
    return temp

Sentence=input("Enter the Sentence: ")
position=int(input("Enter the position: "))

print(function_name(Sentence,position))

"""### Task 15
You have been hired as an app developer for the company. The company plans to make an app for a grocery store where the user can order groceries and see the total amount to be paid in the cart section.

To build this feature, you have to write a function that takes 2 arguments. They are:
- order_items (must be a list)
- location (default value should be set to "Dhanmondi")

Your first task is to take a list of items from the user. Pass the list into the function parameter along with the optional location (Use default argument technique). (Also, no need to take location as input, pass this any value you want.)

Your second task is to implement the function. In the function, create a dictionary for the items shown in the table. Calculate the total price of the items passed as a list to the function. Additionally, add a delivery fee of 30 taka if the location is Dhanmondi. Otherwise, add a delivery fee of 70 taka. Finally, return the value and print it.

| Item | Price(Tk) |
| --- | --- |
| Rice | 105 |
| Potato | 20 |
| Chicken | 250 |
| Beef | 510 |
| Oil | 85 |

=====================================================

**Hint:** The keys are the items and values are the corresponding price. Iterate the items in the list and check if the items in the list are available in the dictionary keys or not. If it is available, add the price.

=====================================================

**Example1:**\
function_name(["Rice", "Beef", "Rice"], "Mohakhali")

total = 105 + 510 + 105 = 720 (Take the price of each item and add them.)\
total = 720 + 70 = 790 (Finally, add the delivery fee based on the location.)

**Input:**\
["Rice", "Beef", "Rice"]\
**Function Call:**\
function_name(["Rice", "Beef", "Rice"], "Mohakhali")\
**Output:**\
790

==============================================

**Example2:**

function_name(["Rice", "Beef", "Rice"])

total = 105 + 510 + 105 = 720 (Take the price of each item and add them.)\
total = 720 + 30 = 750 (Since no location is passed in the parameter, it will use the default location-"Dhanmondi". For dhanmondi, delivery fee of 30 taka)

**Input:**\
["Rice", "Beef", "Rice"]\
**Function Call:**\
function_name(["Rice", "Beef", "Rice"])\
**Output:**\
750
"""

#todo
def grocery_store(oder_items,location="Dhanmondi"):
    bill=0
    if location=="Dhanmondi":
        bill+=30
    else:
        bill+=70
    price_dict={"Rice":105,"Potato":20,"Chiken":250,"Beef":510,"Oil":85}
    for item in order_items:
        bill+=price_dict[item]
    return bill

order_items=["Rice", "Beef", "Rice"]
location= "Dhanmondi"
print(grocery_store(order_items,location))

"""## Optional Tasks (16 -21) [Ungraded]

### Task 16
Write a function called **splitting_money** that takes an “amount” of money as a argument.

Your first task is to take the “amount” of money as user input and pass the value to the function paramater.

Your second task is to implement the function and calculate how that money can be split into 500, 100, 50, 20, 10, 5, 2, and 1 taka notes.

Then print the returned value in the function call.

=====================================================


**Hints:** \
This task’s calculation is similar to Assignment-1’s seconds to hours, minutes conversion. To return the result containing multiple strings, you need to store it in a variable and return it at the end of the function.

=====================================================


**Example1:** \
If the money is 1234, then the function should return

"500 Taka: 2 note(s) \
100 Taka: 2 note(s) \
20 Taka: 1 note(s) \
10 Taka: 1 note(s) \
2 Taka: 2 note(s)"

=====================================================

**Example2:** \
If the money is 151, then the function should return

"100 Taka: 1 note(s)\
50 Taka: 1 note(s)\
1 Taka: 1 note(s)"
"""

#todo
def splitting_money(amount):


        taka_500 =amount//500
        print("500 taka:",taka_500,"note(s)")
        Left_amount =amount%500
        taka_100=Left_amount//100
        print("100 taka",taka_100,'note(s)')
        left_amount=Left_amount%100
        if left_amount>=50:
            taka_50=left_amount//50
            print("50 taka:",taka_50,'note(s)')
            left_amount1=left_amount%50
            taka_20 = left_amount1// 20
            print("20 taka:", taka_20,'note(s)')
            left_amount2=left_amount1%20
            taka_10 = left_amount2// 10
            print("10 taka:", taka_10,'note(s)')
            left_amount3=left_amount2%10
            taka_2=left_amount3//2
            print("2 taka:", taka_2,'note(s)')



        else:
            taka_20=left_amount//20
            print("20 taka:",taka_20,'note(s)')
            left_amount1=left_amount%20
            taka_10=left_amount1//10
            print("10 taka:",taka_10,'note(s)')
            left_amount2=left_amount1%10
            taka_2=left_amount2//2
            print("2 taka:",taka_2,'note(s)')


amount=int(input("Enter the amount: "))
splitting_money(amount)

"""### Task 17
Write a function called **remove_odd** that takes a list of numbers that have both even and odd numbers mixed. \
Your function should remove all the odd numbers and **return a compact list** which only contains the even numbers.

<font color='red'>**[Cannot use remove() or removed() for this task]** </font>

=====================================================

**Example1:** \
**Function Call:**\
remove_odd ([21, 33, 44, 66, 11, 1, 88, 45, 10, 9])\
**Output:**\
[44, 66, 88, 10]

====================================

**Example2:** \
**Function Call:**\
remove_odd ([11,2,3,4,5,2,0,5,3])\
**Output:**\
[2, 4, 2, 0]


"""

#todo
def remove_odd(list_1):
    list_2=[]
    for i in range(len(list_1)):
        if list_1[i]%2==0:
            list_2.append(list_1[i])
    return list_2
list_2=[21, 33, 44, 66, 11, 1, 88, 45, 10, 9]
print((remove_odd(list_2)))

"""### Task 18
Write a function which will take 4 arguments. They are:
- starting value(inclusive)
- ending value(exclusive)
- first divisor
- second divisor

Your first task is to take these arguments as user input and pass these values to the function.

Your second task is to implement the function and find all the numbers that are divisible by the <u> **first divisor or second divisor but not both**</u> from the starting value(inclusive) and ending value(exclusive). Add all the numbers that are divisible and finally return this value. Print the returned value in the function call.

=====================================================

**Input:**\
10\
40\
4\
7\
**Function Call:**\
function_name(10, 40, 4, 7)\
**Output:**\
210\
================================\
**Input:**\
5\
100\
3\
4\
**Function Call:**\
function_name(5, 100, 3, 4)\
**Output:**\
2012



"""

#todo
def number_count(*data):
    number_1=data[0]
    number_2=data[1]
    sum=0
    for i in range(number_1,number_2):
         if (i%data[2] and i%data[3]):
             pass
         elif (i%data[2] or i%data[3]):
             sum+=i
         elif (i%data[2] or i%data[3]):
             sum+=i
    print(sum)
    #     if (number)
    #     if (number_1%data[2] or number_1%data[3]):
    #         sum+=number_1
    #     elif (number_2%data[2] or number_2%data[3]):
    #         sum+=number_2


number1=int(input("Enter the number: "))
number2=int(input("Enter the number: "))
number3=int(input("enter the 1st divisor: "))
number4=int(input("enter the 2nd divisor: "))
# data=int(input("Enter the number"))
number_count(number1,number2,number3,number4)
# number_count(10,40,4,7)

"""### Task 19
Write a python function which will take a string as an argument.

Your first task is to take a string as user input and pass the value to the function.

Your second task is to implement a function which will check whether all the alphabets from a to j (convert all the alphabets to lowercase) has appeared at least once in the given string or not.
- If all of these alphabets (a to j) appear at least once, then the result will be 5.
- If any one of the alphabets (a to j) is not in the given string, then the result will be 6.

Return this result and print the statement, "PSG will win the Champions League this season" that many times.

=====================================================

**Example01:**
"A black jackal is hunting a full grown deer"

Here all the alphabets from A to J are present at least once. So, the function will return 5 and will print the statement 5 times.

**Input:**\
"A black jackal is hunting a full grown deer"\
**Function Call:**\
function_name("A black jackal is hunting a full grown deer")\
**Output:**\
PSG will win the Champions League this season\
PSG will win the Champions League this season\
PSG will win the Champions League this season\
PSG will win the Champions League this season\
PSG will win the Champions League this season

==============================================

**Example02:**

**Input:**\
"ABBCDEFEFGHI"\
**Function Call:**\
function_name("ABBCDEFEFGHI")\
**Output:**\
PSG will win the Champions League this season\
PSG will win the Champions League this season\
PSG will win the Champions League this season\
PSG will win the Champions League this season\
PSG will win the Champions League this season\
PSG will win the Champions League this season

"""

#todo
def alphabets_string(string_1):
    low_string=string_1.lower()
#     string1=""


#     for i in range(ord("a"),ord("z")):
#     for j in range(len(low_string)):
#         if low_string[j]>="a" and low_string[j]<="j":
#             string1+=low_string[j]


    for x in range(ord("a"),ord("k")):
#                 for y in range(len(string1)):
             if chr(x) not in low_string:
                    return 6

    return 5
    print(string1)
#     if counter>0:
#         print("PSG will win the Champions League this season")
#     else:
#         print("hoise")

string_1 = input("enter the string: ")
val=(alphabets_string(string_1))
for i in range(1,val):
    print("a")

"""### Task 20
Write a function called **individul_bonus_calculation** which will take 4 arguments. They are:

- The player name
- Yearly earning of that player
- The total goal scored this season by that player
- Bonus percent per goal.


Your task is to implement the above-mentioned function that will calculate the total bonus on the yearly earnings of a player for the total goals he had scored.

Additionally,
 * If the goal scored is above 30, add a (additional) bonus of 10000 taka.
 * If it is between 20 and 30 inclusive, add an extra 5000 taka.

<font color='blue'>[ For this task, no need to take any input from the user. Call the functions and print the values inside the function. ] </font>



=====================================================

**Example1:**\
individul_bonus_calculation("Neymar", 1200000, 35, 5)

bonus = 35 * (5 / 100 * 1200000) + 10000 = 2110000

**Function call:**\
individul_bonus_calculation("Neymar", 1200000, 35, 5)\
**Output:**\
Neymar earned a bonus of  2110000 Taka for 35 goals.

=====================================================

**Example2:**\
individul_bonus_calculation('Jamal', 700000, 19, 8)

bonus = 19 * (8 / 100 * 700000) + 0 = 1064000

**Function call:**\
individul_bonus_calculation('Jamal', 700000, 19, 8)\
**Output:**\
Jamal earned a bonus of 1064000 Taka for 19 goals.

=====================================================

**Example3:**\
individul_bonus_calculation('Luis', 80000, 25, 10)

bonus = 25 * (10 / 100 * 80000) + 5000 = 205000

**Function call:**\
individul_bonus_calculation('Luis', 80000, 25, 10)\
**Output:**\
Luis earned a bonus of 205000 Taka for 25 goals.

=====================================================
"""

def  individul_bonus_calculation(player_name,yearly_income,total_goal,bonous_percent_goal):
    bonous=0
    goal_score_bonous=0
    if total_goal>30:
        goal_score_bonous+=10000
    elif total_goal>20 and total_goal<=30:
        goal_score_bonous+=5000

    bonous+=(total_goal*(bonous_percent_goal/100*yearly_income))+goal_score_bonous
    print(player_name," earned a bonus of",int(bonous),"Taka for",total_goal,"goals")
individul_bonus_calculation("Neymar", 1200000, 35, 5)

"""### Task 21
You have been hired by the Abahani football club to write a function that will calculate the total bonus on the yearly earnings of each player for the total goals they have scored.

Since the number of players will vary, you decide to use the "*args" technique that you learned in your CSE110 class.

For each player: pass the name, yearly earning, the total goal scored this season, bonus percent per goal.

Additionally,
 * If the goal scored is above 30, add an extra bonus of 10000 taka.
 * If it is between 20 and 30 inclusive, add an extra 5000 taka.

<font color='blue'>[ For this task, no need to take any input from the user. Call the functions and print the values inside the function. ] </font>

**<font color='blue'>[Must reuse the individul_bonus_calculation() function of the previous task]</font>**


=====================================================

**Example1:**\
cal_bonus("Neymar", 1200000, 35, 5)

bonus = 35 * (5 / 100 * 1200000) + 10000 = 2110000

**Function call:**\
cal_bonus("Neymar", 1200000, 35, 5)\
**Output:**\
Neymar earned a bonus of  2110000 Taka for 35 goals.

=====================================================

**Example2:**\
**Function call:**\
function_name("Neymar", 1200000, 30, 10, "Jamal", 700000, 19, 5)\
**Output:**\
Neymar earned a bonus of 3605000 Taka for 30 goals.\
Jamal earned a bonus of 665000 Taka for 19 goals.


=====================================================

**Example3:**\
**Function call:**\
function_name("Neymar", 1200000, 35, 5, 'Jamal', 700000, 19, 8, 'Luis', 80000, 25, 10))\
**Output:**\
Neymar earned a bonus of 2110000 Taka for 35 goals.\
Jamal earned a bonus of 1064000 Taka for 19 goals.\
Luis earned a bonus of 205000 Taka for 25 goals.


"""

# to do
def player_bonus_calculation(*data): #player_name,yearly_income,total_goal,bonous_percent_goal

#     player_name=data[0]
#     yearly_income=data[1]
#     total_goal=data[2]
#     bonous_percent_goal=data[3]
    for i in range(0,len(data),4):

        player_name = data[i]
        yearly_income = data[i+1]
        total_goal = data[i+2]
        bonous_percent_goal = data[i+3]
        individul_bonus_calculation(player_name,yearly_income,total_goal,bonous_percent_goal)
player_bonus_calculation("Neymar", 1200000, 30, 10, "Jamal", 700000, 19, 5)

