import os
import pathlib
import shutil

import nox

PROJECT = "bmipy"
ROOT = pathlib.Path(__file__).parent


@nox.session
def test(session: nox.Session) -> None:
    """Run the tests."""
    session.install("-r", "requirements/requires.txt", "-r", "requirements/testing.txt")
    session.install(".", "--no-deps")

    args = ["--cov", PROJECT, "-vvv"] + session.posargs

    if "CI" in os.environ:
        args.append(f"--cov-report=xml:{ROOT.absolute()!s}/coverage.xml")
    session.run("pytest", *args)

    if "CI" not in os.environ:
        session.run("coverage", "report", "--ignore-errors", "--show-missing")


@nox.session(name="test-cli")
def test_cli(session: nox.Session) -> None:
    """Test the command line interface."""
    session.install("-r", "requirements/requires.txt")
    session.install(".", "--no-deps")
    session.run("bmi-render", "--help")
    session.run("bmi-render", "--version")


@nox.session
def lint(session: nox.Session) -> None:
    """Look for lint."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session
def locks(session: nox.Session) -> None:
    """Create lock files."""
    folders = session.posargs or [".", "docs", "notebooks"]

    session.install("pip-tools")

    with open("requirements.txt", "wb") as fp:
        session.run("pip-compile", "--upgrade", "pyproject.toml", stdout=fp)

    for folder in folders:
        session.log(f"updated {ROOT / folder / 'requirements.txt'!s}")


@nox.session(name="sync-requirements", python="3.11", venv_backend="conda")
def sync_requirements(session: nox.Session) -> None:
    """Sync requirements.in with pyproject.toml."""
    with open("requirements.in", "w") as fp:
        session.run(
            "python",
            "-c",
            """
import os, tomllib
with open("pyproject.toml", "rb") as fp:
    print(os.linesep.join(sorted(tomllib.load(fp)["project"]["dependencies"])))
""",
            stdout=fp,
        )


@nox.session
def build(session: nox.Session) -> None:
    """Build sdist and wheel dists."""
    session.install("pip")
    session.install("build")
    session.run("python", "--version")
    session.run("pip", "--version")
    session.run("python", "-m", "build", "--outdir", "./build/wheelhouse")


@nox.session
def release(session):
    """Tag, build and publish a new release to PyPI."""
    session.install("zest.releaser[recommended]")
    session.run("fullrelease")


@nox.session(name="publish-testpypi")
def publish_testpypi(session):
    """Publish wheelhouse/* to TestPyPI."""
    session.run("twine", "check", "build/wheelhouse/*")
    session.run(
        "twine",
        "upload",
        "--skip-existing",
        "--repository-url",
        "https://test.pypi.org/legacy/",
        "build/wheelhouse/*.tar.gz",
    )


@nox.session(name="publish-pypi")
def publish_pypi(session):
    """Publish wheelhouse/* to PyPI."""
    session.run("twine", "check", "build/wheelhouse/*")
    session.run(
        "twine",
        "upload",
        "--skip-existing",
        "build/wheelhouse/*.tar.gz",
    )


@nox.session(python=False)
def clean(session):
    """Remove all .venv's, build files and caches in the directory."""
    for folder in _args_to_folders(session.posargs):
        with session.chdir(folder):
            shutil.rmtree("build", ignore_errors=True)
            shutil.rmtree("build/wheelhouse", ignore_errors=True)
            shutil.rmtree(f"{PROJECT}.egg-info", ignore_errors=True)
            shutil.rmtree(".pytest_cache", ignore_errors=True)
            shutil.rmtree(".venv", ignore_errors=True)

            for pattern in ["*.py[co]", "__pycache__"]:
                _clean_rglob(pattern)


def _args_to_folders(args):
    return [ROOT] if not args else [pathlib.Path(f) for f in args]


def _clean_rglob(pattern):
    nox_dir = pathlib.Path(".nox")

    for p in pathlib.Path(".").rglob(pattern):
        if nox_dir in p.parents:
            continue
        if p.is_dir():
            p.rmdir()
        else:
            p.unlink()
