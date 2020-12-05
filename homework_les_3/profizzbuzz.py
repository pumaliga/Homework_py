file = open('Desktop/python/numbers.txt', 'r')
for line in file:
    num = line.split()
    fizz = int(num[0])
    buzz = int(num[1])
    stop = int(num[2])
    result = open('Desktop/python/result.txt', 'a')
    result.write('Значние для:\n')
    result.write(line)
    for _ in range(1, stop + 1):
        if _ % fizz == 0 and _ % buzz == 0:
            result.write('FB\n')
        elif _ % fizz == 0:
        	result.write('F\n')
        elif _ % buzz == 0:
        	result.write('B\n')
        else:
            result.write(str(_) + str('\n'))
file.close()     	
