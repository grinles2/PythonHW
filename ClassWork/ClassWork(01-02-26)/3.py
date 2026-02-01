N = int(input("N число--> "))

max_num = None

for i in range(N):
    num = int(input("число: "))

    if max_num is None or num > max_num:
        max_num = num

print("max:", max_num)
