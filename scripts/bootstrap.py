#!/usr/bin/python3
#    ___             _                  _  _    _
#   / _ \  ___    __| | ___  _ __ ___  (_)| |_ | |__
#  / /_\/ / _ \  / _` |/ __|| '_ ` _ \ | || __|| '_ \
# / /_\\ | (_) || (_| |\__ \| | | | | || || |_ | | | |
# \____/  \___/  \__,_||___/|_| |_| |_||_| \__||_| |_|
#

import os
import subprocess

def report_os():
    uname = "Fedora"#os.uname()
    if uname.version.find("Ubuntu") > 0:
        print("Ubuntu")
    elif uname.version.find("Fedora") > 0:
        print("Fedora")
    else:
        print(f"Uknown OS: {uname}")   
# subprocess.run(["sudo", "apt", "upgrade", "&&", "sudo", "apt", "install", "-y"])
# subprocess.run(["sudo", "apt", "install", "ansible", "-y"])


# print("-----------------Input info for gitconfig file-----------------")
# user_name = os.getenv('USER')
# home_dir = f"/home/{user_name}/"
# file_name = ".gitconfig"
# file_path = os.path.join(home_dir, file_name)

# git_name = input("Enter the name you would like to use for git: ")
# git_email = input("Enter the email you would like to use for git: ")

# with open(file_path, "w") as gitconfig:
# 	gitconfig.write(f"[user]\n \tname = {git_name}\n \temail = {git_email}\n[init]\n\tdefaultBranch = main") print("-----------------Create ssh key for github-----------------")
# #subprocess.run(["git", "remote", "set-url", "origin", "git@github.com:godsmith99x/environment_setup.git"])

# subprocess.run(["ssh-keygen", "-t", "ed25519", "-C", f"{git_email}"])
# subprocess.run(["ssh-agent", "-s"])
# subprocess.run(["ssh-add", f"/home/{user_name}/.ssh/id_ed25519"])
# print("-----------------Done-----------------")

# print("-----------------Create gpg key for github-----------------")
# subprocess.run(["gpg", "--full-generate-key"])
# print("-----------------Done-----------------")
