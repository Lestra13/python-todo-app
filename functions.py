FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Cita iz tekst fajla i vraca listu stavki"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Pise odnosno dodaje stavku/stavke u listu i a zatim u tekst fajl"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print((get_todos()))
