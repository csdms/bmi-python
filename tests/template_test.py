from __future__ import annotations

import pytest

from bmipy._template import dedent_docstring
from bmipy._template import render_function_signature


@pytest.mark.parametrize(
    "text",
    (
        "  Foo",
        "\tFoo\n    bar ",
        "\tFoo\n bar",
        "Foo\n        bar\n        baz\n",
    ),
)
def test_dedent_docstring_aligned(text):
    fixed_text = dedent_docstring(text)
    assert [
        line.lstrip() for line in fixed_text.splitlines()
    ] == fixed_text.splitlines()


@pytest.mark.parametrize(
    "text", ("Foo", "  Foo", "\tFoo  ", "\n  Foo", "  Foo\nBar\nBaz")
)
def test_dedent_docstring_lstrip_first_line(text):
    fixed_text = dedent_docstring(text)
    assert fixed_text[0].lstrip() == fixed_text[0]


@pytest.mark.parametrize("text", (None, "", """"""))
def test_dedent_docstring_empty(text):
    assert dedent_docstring(text) == ""


@pytest.mark.parametrize(
    "text,tabsize",
    (("\tFoo", 8), ("Foo\n\tBar  baz", 2), ("\t\tFoo\tBar\nBaz", 0)),
)
def test_dedent_docstring_tabsize(text, tabsize):
    fixed_text = dedent_docstring(text, tabsize)
    assert [
        line.lstrip() for line in fixed_text.splitlines()
    ] == fixed_text.splitlines()


@pytest.mark.parametrize(
    "text",
    ("Foo\n  Bar\n Baz",),
)
def test_dedent_docstring_body_is_left_justified(text):
    lines = dedent_docstring(text).splitlines()[1:]
    assert any(line.lstrip() == line for line in lines)


@pytest.mark.parametrize(
    "annotations",
    (
        {"bar": "int"},
        {"bar" * 10: "int", "baz" * 10: "int"},
        {"bar" * 20: "int", "baz" * 20: "int"},
    ),
)
def test_render_function_wraps(annotations):
    params = list(annotations)
    annotations["return"] = "str"

    text = render_function_signature("foo", params, annotations)
    assert max(len(line) for line in text.splitlines()) <= 88


@pytest.mark.parametrize(
    "annotations",
    (
        {},
        {"bar": "int"},
        {"bar" * 10: "int", "baz" * 10: "int"},
        {"bar" * 20: "int", "baz" * 20: "int"},
    ),
)
def test_render_function_is_valid(annotations):
    params = list(annotations)
    annotations["return"] = "str"

    text = render_function_signature("foo", params, annotations)
    generated_code = f"{text}\n    return 'FOOBAR!'"

    globs = {}
    exec(generated_code, globs)

    assert "foo" in globs
    assert globs["foo"](*range(len(params))) == "FOOBAR!"
