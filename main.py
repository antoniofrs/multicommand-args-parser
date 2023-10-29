#!/usr/bin/env python3

__author__ = "Antonio Frisenda"
__version__ = "0.1.0"

from multicommand_arg_parser import MulticommandArgParser

def main():
    mcap = MulticommandArgParser("template-args.json")
    parser = mcap.get_parser()
    args = parser.parse_args()
    print("Selected command with id: ", args.command_id)
    print("Command  Namespace: ", args)


if __name__ == "__main__":
    main()
