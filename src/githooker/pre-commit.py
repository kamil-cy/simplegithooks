#!/usr/bin/env python
from githooker import PreCommit

# FIXME
pre_commit = PreCommit(__file__)
# pre_commit.add_ignored_file("src/githooker/pre-commit.py")
pre_commit.add_ignored_files(["pre-commit.py", "*.svg", "README.md"])
# pre_commit.add_ignored_files([])
pre_commit.check_content_for("FIXME", "❌", "error")
pre_commit.check_content_for("NotImplemented", "🚧", "fail")
pre_commit.check_content_for("TODO", "⚠️", "warning", prevent=False)
pre_commit.check_command("ruff check")
# pre_commit.check_command("true", rc_zero_succes=False)
pre_commit.check_command("false", rc_zero_succes=False)
print(pre_commit.results())
# print(pre_commit.results("error"))
# print(pre_commit.results("warning"))
# print(pre_commit.results(preventing_only=True))
print(pre_commit.summary())
exit(pre_commit.rc)
