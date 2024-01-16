from __future__ import annotations

import inspect
import os
import re
import textwrap
from collections import defaultdict
from collections import OrderedDict

from bmipy.bmi import Bmi

GROUPS = (
    ("initialize", "initialize"),
    ("update", "(update|update_until)"),
    ("finalize", "finalize"),
    ("info", r"(get_component_name|\w+_var_names|\w+_item_count)"),
    ("var", r"get_var_\w+"),
    ("time", r"get_\w*time\w*"),
    ("value", r"(get|set)_value\w*"),
    ("grid", r"get_grid_\w+"),
)


class Template:
    """Create template BMI implementations."""

    def __init__(self, name: str):
        self._name = name

        funcs = dict(inspect.getmembers(Bmi, inspect.isfunction))

        names = sort_methods(frozenset(funcs))

        self._funcs = OrderedDict(
            (name, funcs.pop(name)) for name in names
        ) | OrderedDict(sorted(funcs.items()))

    def render(self, with_docstring: bool = True) -> str:
        """Render a module that defines a class implementing a Bmi."""
        prefix = f"""\
from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray

from bmipy.bmi import Bmi


class {self._name}(Bmi):
"""
        return prefix + (os.linesep * 2).join(
            [
                self._render_func(name, with_docstring=with_docstring)
                for name in self._funcs
            ]
        )

    def _render_func(self, name: str, with_docstring: bool = True) -> str:
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
                width=84,
            )
        ]
        parts.append(docstring) if with_docstring else None
        parts.append(f"    raise NotImplementedError({name!r})".replace("'", '"'))

        return textwrap.indent(os.linesep.join(parts), "    ")


def sort_methods(funcs: frozenset[str]) -> list[str]:
    """Sort methods by group type."""
    unmatched = set(funcs)
    matched = defaultdict(set)

    for group, regex in GROUPS:
        pattern = re.compile(regex)

        matched[group] = {name for name in unmatched if pattern.match(name)}
        unmatched -= matched[group]

    ordered = []
    for group, _ in GROUPS:
        ordered.extend(sorted(matched[group]))

    return ordered + sorted(unmatched)


def dedent_docstring(text: str | None, tabsize: int = 4) -> str:
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
    width: int = 88,
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
    width : int, optional
        The maximum width of a line.

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
    if len(signature) <= width:
        return signature

    indent = " " * tabsize

    lines = [prefix, indent + ", ".join(body), suffix]
    if max(len(line) for line in lines) <= width:
        return os.linesep.join(lines)

    return os.linesep.join([prefix] + [f"{indent}{line}," for line in body] + [suffix])
