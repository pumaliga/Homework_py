file = open('Desktop/python/test.txt', 'r')
print(file.read()[::-1])
file.close()