#!/usr/bin/env python3
import os
import subprocess
import shutil

from_stdin = "__file__" not in globals() or __file__ == "<stdin>"


def update_submodule():
    ret_code = subprocess.call(
        "git submodule update --init graduation_project_report_common/", shell=True
    )
    if ret_code != 0:
        exit(ret_code)


def check_is_git_repo():
    return os.path.exists(os.path.join(root_dir, ".git"))


def check_has_gpr_common_submodule():
    p = subprocess.run("git submodule status", shell=True, stdout=subprocess.PIPE)
    lines = p.stdout.decode().split("\n")
    lines = list(filter(lambda line: "graduation_project_report_common" in line, lines))
    return len(lines) == 1


root_dir = (
    os.path.realpath(os.curdir)
    if from_stdin
    else os.path.dirname(os.path.realpath(__file__))
)
os.chdir(root_dir)
if not os.path.exists(
    os.path.join(root_dir, "graduation_project_report_common", "scripts", "run.py")
):
    if not check_is_git_repo():
        ret_code = subprocess.call("git init", shell=True)
        if ret_code != 0:
            exit(ret_code)
    if not check_has_gpr_common_submodule():
        ret_code = subprocess.call(
            "git submodule add https://github.com/Destructor17/graduation_project_report_common.git",
            shell=True,
        )
        if ret_code != 0:
            exit(ret_code)
    ret_code = subprocess.call(
        "git submodule update --init graduation_project_report_common/", shell=True
    )
    if ret_code != 0:
        exit(ret_code)

if from_stdin:
    print(root_dir)
    shutil.copy(
        os.path.join(
            root_dir, "graduation_project_report_common", "scripts", "gprctl.py"
        ),
        os.path.join(root_dir, "gprctl.py"),
    )
else:
    print(__file__)

import graduation_project_report_common.scripts.run as run

run.run()
