from __future__ import annotations

import inspect
import os
import textwrap

from bmipy.bmi import Bmi


class Template:
    """Create template BMI implementations."""

    def __init__(self, name: str):
        self._name = name
        self._funcs = dict(inspect.getmembers(Bmi, inspect.isfunction))

    def render(self) -> str:
        """Render a module that defines a class implementing a Bmi."""
        prefix = f"""\
from __future__ import annotations

import numpy

from bmipy.bmi import Bmi


class {self._name}(Bmi):
"""
        return prefix + (os.linesep * 2).join(
            [self._render_func(name) for name in sorted(self._funcs)]
        )

    def _render_func(self, name: str) -> str:
        annotations = inspect.get_annotations(self._funcs[name])
        signature = inspect.signature(self._funcs[name], eval_str=False)

        docstring = textwrap.indent(
            '"""' + dedent_docstring(self._funcs[name].__doc__) + '"""', "    "
        )

        parts = [
            render_function_signature(
                name,
                tuple(signature.parameters),
                annotations,
            ),
            docstring,
            f"    raise NotImplementedError({name!r})".replace("'", '"'),
        ]

        return textwrap.indent(os.linesep.join(parts), "    ")


def dedent_docstring(text: str | None, tabsize=4) -> str:
    """Dedent a docstring, ignoring indentation of the first line.

    Parameters
    ----------
    text : str
        The text to dedent.
    tabsize : int, optional
        Specify the number of spaces to replace tabs with.

    Returns
    -------
    str
        The dendented string.
    """
    if not text:
        return ""

    lines = text.expandtabs(tabsize).splitlines(keepends=True)
    first = lines[0].lstrip()
    try:
        body = lines[1:]
    except IndexError:
        body = [""]
    return first + textwrap.dedent("".join(body))


def render_function_signature(
    name: str,
    params: tuple[str, ...] | None = None,
    annotations: dict[str, str] | None = None,
    tabsize: int = 4,
) -> str:
    """Render a function signature, wrapping if the generated signature is too long.

    Parameters
    ----------
    name : str
        The name of the function.
    params : tuple of str, optional
        Names of each of the parameters.
    annotations : dict, optional
        Annotations for each parameters as well as the return type.
    tabsize : int, optional
        The number of spacses represented by a tab.

    Returns
    -------
    str
        The function signature appropriately wrapped.
    """
    params = () if params is None else params
    annotations = {} if annotations is None else annotations

    prefix = f"def {name}("
    if "return" in annotations:
        suffix = f") -> {annotations['return']}:"
    else:
        suffix = "):"
    body = []
    for param in params:
        if param in annotations:
            param += f": {annotations[param]}"
        body.append(param)

    signature = prefix + ", ".join(body) + suffix
    if len(signature) <= 88:
        return signature

    indent = " " * tabsize

    lines = [prefix, indent + ", ".join(body), suffix]
    if max(len(line) for line in lines) <= 88:
        return os.linesep.join(lines)

    return os.linesep.join([prefix] + [f"{indent}{line}," for line in body] + [suffix])
