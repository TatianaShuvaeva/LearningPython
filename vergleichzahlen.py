# numbers = [int(i) for i in input().split()]
# numbers.sort()

# i=0
# while i < len(numbers) - 1:
#     count = 1
#     while i < len(numbers) - 1 and numbers[i] == numbers[i + 1]:
#         count += 1
#         i += 1

#     if count > 1:
#         print(numbers[i], end=' ')
#     i += 1


numbers = [int(i) for i in input().split()]
numbers.sort()

prev_num = None
for num in numbers:
    if num == prev_num:
        continue

    count = numbers.count(num)
    if count > 1:
        print(num, end=' ')

    prev_num = num