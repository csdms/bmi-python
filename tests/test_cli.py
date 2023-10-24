import sys

import pytest
from click.testing import CliRunner

from bmipy.cmd import main


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "help" in result.output


@pytest.mark.skipif(
    sys.platform == "win32", reason="See https://github.com/csdms/bmi-python/issues/10"
)
def test_cli_default(tmpdir):
    import importlib
    import sys

    runner = CliRunner()
    with tmpdir.as_cwd():
        result = runner.invoke(main, ["MyBmi"])
        assert result.exit_code == 0
        with open("mybmi.py", "w") as fp:
            fp.write(result.output)
        sys.path.append(".")
        mod = importlib.import_module("mybmi")
        assert "MyBmi" in mod.__dict__


def test_cli_with_hints(tmpdir):
    runner = CliRunner()
    with tmpdir.as_cwd():
        result = runner.invoke(main, ["MyBmiWithHints", "--hints"])
        assert result.exit_code == 0
        assert "->" in result.output


def test_cli_without_hints(tmpdir):
    runner = CliRunner()
    with tmpdir.as_cwd():
        result = runner.invoke(main, ["MyBmiWithoutHints", "--no-hints"])
        assert result.exit_code == 0
        assert "->" not in result.output


def test_cli_with_black(tmpdir):
    runner = CliRunner()
    with tmpdir.as_cwd():
        result = runner.invoke(main, ["MyBmiWithHints", "--black"])
        assert result.exit_code == 0
        assert max([len(line) for line in result.output.splitlines()]) <= 88


def test_cli_without_black(tmpdir):
    runner = CliRunner()
    with tmpdir.as_cwd():
        result = runner.invoke(main, ["MyBmiWithoutHints", "--no-black"])
        assert result.exit_code == 0
        assert max([len(line) for line in result.output.splitlines()]) > 88


@pytest.mark.parametrize("bad_name", ["True", "0Bmi"])
def test_cli_with_bad_class_name(tmpdir, bad_name):
    runner = CliRunner()
    result = runner.invoke(main, [bad_name])
    assert result.exit_code == 1
