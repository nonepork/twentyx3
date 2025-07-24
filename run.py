import argparse

from src.main import __version__
from src.main import run


def cli():
    parser = argparse.ArgumentParser(description="twentyx3 application")
    parser.add_argument(
        "--version", "-v", action="store_true", help="Show the version and exit"
    )
    args = parser.parse_args()

    if args.version:
        print(f"twentyx3 version {__version__}")
        return

    run()


if __name__ == "__main__":
    cli()
