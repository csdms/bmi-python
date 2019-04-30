import inspect

import black as blk
import click
import jinja2

from bmipy import Bmi

BMI_TEMPLATE = """# -*- coding: utf-8 -*-

from bmipy import Bmi
import numpy


class {{ name }}(Bmi):
{% for func in funcs %}
    def {{ func }}{{ funcs[func].sig }}:
        \"\"\"{{ funcs[func].doc }}\"\"\"
        raise NotImplementedError("{{ func }}")
{% endfor %}
"""


@click.command()
@click.version_option()
@click.option("--black / --no-black", is_flag=True, help="format output with black")
@click.argument("name")
def render_bmi(name, black):
    """Render a template BMI implementation in Python for class NAME."""

    env = jinja2.Environment()
    template = env.from_string(BMI_TEMPLATE)

    funcs = {}
    for name, func in inspect.getmembers(Bmi, inspect.isfunction):
        funcs[name] = {"sig": inspect.signature(func), "doc": func.__doc__}

    contents = template.render(name=name, funcs=funcs)
    if black:
        contents = blk.format_file_contents(contents, fast=True, mode=blk.FileMode())

    print(contents)
