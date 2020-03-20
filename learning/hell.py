def hell(n):
    print("Welcome to Hell\n" * int(n))


def new_number():
    while True:
        try:
            number1 = int(input("Введите первое число: "))
            number2 = int(input("Введите второе число: "))
            if number2 == number1:
                raise Exception("Числа не должны быть равны")  # добавили своё собственное исключение
                continue
            print("Результат деления:", number1 / number2)
            break
        except ValueError as error:
            print("Преобразование прошло неудачно\nТип ошибки: ", error)
            continue
        except ZeroDivisionError as error:
            print("Попытка деления числа на ноль\nТип ошибки: ", error)
            continue
        except Exception as err:
            print("Общее исключение:\nТип ошибки: ", err)

        #finally: (не обязательный блок, который выполняется вне зависимости от получения ошибки

    print("Завершение программы")
