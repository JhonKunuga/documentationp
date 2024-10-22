#                                                                   Midterm Sergo ! "
# from doctest import debug_src
# from importlib.resources import as_file
# from os import fstat
# from pstats import add_func_stats
#
# class ABC:
#     def __init__(self, string):
#         self.string = string
#
#     def abbreviation(self):
#         words = self.string.split()
#         abbr = ''
#         for word in words:
#             abbr += word[0]
#         return abbr.upper()
#
#     def reverse(self):
#         revers = self.string[::-1]
#         return revers
#
#     def trim(self, num):
#         if len(self.string) > num:
#             return self.string[:num] + "." * (len(self.string) - num)
#         else:
#             return self.string
#
#     def mydic(self):
#         result = {}
#
#         for char in self.string:
#             ascii_code = ord(char)
#
#             if char.isalpha():
#                 alpha_position = ord(char.lower()) - ord('a') + 1
#             else:
#                 alpha_position = 0
#             if ascii_code in result:
#                 if isinstance(result[ascii_code], tuple):
#                     result[ascii_code] = (alpha_position, result[ascii_code][1] + 1)
#                 else:
#                     result[ascii_code] = (alpha_position, 2)
#             else:
#                 result[ascii_code] = alpha_position
#         return result
#
#         abc = ABC("Caucasus University")
#
#         print(abc.abbreviation())
#
#         print(abc.reverse())
#
#         print(abc.trim(3))
#         print(abc`.mydic())
# from collections.abc import generator
from random import random


# #Midterm Irakli!
#
# def longest_sorted_substring(a):
#     max_substring = ""
#     current_substring = a[0]
#     for i in range(1, len(a)):
#         if a[i] >= a[i - 1]:
#             current_substring += a[i]
#         else:
#             if len(current_substring) > len(max_substring):
#                 max_substring = current_substring
#             # განაახლოთ მიმდინარე ქვესტრიქონი
#             current_substring = a[i]
#
#
#         if len(current_substring) > len(max_substring):
#                 max_substring = current_substring
#
#     return max_substring
#
# # ტესტირება
# a = "yzabdecw"
# print(longest_sorted_substring(a))  # გამოიტანოს 'abde'
# # 2
# def queue(n):
#     for i in range(1, n + 1):
#         row = ""
#         for j in range(1, i + 1):
#             row += chr(96 + j)
#         print(row)
#
# print(queue(5))
# 3

# def f(n):
#     new_tuple = ()
#     original = tuple(n)
#     for i in range(len(n)):
#         if n[i] == 'o' or n[i] == 'a':
#             new_tuple += (n[i],)
#         else:
#             continue
#
#     return print(f"თავდაპირველი კორტეჟი{original} ახალი კორტეჟი { new_tuple}  ")
#
# print(f("hello world"))
#
# import random
#
# def generate_random_numbers():
#     random_numbers = [random.randint(1, 10) for _ in range(10)]
#     return random_numbers
#
# # Call the function and print the result
# print(generate_random_numbers())
#
# s = 'yzabdecw'
# test = ''
# best = ''
# for n in range(len(s)):
#     if s[n] == 'a':
#         test = ''
#         continue
#     if n == 0 or s[n] >= s[n - 1]:
#         test += s[n]
#     else:
#         test = s[n]  # start new test substring
#     if len(test) > len(best):
#         best = test
# print("Longest substring in alphabetical order excluding 'a' is:", best)
# num_rows = int(input("Enter the number of rows: "))
# for i in range(1, num_rows + 1):
#     print("".join(chr(97 + j) for j in range(i)))
#
# epsilon = 0.01
# y = 27.0
# guess = y / 2.0
# numGuesses = 0
#
# while abs(guess ** 3 - y) >= epsilon:
#     numGuesses += 1
#     guess = guess - ((guess ** 3 - y) / (3 * guess ** 2))
#
# print('numGuesses =', numGuesses)
# print('Cube root of', y, 'is approximately', guess)

# def filter_words(input_tuple):
#     filtered_tuple = tuple(word for word in input_tuple if 'a' in word and word.startswith('m'))
#     return filtered_tuple
#
# words = ('apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'melon', 'orange', 'pear')
# result = filter_words(words)
# print(result)
# import random
# def generate_random_numbers():
#     return [random.randint(1, 100) for _ in range(10)]
#
# random_numbers = generate_random_numbers()
# print(random_numbers)
# s = 'yzabdecw'
# test = s[0]
# best = ''
# for n in range(1, len(s)):
#     if len(test) > len(best):
#         best = test
#     if s[n] >= s[n-1]:
#         test = test + s[n]
#     else:
#         test = s[n]
# print ("Longest substring in alphabetical order is:", best)
# num_rows = int(input("Enter the number of rows: "))
# for i in range(1, num_rows + 1):
#     print("".join(chr(97 + j) for j in range(i)))
#
# x = 25
# epsilon = 0.01
# num_guesses = 0
# low = 0.0
# high = x if x >= 1 else 1.0
# ans = (high + low) / 2.0
#
# while abs(ans**3 - x) >= epsilon:
#     print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
#     num_guesses += 1
#     if ans**3 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2.0
#
# print('numGuesses = ' + str(num_guesses))
# print(str(ans) + ' is close to cube root of ' + str(x))
import random
def filter_words(input_tuple):
    filtered_tuple = tuple(word for word in input_tuple if 'a' in word or 'o' in word)
    return filtered_tuple

words = ('apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'melon', 'orange', 'pear')
result = filter_words(words)
print(result)
import random
def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(10)]

random_numbers = generate_random_numbers()
print(random_numbers)
