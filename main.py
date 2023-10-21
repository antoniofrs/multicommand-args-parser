#!/usr/bin/env python3

__author__ = "Antonio Frisenda"
__version__ = "0.1.0"


from multicommand_arg_parser import MulticommandArgParser


def main():
    mcap = MulticommandArgParser()
    parser = mcap.get_parser_from_template("template-args.json")
    args = parser.parse_args()
    print("Selected command with id: ", args.id)
    print("Command  Namespace: ", args)


if __name__ == "__main__":
    main()
