try: # Для перестраховки)
    first = int(input("Введите первое число - "))
    second = int(input("Введите второе число - "))
    third = int(input("Введите третье число - "))
    if first == second == third:
        print("Одинаковых чисел - 3")
    elif first == second or first == third or second == third:
        print("Одинаковых чисел - 2")
    else:
        print("Одинаковых чисел - 0")
except ValueError:
    print("Вы ввели неверное значение!")

