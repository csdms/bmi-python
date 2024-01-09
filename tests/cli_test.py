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
    assert main(["MyBmi"]) == 0
    exec(capsys.readouterr().out)
    assert "MyBmi" in globals()


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
