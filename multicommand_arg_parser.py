import argparse
import json
import os
import sys


class MulticommandArgParser:

    def __init__(self, json_file: str):
        try:
            with open(json_file, 'r') as file:
                self.parser_json = json.load(file)
        except FileNotFoundError:
            print(f"Cannot find '{json_file}' file")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"JSON decode thrown an exception: {e}")
            sys.exit(1)

    def get_parser(self) -> argparse.ArgumentParser:
        return self.__get_parser_from_json(self.parser_json)

    def __add_subcommand_to_parser(self, parser: argparse.ArgumentParser, json_data: dict):
        subparsers = parser.add_subparsers()
        parser
        for command in json_data:
            subparser = subparsers.add_parser(
                command["command"], help=command.get("help", ""))
            subparser.set_defaults(command_id=command["id"])
            for arg in command.get("args", []):
                self.__add_argument_to_parser(subparser, arg)

            if "subCommands" in command:
                self.__add_subcommand_to_parser(
                    subparser, command["subCommands"])

    def __add_argument_to_parser(self, parser: argparse.ArgumentParser, arg: dict):
        action_type = arg.get("action", "store")
        arg_default = self.__get_default_arg(arg)
        parser.add_argument(
            f'-{arg["short"]}', f'-{arg["long"]}',
            help=arg.get("help", ""),
            action=action_type,
            default=arg_default
        )

    def __add_arguments_to_parser(self, parser: argparse.ArgumentParser, args: list):
        for arg in args:
            self.__add_argument_to_parser(parser, arg)

    def __get_default_arg(self, arg):
        default = arg.get("default", None)
        return os.getenv(arg["envVar"]) if "envvar" in arg else default

    def __get_parser_from_json(self, json_data: dict):
        parser = argparse.ArgumentParser()
        parser.set_defaults(command_id="default")
        self.__add_arguments_to_parser(parser, json_data.get("globalArgs", []))
        self.__add_subcommand_to_parser(parser, json_data["commands"])
        return parser
