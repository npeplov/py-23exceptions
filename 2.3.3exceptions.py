documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people():
    # p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    document_number = input('Номер документа: ')
    for document in documents:
        if document["number"] == document_number:
            name = document["name"]
            return name


def shelf():
    # s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    document_number = input('Номер документа: ')
    for shelf_number, document in directories.items():
        if document_number in document:
            print('Документ на полке №', shelf_number)
            return
    print('Нет такого документа')


def documents_list():
    # l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    for document in documents:
        print(document["number"], document["name"])


def add_document():
    # a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    document_number = input('Номер документа: ')
    document_type = input('Тип ')
    document_owner_name = input('Имя владельца: ')
    document_shelf_number = input('Номер полки: ')
    try:
        documents.append({'type': document_type, 'number': document_number, 'name': document_owner_name})
        directories[document_shelf_number].append(document_number)
        print('Документ добавлен')
        print(documents, directories, sep='\n', end='\n')
    except KeyError as e:
        print(e)
        print('Введен неверный номер полки')

    # if document_shelf_number in directories.keys():
    #     documents.append({'type': document_type, 'number': document_number, 'name': document_owner_name})
    #     directories[document_shelf_number].append(document_number)
    #     print('Документ добавлен')
    #     print(documents, directories, sep='\n', end='\n')
    # else:
    #     print('Введен неверный номер полки')


def del_document():
    # d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
    counter = 0
    document_number = input('Номер документа: ')
    for shelf_number, document in directories.items():
        if document_number in document:
            del directories[shelf_number][directories[shelf_number].index(document_number)]
            for document in documents:
                # print ('Словарь document: ', document, '\n', 'counter: ', counter, ' number: ', document["number"], '\ndocuments[counter]:', documents[counter], sep='')
                if document["number"] == document_number:
                    del documents[counter]
                counter = counter + 1
            print(f'Документ {document_number} удален: \n{documents} \n{directories}')
            return
    print(f'Нет документа с номером {document_number}')


def move_document_to_shelf():
    # m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
    # document_number = input('Номер документа: ')
    document_number = input('Номер документа: ')
    for documents_on_shelf in directories.values():
        if document_number in documents_on_shelf:
            break
        else:
            print(f'Нет документа с номером {document_number}')
            return
    target_shelf_number = input('Номер полки: ')
    if target_shelf_number not in directories.keys():
        print(f'Полки с номером {target_shelf_number} не существует')
        return
    for shelf_number, doc_numbers in directories.items():
        if document_number in doc_numbers:
            i = doc_numbers.index(document_number)
            directories[shelf_number].pop(i)
            directories[target_shelf_number].append(document_number)
            print(f'Документ {document_number} перенесен на {target_shelf_number}-ю полку: \n{directories}')
            return
        break


def add_shelf():
    # as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
    target_shelf_number = input('Номер полки: ')
    for shelf_number in directories.keys():
        if shelf_number == target_shelf_number:
            print(f'Полка с номером {target_shelf_number} уже существует')
            return
    directories[target_shelf_number] = []
    print(directories)


def input_command():
    command = input('Введите команду: ')
    if command == 'p':
        print(people())
    elif command == 's':
        shelf()
    elif command == 'l':
        documents_list()
    elif command == 'a':
        add_document()
    elif command == 'd':
        del_document()
    elif command == 'm':
        move_document_to_shelf()
    elif command == 'as':
        add_shelf()


while True:
    input_command()