from __future__ import annotations

import sys

import pytest
from bmipy.cmd import main
from bmipy.cmd import WITH_BLACK


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


# @pytest.mark.skipif(
#     sys.platform == "win32", reason="See https://github.com/csdms/bmi-python/issues/10"
# )
def test_cli_default(capsys, tmpdir):
    import importlib
    import sys

    with tmpdir.as_cwd():
        assert main(["MyBmi"]) == 0
        output = capsys.readouterr().out
        with open("mybmi.py", "w") as fp:
            fp.write(output)
        sys.path.append(".")
        mod = importlib.import_module("mybmi")
        assert "MyBmi" in mod.__dict__


def test_cli_with_hints(capsys, tmpdir):
    with tmpdir.as_cwd():
        assert main(["MyBmiWithHints", "--hints"]) == 0
        output = capsys.readouterr().out
        assert "->" in output


def test_cli_without_hints(capsys, tmpdir):
    with tmpdir.as_cwd():
        assert main(["MyBmiWithoutHints", "--no-hints"]) == 0
        output = capsys.readouterr().out
        assert "->" not in output


@pytest.mark.skipif(not WITH_BLACK, reason="black is not installed")
def test_cli_with_black(capsys, tmpdir):
    with tmpdir.as_cwd():
        assert main(["MyBmiWithHints", "--black"]) == 0
        output = capsys.readouterr().out
        assert max(len(line) for line in output.splitlines()) <= 88


def test_cli_without_black(capsys, tmpdir):
    with tmpdir.as_cwd():
        assert main(["MyBmiWithHints", "--hints", "--no-black"]) == 0
        output = capsys.readouterr().out
        assert max(len(line) for line in output.splitlines()) > 88


@pytest.mark.parametrize("bad_name", ["True", "0Bmi"])
def test_cli_with_bad_class_name(capsys, tmpdir, bad_name):
    assert main([bad_name]) != 0
