import click


@click.command()
@click.option('--name', prompt="Enter your name", help="Enter your name")
def hello(name):
    click.echo(f"hello {name}")

PRIORITIES = {
    "o" : "Optional",
    "l" : "low",
    "m" : "medium",
    "h" : "high"
}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=0)
@click.option('--name', prompt="Enter the name of the todo item", help="Enter the name of your todo item.")
@click.option('--description', prompt="Enter the description of the todo item", help="Enter the description of your todo item.")
def todo(name, description, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name} : {description} [Priority: {PRIORITIES[priority]}]")

@click.command()
@click.argument('idx', type=int, required=1)
def delete_todo(idx):
    with open('mytodos.txt', 'r') as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open('mytodos.txt', 'w') as f:
        f.write("\n".join(todo_list))
        f.write("\n")

@click.command()
@click.option('-p', '--priority', type=click.Choice(PRIORITIES.keys()))
@click.argument('todofile', type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, 'r') as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            print(f"({idk}) - {todo}")
    else:
        for idk, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                print(f"({idk}) - {todo}")





if __name__ == "__main__":
    todo()
