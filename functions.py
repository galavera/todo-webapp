FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    # This is a context manager
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file. """  # this is a doc string
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


#   use this to only run code locally and not when imported
if __name__ == "__main__":
    print("something random")
