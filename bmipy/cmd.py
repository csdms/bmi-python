import inspect

import black as blk
import click
import jinja2

from bmipy import Bmi

BMI_TEMPLATE = """# -*- coding: utf-8 -*-
{% if with_hints -%}
from typing import Tuple
{%- endif %}

from bmipy import Bmi
import numpy


class {{ name }}(Bmi):
{% for func in funcs %}
    def {{ func }}{{ funcs[func].sig }}:
        \"\"\"{{ funcs[func].doc }}\"\"\"
        raise NotImplementedError("{{ func }}")
{% endfor %}
"""


def remove_hints_from_signature(signature):
    """Remove hint annotation from a signature."""
    params = []
    for name, param in signature.parameters.items():
        params.append(param.replace(annotation=inspect.Parameter.empty))
    return signature.replace(
        parameters=params, return_annotation=inspect.Signature.empty
    )


@click.command()
@click.version_option()
@click.option("--black / --no-black", default=True, help="format output with black")
@click.option("--hints / --no-hints", default=True, help="include type hint annotation")
@click.argument("name")
def render_bmi(name, black, hints):
    """Render a template BMI implementation in Python for class NAME."""

    env = jinja2.Environment()
    template = env.from_string(BMI_TEMPLATE)

    funcs = {}
    for func_name, func in inspect.getmembers(Bmi, inspect.isfunction):
        signature = inspect.signature(func)
        if not hints:
            signature = remove_hints_from_signature(signature)
        funcs[func_name] = {"sig": signature, "doc": func.__doc__}

    contents = template.render(name=name, funcs=funcs, with_hints=hints)

    if black:
        contents = blk.format_file_contents(contents, fast=True, mode=blk.FileMode())

    print(contents)
