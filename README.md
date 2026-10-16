# clang-apply-replacements

[![PyPI](https://img.shields.io/pypi/v/clang-apply-replacements?labelColor=454a63&color=007ec6)](https://pypi.org/project/clang-apply-replacements/)
[![part of cpp-linter](https://img.shields.io/badge/part%20of-cpp--linter-ffc20a?labelColor=454a63)](https://cpp-linter.github.io/)

A Python wheel of `clang-apply-replacements`, the LLVM-based tool that applies serialized
`clang-tidy` fix-it replacements (YAML files) to source files.

[Website](https://cpp-linter.github.io/) · [Get started](https://cpp-linter.github.io/getting-started/#just-the-clang-tools) · [Discussions](https://github.com/orgs/cpp-linter/discussions)

## Quick start

```bash
pip install clang-apply-replacements
```

The wheel bundles the `clang-apply-replacements` binary; no LLVM installation is required on
the host machine.

> [!TIP]
> In CI, use `pipx run clang-apply-replacements` — no install needed.
> [GitHub-hosted runners](https://github.com/actions/runner-images)
> ship with `pipx` pre-installed.

Verify:

```bash
clang-apply-replacements --version
```

## Usage

`clang-tidy --export-fixes` writes the fixes it suggests to a YAML file, and
`clang-apply-replacements` applies every `.yaml` file under the directory you give it. With a
`compile_commands.json` in `build/`:

```bash
mkdir -p fixes
clang-tidy -p build --export-fixes=fixes/main.yaml src/main.cpp
clang-apply-replacements --remove-change-desc-files fixes
```

- clang-tidy does not create the `fixes` directory, so create it first.
- `--remove-change-desc-files` deletes the YAML files after applying them. Applying the same
  file twice edits the source twice and breaks it.

Run `clang-apply-replacements --help` to see all available options. The
[clang-tidy documentation](https://clang.llvm.org/extra/clang-tidy/) describes `--export-fixes`.

## Supported versions

- PyPI has wheels for LLVM 16 and 17. `pip install clang-apply-replacements` installs the
  newest; `pip install "clang-apply-replacements==16.*"` installs LLVM 16.
- Wheels exist for Linux (x86-64, x86, ARM64 and ARMv7 with glibc; x86-64 and x86 with musl),
  macOS (x86-64 and ARM64) and Windows (x86-64 and x86). On other platforms pip builds the
  source distribution, which downloads and compiles LLVM.
- Since 22.1.8, the `clang-tidy` wheel on PyPI also installs a `clang-apply-replacements`
  command. In an environment with both packages, the one installed last provides the command,
  and uninstalling either one removes it.
- For other LLVM versions, the
  [static binaries](https://github.com/cpp-linter/clang-tools-static-binaries/releases) include
  clang-apply-replacements for LLVM 12 to 23.

## Contributing

See [CONTRIBUTING.md](https://github.com/cpp-linter/clang-apply-replacements/blob/main/CONTRIBUTING.md) for development setup, build instructions, and the release process, and use [GitHub issues](https://github.com/cpp-linter/clang-apply-replacements/issues) for bug reports and feature requests.

## License

This project is licensed under the Apache License 2.0 - see [LICENSE.md](https://github.com/cpp-linter/clang-apply-replacements/blob/main/LICENSE.md) for details. The `clang-apply-replacements` binary bundled in the wheels is part of the [LLVM Project](https://github.com/llvm/llvm-project/releases) and is licensed under the [Apache License 2.0 with LLVM Exceptions](https://github.com/llvm/llvm-project/blob/main/LICENSE.TXT).
