import os
import sys
import tempfile
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def ensure_apply_replacements_from_wheel(monkeypatch):
    """test the installed clang_apply_replacements package, not the local one"""
    this_dir = Path(__file__).resolve().absolute().parent
    for pd in (this_dir, this_dir / ".."):
        try:
            new_path = sys.path.remove(pd)
            monkeypatch.setattr(sys, "path", new_path)
        except ValueError:
            pass
    monkeypatch.delitem(sys.modules, "clang_apply_replacements", raising=False)


def test_executable_file(capsys):
    import clang_apply_replacements

    clang_apply_replacements._get_executable.cache_clear()
    exe = clang_apply_replacements.get_executable("clang-apply-replacements")
    assert os.path.exists(exe)
    assert os.access(exe, os.X_OK)
    assert capsys.readouterr().out == ""


def _test_help():
    import clang_apply_replacements

    assert (
        clang_apply_replacements._run(
            "clang-apply-replacements",
            "--help",
        ) == 0
    )


def test_verbose_output(capsys, monkeypatch):
    import clang_apply_replacements
    monkeypatch.setenv("CLANG_APPLY_REPLACEMENTS_WHEEL_VERBOSE", "1")
    # need to clear cache to make sure the function is run again
    clang_apply_replacements._get_executable.cache_clear()
    clang_apply_replacements.get_executable("clang-apply-replacements")
    assert capsys.readouterr().out


def test_help():
    _test_help()
