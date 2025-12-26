# print("hello")
# """a = 20
# if a%2 == 0:
#     print('even')
# else:
#     print('odd')"""


# """l=10
# b=20
# area = l*b
# print(area)"""

# """a = int(input("Enter number = "  ))
# if a<0:
#     print("negative")
# elif a>0:
#     print("positive")
# else:
#     print("zero")"""

# """side = int(input("enter number = "))
# area = side * side
# print(area)"""


# """a=int(input("enter a number "))
# for a in range(a, 11):
#     print(a)
# """a=int(input("Enter a number" ))
# while a<=10:
#     print(a)
#     a = a+1"""
# """age = 22
# print(age)

# cost=22.02
# print(type(cost))"""

# a=input("Enter a number =" )
# print(int(a))

# b = int(input("Enter a number :"))
# if b<=0:
#     print("Negative")
# else:
#     print("positive")

# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
# a=int(input("enter a number: " ))
# if a >= 40:
#     print("Pass")
# else:
#     print("fail")

# i=0
# for i in range(1,11):
#     print(i)
# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i=i+1
# sum =0
# for i in range(1,6):
#     sum += i
# print(sum)
# i=10
# while i>=1:
#     print(i)
#     i=i-1


# i=1
# while i<=10:
#     mul = 5*i
#     print(mul)
#     i= i+1


# for i in range(1,51):
#     print(i)

# i=50
# while i>=1:
#     print(i)
#     i=i-1

# i=1
# while i <= 20:
#     if i % 2 == 1:
#         print(i)
#     i=i+1
# count = 0
# for i in range(1, 101):
#     count += 1
# print(count)

# i=30
# while i >= 1:
#     if i%3 == 0 and i%5 == 0:
#         print("FissBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)
#     i= i-1


# count = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         count += 1
# print(count)



# i = 20
# while i >= 1:
#     if i % 4 == 0:
#         i -= 1
#         continue
#     else:
#         print(i)
#     i= i-1
# i=1
# even = 0
# odd = 0
# while i <= 20:
#     if i % 2 ==0:
#         even += 1
#     else:
#         i % 2 == 1
#         odd += 1
#     i= i+1
# print(f"Even: {even} ,Odd: {odd}")

# n = int(input("Enter a number : "))
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10+ digit
#     n = n//10
# print(reverse)

# num = int(input("enter a number: "))
# temp = num
# rev = 0
# while num >0:
#     digit = num %10
#     rev = rev *10+digit
#     num = num//10
# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# num =5
# fact = 1
# while num >0:
#     fact = fact * num
#     num = num - 1
# print(fact)

# num =4587
# count = 0
# while num > 0:
#     count = count +1
#     num = num // 10
# print(count)


# n=[1,2,3,4,5]
# for i in n:
#     print(n)
# first = n[0]
# print(first)
# last = n[-1]
# print(last)

# n = [1,2,3,4,5]
# n.append(6)
# n.remove(4)
# print(len(n))
# print(n)


# n=[1,2,3,4,5]
# for i in n:
#     if i % 2 == 0:
#         print(i)



# n = (1,2,3,4,5)
# m = 2
# if m in n:
#     print(f"{m} in tuple")


# n= int(input("Enter a number : "))
# m= int(input("Enter a number : "))
# p= int(input("Enter a number : "))
# q= int(input("Enter a number : "))
# r= int(input("Enter a number : "))
# my_list = [n,m,p,q,r]
# sum = n+m+p+q+r
# print(sum)

# n = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     n.append(num)
# total = sum(n)
# print(total)


# n = (1,2,3,4,5)
# m= 5
# if m in n:
#     print(f"{m} in tuple")

# def name():
#     print("sneha")
# name()




# s = input()
# print("Palindrome" if s == s[::-1] else "Not Palindrome")



# print("hello world")


# def print_name():
#     print("Sneha")
# print_name()

# def sum_two(a,b):
#     print(a+b)
# sum_two(20,10)

# numbers = [1,2,3,4,5]
# print(numbers)
# print(numbers[0])
# print(numbers[-1])

# def check_number(n):
#     if n >= 0:
#         print("positive")
#     else:
#         print("negative")
# check_number(-4)


# def square(n):
#     return n*n
# print(square(6))

# def check(n):
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# check(5)

# def number(n):
#     return n
# print(number(6))


# def print_list(lst):
#     for item in lst:
#         print(item)
# print_list([10,20,30,40])

# def count_elements(lst):
#     count = 0
#     for _ in lst:
#         count += 1
#     return count

# print(count_elements([1, 2, 3, 4]))

# def count_elements(lst):
#     count = 0
#     for _ in lst:
#         count += 1
#     return count
# print(count_elements([1,2,3,4,5,5]))

# def add_element(lst, value):
#     lst.append(value)
#     return lst
# print(add_element([1,2,3,4], 5))

# def list_sum(lst):
#     total=0
#     for num in lst:
#         total+=num
#     return total
# print(list_sum([1,2,3,4,5]))

# def list_sum(lst):
#     total=0
#     count = 0
#     for num in lst:
#         total+=num
#         count+=1
#     return total/count
# print(list_sum([1,2,3,4,5]))


# def exists(lst, value):
#     for item in lst:
#         if item ==value:
#             return True
#     return False
# print(exists([1, 2, 3], 2))

# def remove_lst(lst):
#     new_lst=[]
#     for item in lst:
#         if item not in new_lst:
#             new_lst.append(item)
#     return new_lst
# print(remove_lst([1,2,3,4,3,2,1]))

# def rev_num(lst):
#     rev =[]
#     for i in range(len(lst)-1,-1,-1):
#         rev.append(lst[i])
#     return rev
# print(rev_num([1,2,3,5,4]))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(is_prime(6))
print(is_prime(7))

