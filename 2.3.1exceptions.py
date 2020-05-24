polka = input('Введите польскую нотацию:')
polka = polka.split(' ')


def poland_annotation():
    if operation == '+':
        polka_result = first + second
    elif operation == '-':
        polka_result = first - second
    elif operation == '*':
        polka_result = first * second
    elif operation == '/':
        try:
            polka_result = first / second
        # except (ZeroDivisionError, TypeError) as e:
        except Exception as e:
            polka_result = 'На ноль делить нельзя - ' + str(e)
    print(f'Результат: {polka_result}')


try:
    operation, first, second = polka
except (Exception, TypeError) as e:
    print('Передано меньше 3х аргументов')
else:
    try:
        first = int(first)
        second = int(second)
    except (Exception, TypeError) as e:
        print('Операнды должны быть числом')
    else:
        try:
            assert operation == '+' or operation == '-' or operation == '*' or operation == '/', "Операция недоступна"
        except Exception as e:
            print(e)
        else:
            poland_annotation()