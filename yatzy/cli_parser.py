import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--game",
        choices=["yatzy", "maxiyatzy"],
        default="yatzy",
    )
    parser.add_argument(
        "--variant",
        choices=["standard", "topdown"],
        default="standard",
    )
    parser.add_argument(
        "--gui",
        choices=["cli"],
        default="cli",
    )
    return parser.parse_args()
