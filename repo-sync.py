#! /usr/bin/python

import yaml
import subprocess
import sys
import os

def run_commands(commands, directory):
    command_str = ' && '.join(commands)
    process = subprocess.Popen(command_str, shell=True, cwd=directory, executable="/bin/bash")
    process.wait()

def main(action, name, directory):
    with open('repositories.yaml', 'r') as file:
        config = yaml.safe_load(file)

    for item in config:
        if name == 'all' or item['name'] == name:
            if action in item:
                print(f"Running {action} for {item['name']}...")
                run_commands(item[action], directory)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python repo-sync.py [action] [all|repository name] [directory]")
        sys.exit(1)

    action = sys.argv[1]
    name = sys.argv[2]
    directory = sys.argv[3]

    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        sys.exit(1)

    main(action, name, directory)
