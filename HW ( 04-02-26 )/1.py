print("меню фигур")
print("1 - а")
print("2 - б")
print("3 - в")
print("4 - г")
print("5 - д")
print("6 - е")
print("7 - ж")
print("8 - з")
print("9 - и")
print("10 - к")

choice = int(input("Выберите фигуру: "))

if choice == 1:
    print("\n*        *"
          "\n**      **"
          "\n***    ***"
          "\n****  ****"
          "\n**********"
          "\n****  ****"
          "\n***    ***"
          "\n**      **"
          "\n*        *")
elif choice == 2:
    print("\n*"
          "\n**"
          "\n***"
          "\n****"
          "\n*****"
          "\n******"
          "\n*******"
          "\n********"
          "\n*********")
elif choice == 3:
    print("\n*******"
          "\n ***** "
          "\n **** "
          "\n  ***  "
          "\n   *  ")
elif choice == 4:
    print("    *      "
          "   ***    "
          "  ****   "
          "  *****  "
          " ******* "
          "*********")
elif choice == 5:
    print(""
          "*********"
          " *******"
          "  *****   "
          "  ****"
          "   *** "
          "    *      "
          "   ***    "
          "  ****   "
          "  *****  "
          " ******* "
          "*********")
elif choice == 6:
    pass
elif choice == 7:
    print("\n*"
          "\n**"
          "\n***"
          "\n****"
          "\n****"
          "\n***"
          "\n**"
          "\n*")
elif choice == 8:
    print("\n        *"
          "\n       **"
          "\n      ***"
          "\n     ****"
          "\n    *****"
          "\n     ****"
          "\n      ***"
          "\n       **"
          "\n        *")
elif choice == 9:
    pass
elif choice == 10:
    pass
else:
    exit()
