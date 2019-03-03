"""TranslationMaker.py: ..."""

import os
import argparse
import time

class TranslationMaker(object):
    def _recurse(self, parent_path, file_list, level):
        if len(file_list) == 0 \
            or (self.max_level != -1 and self.max_level <= level):
            return
        else:
            # Loop through current file list
            file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)))
            for _, sub_path in enumerate(file_list):
                # If file or directory is of excluded name, skip it
                if any(exclude_name in sub_path for exclude_name in self.exn):
                    continue

                full_path = os.path.join(parent_path, sub_path)

                # If current full path is of file
                if os.path.isfile(full_path):
                    print(full_path)

                # If sub directory is not in excluded path, traverse it
                if os.path.isdir(full_path) and sub_path not in self.exf:
                    # print(full_path)
                    self._recurse(full_path, os.listdir(full_path), level + 1)

    def make(self, args):
        self.root = args.root
        self.exf = args.exclude_folder
        self.exn = args.exclude_name
        self.max_level = args.max_level

        self._recurse(self.root, os.listdir(self.root), 0)

        return 'end'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", help="root of file tree", default=".")
    parser.add_argument("-o", "--output", help="output file name", default="")
    parser.add_argument("-xf", "--exclude_folder", nargs='*', help="exclude folder", default=['.git'])
    parser.add_argument("-xn", "--exclude_name", nargs='*', help="exclude name", default=[])
    parser.add_argument("-m", "--max_level", help="max level",
                        type=int, default=-1)
    args = parser.parse_args()
    print(TranslationMaker().make(args))