num1, num2, num3 = int(input()), int(input()), int(input())
for i in range(1, num3 + 1):
    if i % num1 == 0 and i % num2 == 0:
        print("FB", end = " ")
    elif i % num1 == 0:
        print("F", end = " ")
    elif i % num2 == 0:
        print("B", end = " ")
    else:
        print(i, end = " ")