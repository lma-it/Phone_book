# Написать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находится в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например фамилия, имя или номер телефона)
# 4. Использование функций чтоб программа не была линейной, а содержала меню.

# ДЗ. 

import ast

still_work = True
'''
Переменная, которая необходима для выхода из цикла программы, если ее значение будет False
''' 
file = 'phone_book.txt'
'''
Путь к файлу с контактами
'''
temp_file = 'deleted_contacts.txt'
'''
Путь к файлу с удаленными контактами
'''
contact = {'Name': '', 'Surname': '', 'Second name': '', 'phone': 0}
'''
Шаблон словаря для контакта
'''
phone_book = []
'''
Список в котором будут храниться словари с контактами
'''
deleted_contacts = []
'''
Список для временного хранения удаленных контактов.
'''
copy_contacts = []
'''
Список для хранения экспортированных контактов
'''


def menu(phone_book, deleted_contacts):
    '''
    Главное меню приложения, в котором можно выбрать действие необходимое выполнить в приложении

    Args:
        phone_book: Список в котором храняться словари с контактами.
        Шаблон словаря: contact = {'Name': '', 'Surname': '', 'Second name': '', 'phone': 0}
    '''
    global still_work
    print("1. Enter 1 if you want search contacts by name.")
    print("2. Enter 2 if you want search contacts by surname.")
    print("3. Enter 3 if you want search contacts by second name.")
    print("4. Enter 4 if you want search contacts by phone.")
    print("5. Enter 5 if you want add a new contact.")
    print("6. Enter 6 if you want see all of your contacts.")
    print("7. Enter 7 if you want edit contact.")
    print("8. Enter 8 if you want DELETE the contact.")
    if len(deleted_contacts) > 0:
        print("0. Enter 0 if you want RESTORE deleted contact.")
    print("9. Enter 9 if you want export contacts in new file.")
    option = int(input("10. Enter 10 if you want exit programm. Enter number of your choise: "))
    
    if option == 1:
        return get_contact_by_name(phone_book)
    elif option == 2:
        return get_contact_by_surname(phone_book)
    elif option == 3:
        return get_contact_by_second_name(phone_book)
    elif option == 4:
        return get_contact_by_phone(phone_book)
    elif option == 5:
        return set_contact(phone_book)
    elif option == 6:
        return view_all_contacts(phone_book)
    elif option == 7:
        return edit_contact(phone_book)
    elif option == 8:
        return delete_contact(phone_book, deleted_contacts)
    elif option == 0:
        return restore_deleted_contacts(deleted_contacts, phone_book)
    elif option == 9:
        return copy_contact(phone_book, copy_contacts)
    elif option == 10:  
        still_work = False
    

def edit_contact(phone_book):
    '''
    Функция которая позволяет изменить существующий контакт

    Args:
        phone_book: Список в котором храняться словари с контактами
    '''
    name = input("Enter the name of contact wich you want edit: ")
    index = 0
    for contact in phone_book:
        if name == contact['Name']:
            print(f"Choose what you want edit in contact: {contact}")
            print("1. Enter 1 if you want edit Name")
            print("2. Enter 2 if you want edit Surnaname")
            print("3. Enter 3 if you want edit Second Name")
            print("4. Enter 4 if you want edit phone")
            print("5. Enter 5 if you want skip this contact")
            option = int(input("6. Enter 6 if you want exit. Enter your number: "))

            if option == 1:
                contact['Name'] = input("Enter new Name: ")
            elif option == 2:
                contact['Surname'] = input("Enter new Surname: ")
            elif option == 3:
                contact['Second name'] = input("Enter new Second Name: ")
            elif option == 4:
                contact['phone'] = input("Enter new phone number: ")
            elif option == 5:
                index += 1
                continue
            elif option == 6:
                break
        index += 1


def load_contacs(file, phone_book):
    '''
    Функция, которая загружает все контакты в список перед началом работы программы

    Args:
        file: Путь к файлу, из которого идет чтение контактов
        phone_book: Список всех контактов в котором храняться словари с контактами
    '''
    data = open(file, 'r', encoding="UTF-8")
    if data != None:
        for line in data:
            contact = ast.literal_eval(line)
            phone_book.append(contact)
        data.close()
    else:
        data.close()


def get_contact_by_name(phone_book):
    '''
    Выводит в консоль все контакты с которыми есть совпадения по введеному имени

    Args:
        phone_book: Список в котором храняться словари с контактами.
    '''
    name = input("Enter the Name in format: Name ")
    for contact in phone_book:
        if name == contact['Name']:
            print(contact['Surname'], contact['Name'], contact['Second name'], contact['phone'])
    

def get_contact_by_surname(phone_book):
    '''
    Выводит в консоль все контакты с которыми есть совпадения по введеной фамилии

    Args:
        phone_book: Список в котором храняться словари с контактами.
    '''
    surname = input("Enter the Surname in format: Surname ")
    for contact in phone_book:
        if surname == contact['Surname']:
            print(contact['Surname'], contact['Name'], contact['Second name'], contact['phone'])


def get_contact_by_phone(phone_book):
    '''
    Выводит в консоль контакт с которым есть совпадение по введеному номеру телефона

    Args:
        phone_book: Список в котором храняться словари с контактами.
    '''
    phone = input("Enter the phone wich you want find: ")
    for contact in phone_book:
        if phone in contact:
            print(contact['Surname'], contact['Name'], contact['Second name'], contact['phone'])


def get_contact_by_second_name(phone_book):
    '''
    Выводит в консоль все контакты с которыми есть совпадение по введеному отчеству

    Args:
        phone_book: Список в котором храняться словари с контактами.
    '''
    second_name = input("Enter the Second Name in format: Second name ")
    for contact in phone_book:
        if second_name in contact['Second name']:
            print(contact['Surname'], contact['Name'], contact['Second name'], contact['phone'])


def set_contact(phone_book):
    '''
    Функция добавляет в список контактов новый контакт, если совпадений с уже существующими контактами нет.

    Args:
        phone_book: Список в котором храняться словари с контактами.
    '''
    new_contact = dict(contact)
    new_contact['Name'] = input("Enter Name of contact: ")
    new_contact['Surname'] = input("Enter Surname of contact: ")
    new_contact['Second name'] = input("Enter Second Name of contact: ")
    new_contact['phone'] = input("Enter phone of contact: ")
    if new_contact not in phone_book:
        phone_book.append(new_contact)


def save_file(phone_book, file):
    '''
    Функция сохраняет все контакты в файл (БД).

    Args:
        phone_book: Список в котором храняться словари с контактами.

        file: Путь к файлу, в который необходимо сохранить контакты.
    '''
    data = open(file, 'w', encoding="UTF-8")
    for contact in phone_book:
        data.write(str(contact) + '\n')
    data.close()


def view_all_contacts(phone_book):
    '''
    Функция выводит в консоль все контакты которые имеются в списке phone_book

    Args:
        phone_book: Список в которм храняться словари с контактами
    '''
    for contact in phone_book:
        print(contact['Surname'], contact['Name'], contact['Second name'], contact['phone'])


def isContinue():
    '''
    Функция, которая запрашивает у пользователя желает ли он продолжить использование программы, чтоб избежать бесконечного вывода всего меню в консоль. Если "Да", то программа заново выводит меню, если "Нет", то программа завершается.
    '''
    global still_work
    option = input("Do you want open main menu? Set 'y' if you want, or 'n' if you don't. ")
    if option == 'y':
        still_work = True
    elif option == 'n':
        still_work = False


def delete_contact(phone_book, deleted_contacts):
    '''
    Функция удаляет существующий контакт, с возможностью прервать процесс удаления.

    Args:
        phone_book: Список со словарями контактов
    '''
    name = input("Enter the name of contact wich you want to remove from a book: ")
    surname = input("Enter the surname of contact wich you want to remove from a book: ")
    index = 0
    for contact in phone_book:
        if name == contact['Name'] and surname == contact['Surname']:
            print(f"Do you still want to delete the contact: {contact}?")
            answer = input("Enter 'y' if you want, or 'n' if you don't: ")
            if answer == 'y':
                deleted_contacts.append(phone_book.pop(index))
                index += 1
            elif answer == 'n':
                index += 1
                continue
        index += 1


def restore_deleted_contacts(deleted_contacts, phone_book):
    '''
    Функция позволяет восстановить удаленные контакты.

    Args:
        deleted_contacts: Список с удаленными контактами.
        phone_book: Список в котором храняться контакты. 
    '''
    name = input("Enter the name of contact wich you want restore: ")
    index = 0
    for contact in deleted_contacts:
        if name == contact['Name']:
            print(f"Do you still want restore the {contact} contact?")
            answer = input("Enter 'y' if Yes, or 'n' if No. ")
            if answer == 'y':
                phone_book.append(contact)
                deleted_contacts.pop(index)
                index += 1
            elif answer == 'n':
                index += 1
                continue
        index += 1


def copy_contact(phone_book, copy_contacts):
    '''
    Функция которая позволяет копировать контакты или контакт в отдельный файл.

    Args:
        phone_book: Список всех контактов 
        copy_contacts: Список копирванных контактов.
    '''
    still_copy = True
    isShow = True
    while still_copy == True:
        index = 1
        if isShow:
            print("That is all of yours contacts: ")
            for contact in phone_book:
                print(f"{index}. {contact['Surname']} {contact['Name']} {contact['Second name']} {contact['phone']}")
                index += 1
        index = int(input("Enter number of contact wich you want to export in file: "))
        copy_contacts.append(phone_book[index - 1])
        answer = input("Do you want continue export? Enter 'y' if Yes, or 'n' if No: ")
        if answer == 'y':
            show_again = input("Do you want see all of your contacts again? Enter 'y' if Yes, or 'n' if No: ")
            if show_again == 'y':
                index = 1
                if isShow == True:
                    isShow = False
                else:
                    isShow = True
                for contact in phone_book:
                    print(f"{index}. {contact['Surname']} {contact['Name']} {contact['Second name']} {contact['phone']}")
                    index += 1
            elif show_again == 'n':
                isShow = False
                continue
        elif answer == 'n':
            still_copy = False
            if len(copy_contacts) == 1:
                data = open(f"{copy_contacts[0]['Name']}_{copy_contacts[0]['Surname']}.txt", 'a', encoding="UTF-8")
                for contact in copy_contacts:
                    data.write(str(contact) + '\n')
                data.close()
            else:
                data = open("copy_of_contacts.txt", 'a', encoding="UTF-8")
                for contact in copy_contacts:
                    data.write(str(contact) + '\n')
                data.close()


# PROGRAMM BLOCK
load_contacs(file, phone_book)
load_contacs(temp_file, deleted_contacts)

while still_work:
    menu(phone_book, deleted_contacts)
    if still_work == True:
        isContinue()

save_file(phone_book, file)
save_file(deleted_contacts, temp_file)