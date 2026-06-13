<!-- markdownlint-disable MD033 MD041 -->

[issues]: https://github.com/cpp-linter/clang-apply-replacements/issues
[contributing]: https://github.com/cpp-linter/clang-apply-replacements/blob/main/CONTRIBUTING.md
[clang-format-wheel]: https://github.com/ssciwr/clang-format-wheel
[clang-tidy-wheel]: https://github.com/ssciwr/clang-tidy-wheel
[clang-include-cleaner]: https://github.com/cpp-linter/clang-include-cleaner
[license]: https://github.com/cpp-linter/clang-apply-replacements/blob/main/LICENSE.md

[llvm-releases]: https://github.com/llvm/llvm-project/releases
[cpp-linter-hub]: https://cpp-linter.github.io/

# clang-apply-replacements

[![PyPI version](https://img.shields.io/pypi/v/clang-apply-replacements.svg?color=blue)](https://pypi.org/project/clang-apply-replacements/)
[![Platform](https://img.shields.io/badge/platform-linux--64%20%7C%20linux--arm64%20%7C%20win--64%20%7C%20osx--64%20%7C%20osx--arm64-blue)](https://github.com/cpp-linter/clang-apply-replacements)
[![Build](https://github.com/cpp-linter/clang-apply-replacements/actions/workflows/release.yml/badge.svg)](https://github.com/cpp-linter/clang-apply-replacements/actions/workflows/release.yml)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/clang-apply-replacements)](https://pypistats.org/packages/clang-apply-replacements)
[![cpp-linter hub](https://img.shields.io/badge/%F0%9F%8F%A0_cpp--linter_hub-%E2%86%90_home-22863a)](https://cpp-linter.github.io/)

A Python distribution of `clang-apply-replacements` - the LLVM-based tool
that applies **serialized `clang-tidy` fix-it replacements** (YAML files) to
source files. Install it with a single `pip install`, no LLVM toolchain
required.

---

## Table of Contents

- [Installation](#installation)
- [Related Projects](#related-projects)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
pip install clang-apply-replacements
```

The wheel bundles a statically-linked binary and clang builtin
headers - **no LLVM installation is required** on the host machine.

> [!TIP]
> In CI, use `pipx run clang-apply-replacements` — no install needed.
> All [GitHub Actions runners](https://docs.github.com/en/actions)
> ship with `pipx` pre-installed.

Verify:

```bash
clang-apply-replacements --version
```

Run `clang-apply-replacements --help` to see all available options.

For full usage documentation, see the
[upstream docs](https://clang.llvm.org/extra/clang-apply-replacements.html).

## Related Projects

- [**clang-format-wheel**][clang-format-wheel] — pip-installable clang-format binary
- [**clang-tidy-wheel**][clang-tidy-wheel] — pip-installable clang-tidy binary
- [**clang-include-cleaner**][clang-include-cleaner] — pip-installable clang-include-cleaner binary

## Contributing

We welcome contributions! See [CONTRIBUTING.md][contributing] for
development setup, build instructions, and the release process.

Please use [GitHub issues][issues] for bug reports and feature requests.

## License

This project is licensed under the Apache License 2.0 with LLVM
exceptions - see [LICENSE.md][license] for details.

The `clang-apply-replacements` binary bundled in the wheels is part of the
[LLVM Project][llvm-releases] and is provided under the same license.
