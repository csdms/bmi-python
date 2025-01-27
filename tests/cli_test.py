from __future__ import annotations

import pytest

from bmipy._cmd import main


def test_cli_version(capsys):
    try:
        assert main(["--version"]) == 0
    except SystemExit:
        pass
    output = capsys.readouterr().out

    assert "bmipy" in output


def test_cli_help(capsys):
    try:
        assert main(["--help"]) == 0
    except SystemExit:
        pass
    output = capsys.readouterr().out

    assert "help" in output


def test_cli_default(capsys):
    assert main(["MyUniqueBmi"]) == 0
    globs = {}
    exec(capsys.readouterr().out, globs)
    assert "MyUniqueBmi" in globs


def test_cli_wraps_lines(capsys):
    assert main(["MyBmi"]) == 0
    output = capsys.readouterr().out
    assert max(len(line) for line in output.splitlines()) <= 88


def test_cli_with_hints(capsys):
    assert main(["MyBmiWithHints"]) == 0
    output = capsys.readouterr().out
    assert "->" in output


@pytest.mark.parametrize("bad_name", ["True", "0Bmi"])
def test_cli_with_bad_class_name(capsys, bad_name):
    assert main([bad_name]) != 0


def test_cli_docstrings(capsys):
    assert main(["MyBmiWithDocstrings", "--docstring"]) == 0
    output_default = capsys.readouterr().out

    assert main(["MyBmiWithDocstrings", "--docstring"]) == 0
    output_with_docstrings = capsys.readouterr().out
    assert output_with_docstrings == output_default

    assert main(["MyBmiWithoutDocstrings", "--no-docstring"]) == 0
    output_without_docstrings = capsys.readouterr().out

    assert len(output_with_docstrings) > len(output_without_docstrings)
