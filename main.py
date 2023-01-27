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


if __name__ == "__main__":
    todo()
