# def add(args):
#     print(args)
#     addition = 0
#     addition += int(args)
#     return addition
#
# def  sub(*args):
#     division = 0
#     division -= args
#     return division
#
# def mul(*args):
#     multi = 1
#     multi *= args
#     return multi
#
# print("1.addition")
# print("2.substraction")
# print("3.multiplication")
# num = int(input("Enter your choice:"))
# if num == 1:
#     args = input("Enter Nubers by comma separated:")
#     add(args)
# elif num == 2:
#     sub()
# elif num == 3:
#     mul()
# else:
#     print("Invalid Input")
#
# ----------------------------------------------------
import csv

#
# def add(a, b):
#     return a + b
#
#
# def mul(a, b):
#     return a * b
#
#
# def sub(a, b):
#     return a - b
#
#
# def div(a, b):
#     try:
#         print("div:", a // b)
#
#     # division = a // b
#     # return a // b
#
#     except ZeroDivisionError:
#         if b == 0:
#             print("Please enter None than zero")
#
#
# print("1.Addition")
# print("2.Multiplication")
# print("3.Substraction")
# print("4.Division")
# choice = input("Enter your choice:")
# a = input("Enter First Number:")
# b = input("Enter Second Number:")
# try:
#     choice = int(choice)
#     l = int(a)
#     m = int(b)
#
# except Exception:
#     raise ValueError("Enter valid number:")
#
# if choice == 1:
#     print(add(a, b))
# elif choice == 2:
#     print(mul(a, b))
# elif choice == 3:
#     print(sub(a, b))
# elif choice == 4:
#     print(div(a, b))
# else:
#     print("Invalid Input")

# def add(a,b,c=9):
#     print("a:", a)
#     print("b:", b)
#     a=a
#     b=b
#     return a,b,c
#
# a,b,c = add(a=1,b=2)
# print("a:", a)
# print("b:", b)
# print("c:", c)


# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""
#
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
#
#
# num = 6
# print("The factorial of", num, "is", factorial(num))

# sum = lambda a,b : a + b
# print(sum(2,3))

# a = "pqr"
# def mess():
#     global a
#     a = "abc"
#     print(a)
#
# mess()
# print(a)

# global variable
c = 1

# def add():
#     b = c + 2
#     print(b)
#     print(c)
#
# add()
# print(c)

# import csv
# with open('emp.txt', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     rows = []
#     for row in reader:
#         rows.append(row)
#         print(row)
#     with open("Emp_data.csv", "w", newline="") as csv_write:
#         headers = rows[0].keys()
#         writer = csv.DictWriter(csv_write, fieldnames= headers)
#         writer.writeheader()
#         writer.writerows(rows)

# import csv
# for row in csv.reader(['one,two,three']):
#     print(row)

#department data(print list of string)
# import csv
# with open('department.csv','r', newline='' ) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(', '.join(row))

#tab delimeter
# import csv
# with open('countries.csv', newline='') as csvfile:
#      data = csv.reader(csvfile, delimiter = '\t')
#      for row in data:
#         print(', '.join(row))

# to show specific columns from csv file
# import csv
# with open('department.csv','r', newline='') as f:
#     data = csv.DictReader(f)
#     for row in data:
#         print(row['department_name'], row['location_id'])

#Write a Python program that reads each row of a given csv file and skip the header of the file.
# Also print the number of rows and the field names.
# fields = []
# rows = []
# with open('department.csv','r', newline='') as f:
#     reader = csv.reader(f)
#     cnt = 0
#     fields =next(reader)
#     for row in reader:
#         print(row)
#         cnt += 1
# print("rows count including header:", reader.line_num)
# print("rows count without header:", cnt)
# # print(fields)
# print("Fields are :"+', '.join (field for field in fields))






