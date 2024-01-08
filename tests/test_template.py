import pytest

from bmipy._template import dedent_docstring


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
    assert [l.lstrip() for l in fixed_text.splitlines()] == fixed_text.splitlines()


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
    assert [l.lstrip() for l in fixed_text.splitlines()] == fixed_text.splitlines()


@pytest.mark.parametrize(
    "text",
    ("Foo\n  Bar\n Baz",),
)
def test_dedent_docstring_body_is_left_justified(text):
    lines = dedent_docstring(text).splitlines()[1:]
    assert any(line.lstrip() == line for line in lines)
