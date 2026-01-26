A = int(input("число A: "))
N = int(input("степень N: "))

result = 1
i = 0

while i < N:
    result = result * A
    i += 1

print("А в степени N--->", result)
