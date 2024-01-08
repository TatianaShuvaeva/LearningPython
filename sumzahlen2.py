numbers = [int(i) for i in input().split()]
if len(numbers) == 1:
    print(numbers[0])
else:
    for i in range(len(numbers)):
        print(numbers[i - 1] + numbers[(i + 1) % len(numbers)], end=" ")