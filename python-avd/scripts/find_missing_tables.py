# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import argparse
import glob
import sys
from pathlib import Path

"""
Help on find_missing_tables.py:

DESCRIPTION
    Script to catch schema tables not covered in docs.
    ==================================================

    Checks if table files are added as snips in relevant role docs. Uses argparse to call arguments in CLI with 4 arguments:
        - Glob for table files -> glob
        - Glob for md files, ie. the role docs -> glob
        - Start of relative path to role doc -> Path. For the use in the avd system, the argument: "ansible_collections/arista/avd", should be used as standard
        - Ignored files. The table files that is to be ignored in the search -> Path

        Using these 4 arguments the script calls the functions check_files_in_markdown(table_files, md_files)
        and returns the table files not covered in the role docs

        Can take any number of table_files, any number of role docs, one root path, any number of ignored files, and checks all role docs files for all of the table files.

        checks role docs for the snip string, and adds the table files from the role docs to the md_file_set.

        Adds all table files from the table_files_glob to a set, then reformats to match root_path, and adds to a new set. Discard then the ignored_files,
        and compare to the set of table files found in the role docs.
        Returns the difference set of the two, which is then looped through, printing all the missing files, excepting the ignored ones.

        If set is empty, sys.exit()
"""

parser = argparse.ArgumentParser()

parser.add_argument(
    "--table_files_glob",
    dest="table_files",
    type=glob.glob,
    nargs="*",
    help="The glob for the table file",
)
parser.add_argument(
    "--markdown_files_glob",
    type=glob.glob,
    dest="markdown_files",
    nargs="*",
    help="The glob for the markdown file",
)
parser.add_argument(
    "--root_path",
    dest="root_path",
    type=Path,
    help="The start of the relative path of the md files, ie. the place in the table path from where to cut down to match",
)
parser.add_argument(
    "--ignore_files",
    dest="ignore_files",
    nargs="*",
    type=Path,
    help="The table files to be ignored, when checking for missing table files",
)
args = parser.parse_args()

ignored_files = list(args.ignore_files)

root_path = args.root_path

md_files = list(*args.markdown_files)

table_files = set(*args.table_files)


def check_files_in_markdown(table_files: set, md_files: list):
    md_file_set = set()
    for md_file in md_files:
        with open(md_file) as f:
            md_lines = f.readlines()
            flag = False
            for line in md_lines:
                if line.strip() == "--8<--":
                    flag = not flag
                elif flag:
                    md_file_set.add(Path(line.strip()))

    table_paths_set = {Path(table_file).relative_to(root_path) for table_file in table_files}

    for ignored_file in ignored_files:
        table_paths_set.discard(ignored_file)

    return table_paths_set.difference(md_file_set)


missing_files = check_files_in_markdown(table_files, md_files)
if len(missing_files) == 0:
    sys.exit(0)
else:
    print("These are the missing files:")
    for missing_file in missing_files:
        print(missing_file)
    sys.exit(1)
