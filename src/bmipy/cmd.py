"""Command line interface that create template BMI implementations."""
from __future__ import annotations

import argparse
import functools
import inspect
import keyword
import re
import sys

import jinja2
from bmipy._version import __version__
from bmipy.bmi import Bmi

try:
    import black as blk
except ModuleNotFoundError:
    WITH_BLACK = False
else:
    WITH_BLACK = True

BMI_TEMPLATE = """\
from __future__ import annotations

import numpy

from bmipy.bmi import Bmi


class {{ name }}(Bmi):
{% for func in funcs %}
    def {{ func }}{{ funcs[func].sig }}:
        \"\"\"{{ funcs[func].doc }}\"\"\"
        raise NotImplementedError("{{ func }}")
{% endfor %}
"""

err = functools.partial(print, file=sys.stderr)
out = functools.partial(print, file=sys.stderr)


def _remove_hints_from_signature(signature: inspect.Signature) -> inspect.Signature:
    """Remove hint annotation from a signature."""
    params = []
    for _, param in signature.parameters.items():
        params.append(param.replace(annotation=inspect.Parameter.empty))
    return signature.replace(
        parameters=params, return_annotation=inspect.Signature.empty
    )


def _is_valid_class_name(name: str) -> bool:
    p = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
    return bool(p.match(name)) and not keyword.iskeyword(name)


def render_bmi(name: str, black: bool = True, hints: bool = True) -> str:
    """Render a template BMI implementation in Python.

    Parameters
    ----------
    name : str
        Name of the new BMI class to implement.
    black : bool, optional
        If True, reformat the source using black styling.
    hints : bool, optiona
        If True, include type hint annotation.

    Returns
    -------
    str
        The contents of a new Python module that contains a template for
        a BMI implementation.
    """
    if _is_valid_class_name(name):
        env = jinja2.Environment()
        template = env.from_string(BMI_TEMPLATE)

        funcs = {}
        for func_name, func in inspect.getmembers(Bmi, inspect.isfunction):
            signature = inspect.signature(func)
            if not hints:
                signature = _remove_hints_from_signature(signature)
            funcs[func_name] = {"sig": signature, "doc": func.__doc__}

        contents = template.render(name=name, funcs=funcs, with_hints=hints)

        if black:
            contents = blk.format_file_contents(
                contents, fast=True, mode=blk.FileMode()
            )

        return contents
    else:
        raise ValueError(f"invalid class name ({name})")


def main(args: tuple[str, ...] | None = None) -> int:
    """Render a template BMI implementation in Python for class NAME."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=f"bmipy {__version__}")
    parser.add_argument("name")

    black_parser = parser.add_mutually_exclusive_group()
    if WITH_BLACK:
        black_parser.add_argument(
            "--black",
            action="store_true",
            dest="black",
            default=False,
            help="format output with black",
        )
    black_parser.add_argument(
        "--no-black",
        action="store_false",
        dest="black",
        default=False,
        help="format output with black",
    )
    hints_group = parser.add_mutually_exclusive_group()
    hints_group.add_argument(
        "--hints",
        action="store_true",
        default=True,
        dest="hints",
        help="include type hint annotation",
    )
    hints_group.add_argument(
        "--no-hints",
        action="store_false",
        dest="hints",
        default=True,
        help="include type hint annotation",
    )

    parsed_args = parser.parse_args(args)

    if _is_valid_class_name(parsed_args.name):
        print(
            render_bmi(
                parsed_args.name, black=parsed_args.black, hints=parsed_args.hints
            )
        )
    else:
        err(f"💥 💔 💥 {parsed_args.name!r} is not a valid class name in Python")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
