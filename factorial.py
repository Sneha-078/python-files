# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# print(factorial(3))

# def count_vowels(s):
#     count = 0
#     for ch in s:
#         if ch.lower() in "aeiou":
#             count += 1
#     return count
# print(count_vowels("aeiou"))

# def reverse_num(n):
#     rev = 0
#     while n> 0:
#         rev = rev *10 + n%10
#         n//=10
#     return rev
# print(reverse_num(34567))

# x = 10
# def num(x):
#     return x
# print(num(x))


# def num():
#     y = 20
#     print(y)
# num()
# a = [1, 2, 3]
# a.remove(2)
# print(a)
# a = [1, 2, 3]
# a.pop()
# print(a)
# a = [10, 20, 30]
# print(len(a))

# l= [1,2,3,]
# t=tuple(l)
# print(t)

# with out using reverse
# nums=[1,2,3,4]
# reverse = nums[::-1]
# print(reverse)

nums = [1,2,3,4,3,2,]
duplicates =[]
for n in nums:
    if nums.count(n) > 1 and n not in duplicates:
         duplicates.append(n)
print(duplicates)

# unique = [1,2,3,4,5,4,3,2,]
# for n in unique:
#     if n not in duplicates