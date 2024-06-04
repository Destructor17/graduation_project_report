#!/usr/bin/env python3
import os
import subprocess

def update_submodule():
    ret_code = subprocess.call("git submodule update --init graduation_project_report_common/", shell=True)
    if ret_code!=0:
        exit(ret_code)

def check_is_git_repo():
    return os.path.exists(os.path.join(root_dir, ".git"))

def check_has_gpr_common_submodule():
    p = subprocess.run("git submodule status", shell=True, stdout=subprocess.PIPE)
    lines = p.stdout.decode().split("\n")
    lines = list(filter(lambda line: line.endswith("graduation_project_report_common"), lines))
    return len(lines) == 1

root_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(root_dir)
if not os.path.exists(os.path.join(root_dir, "graduation_project_report_common","scripts", "gprctl_main.py")):
    if not check_is_git_repo():
        print("Error: not a git repo")
        exit(1)
    if not check_has_gpr_common_submodule():
        ret_code = subprocess.call("git submodule add https://github.com/Destructor17/graduation_project_report_common.git")
        if ret_code!=0:
            exit(ret_code)
    ret_code = subprocess.call("git submodule update --init graduation_project_report_common/", shell=True)
    if ret_code!=0:
        exit(ret_code)

import graduation_project_report_common.scripts.gprctl_main as gprctl_main
gprctl_main.run()
