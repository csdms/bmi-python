from click.testing import CliRunner
import pytest
import six

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


@pytest.mark.skip(reason="hints are disabled in v0")
def test_cli_with_hints(tmpdir):
    runner = CliRunner()
    with tmpdir.as_cwd():
        result = runner.invoke(main, ["MyBmiWithHints", "--hints"])
        assert result.exit_code == 0
        assert "->" in result.output


@pytest.mark.skip(reason="hints are disabled in v0")
def test_cli_without_hints(tmpdir):
    runner = CliRunner()
    with tmpdir.as_cwd():
        result = runner.invoke(main, ["MyBmiWithoutHints", "--no-hints"])
        assert result.exit_code == 0
        assert "->" not in result.output


@pytest.mark.skipif(six.PY2, reason="requires python 3")
def test_cli_with_black(tmpdir):
    runner = CliRunner()
    with tmpdir.as_cwd():
        result = runner.invoke(main, ["MyBmiWithHints", "--black"])
        assert result.exit_code == 0
        assert max([len(line) for line in result.output.splitlines()]) <= 88


@pytest.mark.skipif(six.PY2, reason="requires python 3")
def test_cli_without_black(tmpdir):
    runner = CliRunner()
    with tmpdir.as_cwd():
        result_without = runner.invoke(main, ["MyBmiWithoutHints", "--no-black"])
        result_with = runner.invoke(main, ["MyBmiWithoutHints", "--black"])
        assert result_with.exit_code == 0
        assert result_without.exit_code == 0
        assert result_with.output != result_without.output


@pytest.mark.parametrize("bad_name", ["break", "0Bmi"])
def test_cli_with_bad_class_name(tmpdir, bad_name):
    runner = CliRunner()
    result = runner.invoke(main, [bad_name])
    assert result.exit_code == 1
