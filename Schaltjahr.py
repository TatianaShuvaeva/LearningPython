N = int(input())
if N%4==0 and N%100!=0 or N%400==0:
    print('Високосный')
else:
    print('Обычный')