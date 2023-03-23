def format_data(data, sep):
    separated_data = ' '
    for i in data:
        separated_data += sep.join(i.values())
    return separated_data


def write_data(data, path):
    with open(path, 'w', encoding="utf-8") as file:
        file.write(format_data(data, ";"))
    with open("dataBase.txt", "w", encoding="utf-8") as file:
        file.write(format_data(data, "::"))


def remove_data(data, path, delete):

    data = [i for i in data for j in i.values if j['phone'] != delete]
    write_data(data, path)
