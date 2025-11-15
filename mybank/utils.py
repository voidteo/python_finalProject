def do_you_want_continue() -> None:
    is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
    if is_end == "\n":
        return None


def print_commands(commands: list[str]):
    for command in commands:
        print(command)