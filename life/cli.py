import argparse

from life import __version__, patterns, views


def get_command_line_args():
    parser = argparse.ArgumentParser(
        prog="life",
        description="Conway's Game of Life",
    )
