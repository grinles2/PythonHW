def is_symmetric(list):
    if len(list) <= 1:
        return True
    if list[0] != list[-1]:
        return False
    return is_symmetric(list[1:-1])


list_user = list(map(int, input("Введите числа (ЧЕРЕЗ ПРОБЕЛ) -> ").split()))
list = list_user
if is_symmetric(list):
    print("Симетричный")
else:
    print("Не симетричный")