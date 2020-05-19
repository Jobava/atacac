import importlib

import click


COMMANDS = [
    'backup',
    'differentiate',
    'restore',
    'synchronize',
    'upload',
    'validate',
]


class CommandsLoader(click.MultiCommand):
    """
    Multi command loader. Dynamically loads commands from external files.
    """

    def list_commands(self, ctx):
        return COMMANDS

    def get_command(self, ctx, name):
        return importlib.import_module(f'atacac.{name}').main


main = CommandsLoader()


if __name__ == '__main__':
    main()
