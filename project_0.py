# Q1: 按照下面的要求，完成 function 的功能实现

# - 如果输入的 num1 和 num2 的乘积大于等于 1000，那么返回这两个数的和
# - 如果输入的 num1 和 num2 的乘积小于 1000，那么返回这两个数的乘积
def multiplication_or_sum(num1, num2):
  if num1*num2 >= 1000:
    return num1+num2
  elif num1*num2 < 1000:
    return num1*num2

# - 如果输入是偶数则返回 1，如果输入是奇数则返回 2
# - 如果输入非数字类型的参数，返回 0
def even_or_odd(n):
    if type(n) != int:
        return 0
    elif n % 2 == 0:
        return 1
    else:
        return 2

# 输入 arr 是一个数组，包含的元素为数字；现在要求计算 arr 中所有元素之和
def add_and_iterate(arr):
  return sum(arr)
# 输入 arr 是一个包含数字的数组，n 是一个输入为正整数的值；
# - 要求 输出一个数组，数组的值为 arr 中所有刚好可以整除 n 的元素，如 n 为 5 的时候，
# arr 为 [10, 12, 20]，那么要求输出为 [10, 20]
def save_divisible(arr, n):
    return [num for num in arr if num % n == 0]

# 输入 arr1 和 arr2 都是两个包含数字的数组，n 是一个正整数；
# - 检查是否 arr1 的前值为 2 的时候，
# [1, 2, 3, 4] 的前两个元素等于 [4, 1, 2] 的后两个元素，返回 True, 
# 但是不等于 [4, 3, 1] 的后两位元素，返回 False
def check_n_same(arr1, arr2, n):
  if n >= len(arr1) or n >= len(arr2):
    return False
  pre_arr1 = arr1[:n]
  suf_arr2 = arr2[-n:]

  return pre_arr1 == suf_arr2
# 输入 s 为一个字符串，要求反转这个字符串并返回
def reverse_str(s):
  return s[::-1]

# 输入 s 为一个字符串，n 为一个正整数；
# - 要求输出一个字符串，这个字符串的值为将 s 的前 n 字符移除后的结果；
# - 如果 n 大于字符串 s 的长度，返回一个空字符串
# - 如果 n 不是一个数字或是一个负数，抛出异常 TypeError
def remove_first_n_chars(s, n):
    if type(n) != int or n < 0:
        raise TypeError("n must be a non-negative integer")
    if n == 0:
        return ""

    if n >= len(s):
        return ""

    return s[n:]

if __name__ == '__main__':
  print("Hello Python")
  remove_first_n_chars("hello")

  # a=print("hello")
  # print(a)