"""Command line interface that create template BMI implementations."""
from __future__ import annotations

import argparse
import keyword
import sys

from bmipy._template import Template
from bmipy._version import __version__


def main(args: tuple[str, ...] | None = None) -> int:
    """Render a template BMI implementation in Python for class NAME."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=f"bmipy {__version__}")
    parser.add_argument("name")

    parsed_args = parser.parse_args(args)

    if parsed_args.name.isidentifier() and not keyword.iskeyword(parsed_args.name):
        print(Template(parsed_args.name).render())
    else:
        print(
            f"💥 💔 💥 {parsed_args.name!r} is not a valid class name in Python",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
