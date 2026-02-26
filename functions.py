def get_todos(f="todos.txt"):
    with open(f,"r") as file:
        todos=file.readlines()
    return todos
def write_todos(argg,f="todos.txt"):
    with open(f,"w") as file:
        file.writelines(argg)
