class ContextHolder:
    args = {}

    @classmethod
    def init_args(cls,args):
        cls.args = args

    @classmethod
    def get_command_id(cls) -> str:
        return cls.args.command_id

    @classmethod
    def set(cls, key, value):
        cls.args[key] = value

    @classmethod
    def get(cls, key) -> str:
        return cls.get_or_default(key, None)
    
    @classmethod
    def get_or_default(cls, key, default) -> str:
        return cls.args.get(key, default)

    @classmethod
    def get_all_args(cls) -> dict:
        return cls.args
