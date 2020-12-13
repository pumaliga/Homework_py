XXS = {"Russia": 42, "Germany": 36, "USA": 8, "France": 38, "Great Britain": 24}
XS = {"Russia": 44, "Germany": 38, "USA": 10, "France": 40, "Great Britain": 26}
S = {"Russia": 46, "Germany": 40, "USA": 12, "France": 42, "Great Britain": 28}
M = {"Russia": 48, "Germany": 42, "USA": 14, "France": 44, "Great Britain": 30}
L = {"Russia": 50, "Germany": 44, "USA": 16, "France": 46, "Great Britain": 32}
XL = {"Russia": 52, "Germany": 46, "USA": 18, "France": 48, "Great Britain":34}
XXL = {"Russia": 44, "Germany": 48, "USA": 20, "France": 50, "Great Britain": 36}
XXXL = {"Russia": 46, "Germany": 50, "USA": 22, "France": 52, "Great Britain": 38}
def prikid(value):
	if value == XXS:
		return XXS
	elif value == XS:
		return XS
	elif value == S:
		return S
	elif value == M:
		return M
	elif value == L:
		return L
	elif value == XL:
		return XL
	elif value == XXL:
		return XXL
	elif value == XXXL:
		return XXXL

print(prikid(L))