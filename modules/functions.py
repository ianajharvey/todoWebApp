FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """ Reads a text file for a to do list and return the list of items """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ Writes a list of items to a text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)