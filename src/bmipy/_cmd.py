"""Command line interface that create template BMI implementations."""
from __future__ import annotations

import argparse
import keyword
import sys

from bmipy._template import Template
from bmipy._version import __version__


def main(argv: tuple[str, ...] | None = None) -> int:
    """Render a template BMI implementation in Python for class NAME."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=f"bmipy {__version__}")
    parser.add_argument("name")

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--docstring",
        action="store_true",
        dest="docstring",
        default=True,
        help="Add docstrings to the generated methods (default: include docstrings)",
    )
    group.add_argument("--no-docstring", action="store_false", dest="docstring")

    args = parser.parse_args(argv)

    if args.name.isidentifier() and not keyword.iskeyword(args.name):
        print(Template(args.name).render(with_docstring=args.docstring))
    else:
        print(
            f"💥 💔 💥 {args.name!r} is not a valid class name in Python",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
