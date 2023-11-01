#!/usr/bin/env python3

__author__ = "Antonio Frisenda"
__version__ = "1.0"

from multicommand_arg_parser import MulticommandArgParser
from multicommand_context_holder import ContextHolder

def main():
    mcap = MulticommandArgParser("template-args.json")
    args = mcap.parse_args()
    mcap.print_help()

    print("Selected command with id: ", args.command_id)
    print("Command namespace: ", args)

    print("Command id form Context holder:", ContextHolder.get_command_id())
    print("Namespace from Context holder:", ContextHolder.get_all_args())


if __name__ == "__main__":
    main()
