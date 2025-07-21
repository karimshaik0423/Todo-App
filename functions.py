FILEPATH = "todo.txt"
def get_todos (filepath=FILEPATH):
    """Read a text file and return the list of
    to do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todo_arg, filepath=FILEPATH):
    """Write a text file and return the list of
        to do items"""
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())