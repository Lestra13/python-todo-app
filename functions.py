FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    eng: Reads todos from a text file, and returns them in a list
    srb:Cita iz tekst fajla i vraca listu stavki"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    eng: Writes, appends todos to a text file
    srb:Pise odnosno dodaje stavku/stavke u tekst fajl
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print((get_todos()))
