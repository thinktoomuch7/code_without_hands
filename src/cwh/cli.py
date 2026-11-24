"""Command line interface for the code_without_hands demo."""

from __future__ import annotations

import argparse
from typing import Optional, Sequence

DEFAULT_NAME = "世界"


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the ``cwh`` command."""
    parser = argparse.ArgumentParser(prog="cwh", description="code_without_hands demo")
    subparsers = parser.add_subparsers(dest="command", required=True)

    hello_parser = subparsers.add_parser("hello", help="print a greeting")
    hello_parser.add_argument(
        "--name",
        default=DEFAULT_NAME,
        help="name to greet (default: %(default)s)",
    )
    hello_parser.set_defaults(handler=_handle_hello)

    return parser


def _handle_hello(args: argparse.Namespace) -> int:
    print(f"hello, {args.name}")
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the CLI and return its exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
