from tabulate import tabulate


def options():
    print("Choose one of the options bellow: "
          "\n* Type 1 to see all contacts "
          "\n* Type 2 to add a new contact "
          "\n* Type 3 to search a contact "
          "\n* Type 4 to edit a contact "
          "\n* Type 5 to delete a contact "
          "\n* Type 6 to import/ export "
          "\n Type 7 to close the programm \n")
    num = int(input('Input here: '))
    if 0 < num < 8:
        return num
    else:
        print('Incorrect number!')


def new_contact():
    contact = {'id': '', 'surname': input('Input surname or press "Enter": '), 'name': input('Input name: ')}
    while contact['name'] == '':
        contact['name'] = input('Input name: ')
    contact['patronymic'] = input('Input patronymic or press "Enter": ')
    contact['phone'] = input('Input phone number: ')
    while contact['phone'] == '':
        contact['phone'] = input('Input phone number: ')
    contact['comment'] = input('Type a comment or press "Enter": ') + '\n'
    return contact


def search_contact():
    print('You can search a contact by surname, name, patronymic, comment')
    search_by = input('Input here: ')
    return search_by


def make_achoice_from_list():
    contact_number = input("Input the contact's phone number You want to edit: ")
    return contact_number


def edit_contact():
    edit_the = int(input('Input 1 to change the surname \nInput 2 to change the name \nInput 3 to change the patronymic'
                         '\nInput 4 to change the phone number \n Input 5 to change the comment: '))
    while 0 > edit_the > 5:
        edit_the = int(
            input('Input 1 to change the surname \nInput 2 to change the name \nInput 3 to change the patronymic'
                  '\nInput 4 to change the phone number \n Input 5 to change the comment: '))

    if edit_the == 1:
        edit_the = 'surname'
    if edit_the == 2:
        edit_the = 'name'
    if edit_the == 3:
        edit_the = 'patronymic'
    if edit_the == 4:
        edit_the = 'phone'
    if edit_the == 5:
        edit_the = 'comment'

    return edit_the


def edit_to_val():
    edit_to = input('Input the value to overwrite the current value:')
    return edit_to


def delete_contact():
    pass


def import_export():
    pass


def show_all_data(data): # [{key:value}]
    data_to_show = []

    for i in range(len(data)):
        li = list(data[i].values())
        li.pop(0)
        data_to_show.append(li)

    params = ['Surname', 'name', 'Patronymic', 'Phone number', 'Comment']

    print(tabulate(data_to_show, headers=params, tablefmt="fancy_grid", showindex="never"))


# def show_all_data_list(data):
#     data_to_show = []
#
#     for i in range(len(data)):
#         for j in data[i]:
#             li = data[i].values()
#             li.pop(0)
#             data_to_show.append(li)
#
#     params = ["Firstname", "Lastname", "Middlename", "Phone number", "Comment"]
#
#     print(tabulate(data_to_show, headers=params, tablefmt="fancy_grid", showindex="never"))

#
# def show_all_data_list(data):
#     params = ['Surname', 'name', 'Patronymic', 'Phone number', 'Comment']
#
#     for i in range(len(data)-15):
#         li = list(data[i].values())
#         li.pop(0)
#         print(tabulate(li, headers=params, tablefmt="fancy_grid", showindex="never"))
#
