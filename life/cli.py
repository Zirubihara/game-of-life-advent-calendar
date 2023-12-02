import argparse

from life import __version__, patterns, views


def get_command_line_args():
    parser = argparse.ArgumentParser(
        prog="life",
        description="Conway's Game of Life",
    )

    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    parser.add_argument(
        "-p",
        "--pattern",
        choices=[p.name for p in patterns.get_all_patterns],
        default="glider",
        help="Pattern to start with",
    )
