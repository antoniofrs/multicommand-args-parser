def print_command(commands: list, command_root = "", root_args = []):
    help:str = ""
    for command in commands:
        command_root = f"{command_root.strip()} " if command_root != "" else ""
        help += f"\nCOMMAND: {command_root}{command["command"]}, command_id = {command["id"]}   ({command.get("help", "")})\n"

        args = command.get("args", [])
        help += print_args(args, root_args)

        if "subCommands" in command:
            help += print_command(command["subCommands"], f"{command["command"]}", args)
    return help


def print_args(args: list, root_args: list = []):
    help:str = ""
    if len(root_args) > 0:
        help += print_args(root_args)

    for arg in args:
        help += print_arg(arg)
    return help


def print_arg(arg):
    return "\t-{:<5}\t--{:<15}\t{:<15}\t{:<40}\t{}\n"\
        .format(arg["short"], arg["long"], arg.get("default", ""), arg.get("envvar", ""), arg["help"])
    

def get_parser_help(json_data: dict):
    help = "GLOBAL ARGS:"
    help += print_args(json_data.get("globalArgs", []))
    help += print_command(json_data["commands"])
    return help