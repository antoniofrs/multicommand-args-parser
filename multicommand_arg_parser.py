import argparse
import json
import os
import sys


class MulticommandArgParser:

    def add_command_to_parser(self, parser: argparse.ArgumentParser, json_data: dict):
        subparsers = parser.add_subparsers()
        for command in json_data:
            subparser = subparsers.add_parser(command["command"], help=command.get("help", ""))
            subparser.set_defaults(id=command["id"])
            for arg in command.get("args", []):
                self.add_arguments_to_parser(subparser, arg)

            if "subCommands" in command:
                self.add_command_to_parser(subparser, command["subCommands"])

    def __get_default_arg(self, arg):
        default = arg.get("default", None)
        return os.getenv(arg["envVar"]) if "envvar" in arg else default

    def get_parser_from_json(self, json_data: dict):
        parser = argparse.ArgumentParser()
        self.add_command_to_parser(parser, json_data)
        return parser

    def get_parser_from_template(self, json_file: str):
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
            return self.get_parser_from_json(data)
        except FileNotFoundError:
            print(f"Cannot find '{json_file}' file")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"JSON decode thrown an exception: {e}")
            sys.exit(1)

    def add_arguments_to_parser(self, parser: argparse.ArgumentParser, arg: dict):
        action_type = arg.get("action", "store")
        arg_default = self.__get_default_arg(arg)
        parser.add_argument(
            f'-{arg["short"]}', f'-{arg["long"]}',
            help=arg.get("help", ""),
            action=action_type,
            default=arg_default
        )
