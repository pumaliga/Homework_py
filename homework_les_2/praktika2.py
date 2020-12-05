print("""Эта программа определяет время суток.
Введите время в формате 'HH:MM'""")
time = float(input())
if time < 0 and time > 24:
	print("Неправильный ввод")
elif time >= 4 and time < 12:
	print("Сейчас утро :)")
elif time >= 12 and time < 18:
	print("Сейчас день:)") 
elif time >= 18 and time < 24:
	print("Сейчас вечер:)")
else:
	print("Сейчас ночь:)")