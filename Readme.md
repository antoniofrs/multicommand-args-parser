# Multicommand arg parser for python

Structuring a multi-command argparse in Python can be difficult to write and read.

This library allows you to structure commands and subcommands with a recursive json file.


```json
[
    {
        "id": "c1_id",
        "command": "command1",
        "help": "Select c1",
        "args": [ ... ],
        "subCommands": [
            {
                "id": "sc1_id",
                "command": "subcommand1",
                "help": "select sc1",
                "args": [ ... ]
            },
            {
                "id": "sc2_id",
                "command": "subcommand2",
                "help": "Select c12",
                "args": [ ... ]
            }
        ]
    },
    {
        "id": "command2",
        "command": "c2",
        "help": "Selected c2",
        "args": [ ]
    }
]
```

For example, in this json a list of commands is initialized as follows:

| command | id     |
| ------- | ------ |
| c1      | c1_id  |
| c1 sc1  | sc1_id |
| c1 sc2  | sc2_id |
| c2      | c2_id  |

Where is the `id`, which you can retrieve from `agrs.id`, will help you to get
the command given in input by the user

### Arguments

The `args` array contains a list of objects as follows:

```json
{
    "short": "e",
    "long": "example-here",
    "action": "store",
    "help": "This is an example",
    "default": "default-value",
    "envVar": "EXAMPLE_ENV"
}
```

Where:

| field   | description                                     | Optional | Default      |
| ------- | ----------------------------------------------- | -------- | ------------ |
| short   | Arg short name                                  | No       |              |
| long    | Arg extended name                               | No       |              |
| action  | (e.g: store, store_true)                        | Yes      | store        |
| help    | Message to show with -h or --help               | Yes      | empty string |
| default | default value                                   | Yes      | empty string |
| envVar  | Environment variable associated to the argument | Yes      | no env var   |

Default and envVar will respect the following logic:

```python
default_value = os.getenv(arg["envVar"], "default")
```
If the command line argument is passed the environment variable is ignored

### :star: You can find a complete json example in the `template-args.json` file


## How to use

```python
mcap = MulticommandArgParser()
parser = mcap.get_parser_from_template("template-args.json")
args = parser.parse_args()
print("Selected command with id: ", args.id)
print("Args list: ", args)
```

