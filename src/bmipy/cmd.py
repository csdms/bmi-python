"""Command line interface that create template BMI implementations."""
from __future__ import annotations

import click

from bmipy._template import Template


@click.command()
@click.version_option()
@click.argument("name")
@click.pass_context
def main(ctx: click.Context, name: str):
    """Render a template BMI implementation in Python for class NAME."""
    if name.isidentifier():
        print(Template(name).render())
    else:
        click.secho(
            f"💥 💔 💥 {name!r} is not a valid class name in Python",
            err=True,
            fg="red",
        )
        ctx.exit(code=1)
