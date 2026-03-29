# Release Notes


## v2.0.2 (2026-03-29)

### Added

* Add a changelog ([#72](https://github.com/csdms/bmipy/pull/72))
* Add `--docstring` / `--no-docstring` CLI options ([#45](https://github.com/csdms/bmipy/pull/45))
* Add `width` option for generated code formatting ([#46](https://github.com/csdms/bmipy/pull/46))
* Add BMI template module for code generation ([#46](https://github.com/csdms/bmipy/pull/46))
* Add Python 3.13 and 3.14 to the CI test matrix ([#68](https://github.com/csdms/bmipy/pull/68))

### Changed

* Replace Click-based CLI with `argparse` ([#45](https://github.com/csdms/bmipy/pull/45))
* Reorder and group generated BMI methods ([#49](https://github.com/csdms/bmipy/pull/49))
* Improve generated type annotations and generated-code testing ([#45](https://github.com/csdms/bmipy/pull/45))
* Switch CI to `actions/setup-python` ([#63](https://github.com/csdms/bmipy/pull/63))
* Manage package version through `pyproject.toml` metadata ([#67](https://github.com/csdms/bmipy/pull/67))
* Make NumPy a typing-only dependency ([#65](https://github.com/csdms/bmipy/pull/65))

### Removed

* Remove Jinja and Black dependencies ([#46](https://github.com/csdms/bmipy/pull/46))
* Remove `setup.py` in favor of `pyproject.toml` ([#46](https://github.com/csdms/bmipy/pull/46))
* Remove pinned dependencies and disable Dependabot ([#66](https://github.com/csdms/bmipy/pull/66))

### Fixed

* Fix CI issue caused by an unsupported nox flag ([#69](https://github.com/csdms/bmipy/pull/69))
* Fix a flaky test ([#45](https://github.com/csdms/bmipy/pull/45))

### Maintenance

* Add manual trigger for publishing to PyPI and TestPyPI ([#75](https://github.com/csdms/bmipy/pull/75))
* Replace Coveralls with Codecov and simplify coverage reporting
  ([#68](https://github.com/csdms/bmipy/pull/68), [#73](https://github.com/csdms/bmipy/pull/73))
* Update linting and pre-commit tooling, including migration to isort
  ([#62](https://github.com/csdms/bmipy/pull/62), [#70](https://github.com/csdms/bmipy/pull/70))
* Update license metadata for PEP 639 ([#71](https://github.com/csdms/bmipy/pull/71))
* Refresh development dependencies and CI tooling ([#39](https://github.com/csdms/bmipy/pull/39),
  [#42](https://github.com/csdms/bmipy/pull/42), [#43](https://github.com/csdms/bmipy/pull/43))


## v2.0.1 (2023-10-24)

### Added

* Add Python 3.12 support ([#32](https://github.com/csdms/bmi-python/pull/32)).
* Add `py.typed` marker for PEP 561 ([#22](https://github.com/csdms/bmi-python/pull/22)).

### Changed

* Move project metadata to `pyproject.toml` ([#16](https://github.com/csdms/bmi-python/pull/16)).
* Switch to zest.releaser ([#18](https://github.com/csdms/bmi-python/pull/18)).
* Configure coverage ([#17](https://github.com/csdms/bmi-python/pull/17)).
* Use GitHub Actions ([#11](https://github.com/csdms/bmi-python/pull/11)).
* Drop Python 3.6; test newer versions ([#15](https://github.com/csdms/bmi-python/pull/15)).

### Removed

* Remove docs directory ([#9](https://github.com/csdms/bmi-python/pull/9)).

### Fixed

* Fix type hints and docstrings ([#37](https://github.com/csdms/bmi-python/pull/37)).
* Fix miniconda download URL ([#8](https://github.com/csdms/bmi-python/pull/8)).


## v2.0 (2020-02-17)

### Added

* Add BMI v2.0 methods ([#4](https://github.com/csdms/bmi-python/pull/4)).
* Add Python 3.8 support.
* Add documentation links and examples.

### Changed

* Update tests for BMI v2.0.

### Fixed

* Fix multiple docstrings.


## v1.0.0 (2019-05-01)

### Added

* Add `bmipy-render` command to generate example BMI implementations.
* Add CLI validation for class names.
* Add optional `--no-hints` flag.
* Add tests for CLI functionality.

### Changed

* Set CLI entry point to `bmipy.cli:main`.

### Fixed

* Fix template type imports.
* Fix class name reset bug.


## v0.3.2 (2019-05-08)

### Fixed

* Minor fixes and packaging updates.


## v0.3.1 (2019-05-08)

### Fixed

* Minor fixes.


## v0.3.0 (2019-05-08)

### Added

* Incremental improvements to CLI and packaging.


## v0.2.0b1 (2019-04-30)

### Added

* Initial beta release of CLI tooling and BMI generator.


## v0.1.0 (2019-04-18)

### Added

* Initial release with BMI implementation, CLI, tests, and CI.
