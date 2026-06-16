# 1~100猜數字遊戲
# import random

# min_num = 1
# max_num = 100
# target = random.randint(min_num, max_num)
# guess_count = 0
# while True:
#     guess = int(input(f"猜測的數字是({min_num}~{max_num}):"))
#     if guess < min_num or guess > max_num:
#         print(f"超出範圍{min_num}~{max_num},請重新輸入")
#         continue
#     guess_count += 1
#     if guess == target:
#         print("恭喜你猜對了！", guess_count, "次猜中")
#         break
#     elif guess < target:
#         min_num = guess
#         print("太小了，再大一點")
#     else:
#         max_num = guess
#         print("太大了，再小一點")

# 讓用戶輸入一個整數，將其反向輸出
# input_str = input("請輸入一個整數：")
# temp = ""
# for str in input_str:
#     temp = str + temp

# print(temp)

# 讓用戶輸入一個整數 N ，列出 1 + 2 + 3 + .... x >= N
# 例如: N = 11 ，輸出 1 + 2 + 3 + 4 + 5 >= 11
# input_number = int(input("請輸入一個整數："))
# temp_number = 0
# sum = 0
# process_list = []
# while sum < input_number:
#     temp_number += 1
#     sum += temp_number
#     process_list.append(str(temp_number))
# process_string = " + ".join(process_list)
# print(process_string)
# print(f"{sum} >= {input_number}")

# 輸入一個整數值n，找出第n個質數
# num = int(input("請輸入一個整數："))
# n = 0
# while num >0:
#     n += 1
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             break
#     else:
#         num -= 1

# print(n)


# 讓用戶輸入任意數量的整數，如用戶輸入空白則表示停止
# 列出該數列，最大、最小及平均值

# input_list = []
# while True:
#     input_str = input("請輸入一個整數(空白則停止輸入)：")
#     if input_str == "":
#         break
#     input_list.append(int(input_str))
# print(input_list)
# print("最大值：", max(input_list))
# print("最小值：", min(input_list))
# print("平均值：", sum(input_list) / len(input_list))

# 亂數隨機產生10個，介於1~100之間整數值，將奇數排前，偶數排後，不用分數字大小排列
# import random

# ls = random.choices(range(1, 101), k=10)

# even_list = []
# odd_list = []
# for i in ls:
#     if i % 2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(odd_list + even_list)


# 亂數隨機產生10個，介於1~100之間整數值，只拿質數
import random

ls = random.choices(range(1, 101), k = 10)
prime_list = []
for i in ls:
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        prime_list.append(i)
print(prime_list)
