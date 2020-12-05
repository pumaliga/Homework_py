UAH50, UAH100, UAH200, UAH500, UAH1000 = 0, 0, 0, 0, 0
print("Введите сумму кратную 50")
sum = int(input())
if sum % 50 != 0:
	print("Неправильная сумма")
elif sum % 50 == 0:
	while sum >= 1000:
		UAH1000 += 1
		sum -= 1000
	while sum >= 500:
		UAH500 += 1
		sum -= 500
	while sum >= 200:
		UAH200 += 1
		sum -= 200
	while sum >= 100:
		UAH100 += 1
		sum -= 100
	while sum >= 50:
		UAH50 += 1
		sum -= 50
	print("Итого к выдаче:", "\n", "UAH1000:", UAH1000, "\n", "UAH500:", UAH500, "\n", "UAH200:", UAH200, "\n", "UAH100:", UAH100, "\n", "UAH50:", UAH50)
