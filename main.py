import sys

max_number_of_cases = 80
max_range = 80

number_of_cases = int(input())
if number_of_cases < 1 or number_of_cases > max_number_of_cases:
    sys.exit(0)

palindromes = []
#
def is_palindrome(user_number):
    if str(user_number) == str(user_number)[::-1]:
        return True
    else:
        return False
#
# repeat_counter = 0
# def calulate_palindrome(user_number):
#
#     if is_palindrome(user_number):
#         palindromes.append([user_number, repeat_counter])
#     else:
#


for i in range(0, number_of_cases):
    user_number = int(input())
    if user_number < 1 or user_number > max_range:
        sys.exit(0)

    temp_result = 0
    repeat_counter = 0
    if is_palindrome(user_number):
        palindromes.append([user_number, 0])
    else:
        while True:
            repeat_counter += 1
            user_number = user_number + int(str(user_number)[::-1])
            if is_palindrome(user_number):
                palindromes.append([user_number, repeat_counter])
                break

for i in palindromes:
    print(i[0], i[1])
