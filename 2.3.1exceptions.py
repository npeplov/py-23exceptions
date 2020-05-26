polka = input('Введите польскую нотацию: ')
polka = polka.split(' ')


def poland_annotation():
    # Если не определить переменную, то предупреждает:
    # Local variable 'polka_result' might be referenced before assignment
    polka_result = 0
    if operation == '+':
        polka_result = first + second
    elif operation == '-':
        polka_result = first - second
    elif operation == '*':
        polka_result = first * second
    elif operation == '/':
        polka_result = first / second
    return polka_result


try:
    # проверка на количество введенных аргументов
    operation = polka[0]
    first = polka[1]
    second = polka[2]

    # проверка на допустимую операцию
    assert operation == '+' or operation == '-' or operation == '*' or operation == '/', "Операция недоступна"

    # проверка на то, что операнд - число
    first = int(first)
    second = int(second)
except (AssertionError, TypeError) as e:
    print(e)
except (IndexError, TypeError) as e:
    print('Передано меньше 3х аргументов', e)
except (ValueError, TypeError) as e:
    print('Операнды должны быть числом')
else:
    try:
        print(poland_annotation())
    except (ZeroDivisionError, TypeError) as e:
        print('На ноль делить нельзя', e)