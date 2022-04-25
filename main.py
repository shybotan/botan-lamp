import time


class Book:

    def __init__(self, id_, name_, author_, publisher_, section_, status_, mark_):
        self.id = id_
        self.name = name_
        self.author = author_
        self.publisher = publisher_
        self.section = section_
        self.status = status_
        self.mark = mark_

    def __repr__(self):
        return f"ID: {self.id} \
        Name: {self.name} \
        Аuthor: {self.author} \
        Publisher: {self.publisher}\
        Section: {self.section}\
        Status: {self.status} \
        Mark: {self.mark}\n"


def show(library):
    a = int(input("по чему хотите вывести книги?\n 1 автор \n 2 раздел \n 3 наличие \n"))
    if a == 1:
        author_ = input("Введите автора книги \n")
        for book in library:
            if book.author == author_:
                print(book)
    elif a == 2:
        section_ = input("Введите раздел книги \n")
        for book in library:
            if book.section == section_:
                print(book)
    elif a == 3:
        status_ = int(input("Введите наличие книги \n"))
        for book in library:
            if book.status == status_:
                print(book)
    else:
        print("Вы ввели не допустимое число, ошибка")
        time.sleep(2)
        return library


def edit(library):
    show(library)
    id_ = int(input("Введите номер книги \n"))
    for book in library:
        if book.id == id_:
            a = int(input("Какой пункт хотите исправить \n"))
            if a == 1:
                book.name = input("Введите название книги \n")
            elif a == 2:
                book.author = input("Введите автора книги \n")
            elif a == 3:
                book.publisher = input("Введите издательство книги \n")
            elif a == 4:
                book.section = input("Введите раздел книги \n")
            elif a == 5:
                book.status = input("Введите статус книги \n")
            elif a == 6:
                book.mark = input("Введите оценку \n")
            else:
                print("Вы ввели не допустимое число, ошибка")
                time.sleep(2)
                return library
            return library
    print("Не нашли книгу в библиотеке")
    return(library)


def add(library):
    id_ = int(input("Введите номер книги \n"))
    for book in library:
        if book.id == id_:
            print("Ошибка")
            return library
    name = input("Введите название книги \n")
    author = input("Введите автора книги \n")
    publisher = input("Введите издательство \n")
    section = input("Введите раздел \n")
    status = input("Введите статус \n")
    mark = input("Введите оценку \n")
    book = Book(id_, name, author, publisher, section, status, mark)
    library.append(book)
    time.sleep(2)
    return library


def delete(library):
    id_ = int(input("Введите номер книги \n"))
    for book in library:
        if book.id == id_:
            library.remove(book)
            continue
    return library


def import_from(library):
    pass


def export_to(library):
    pass


if __name__ == '__main__':
    book1 = Book(1, 'Гарри Поттер1', 'Роулин', 'АСТ', 'фантастика', 1, 'Хорошо')
    book2 = Book(2, 'Гарри Поттер2', 'Роулин', 'АСТ', 'фантастика', 2, 'Хорошо')
    book3 = Book(3, 'Гарри Поттер3', 'Роулин', 'АСТ', 'фантастика', 1, 'Средне')
    book4 = Book(4, 'Маленький принц', 'Антуан де Сент-Экзюпери', 'АСТ', 'повесть', 1, 'Отлично')

    library = [book1, book2, book3, book4]
    while True:
        print('1 Вывод книг \n'
              '2 Редактирование записи \n'
              '3 Добавление книги \n'
              '4 Удаление книги \n'
              '5 Загрузка из файла \n'
              '6 Сохранение в файл \n')
        a = int(input("Введите целое число: "))
        time.sleep(2)
        if a == 1:
            show(library)
        elif a == 2:
            edit(library)
        elif a == 3:
            library = add(library)
        elif a == 4:
            library = delete(library)
        elif a == 5:
            import_from(library)
        elif a == 6:
            export_to(library)
        else:
            print("Вы ввели не допустимое число, ошибка")
            time.sleep(2)
    print(library)