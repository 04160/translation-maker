"""TranslationMaker.py: ..."""

import os
import argparse
import time

class TranslationMaker(object):
    def loopThroughFileStructure(self, parent_path, file_list, level):
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
                    self.parseFile(full_path)

                # If sub directory is not in excluded path, traverse it
                if os.path.isdir(full_path) and sub_path not in self.exf:
                    # print(full_path)
                    self.loopThroughFileStructure(full_path, os.listdir(full_path), level + 1)

    def make(self, args):
        self.root = args.root
        self.exf = args.exclude_folder
        self.exn = args.exclude_name
        self.max_level = args.max_level

        self.loopThroughFileStructure(self.root, os.listdir(self.root), 0)

        return 'end'

    def parseFile(self, full_path):
        # Loop through file and find translation usage, noting location of usage if unable to write it
        translations = self.getTranslationUsage(full_path)
        if len(translations) == 0:
            print('No translations found in ' + full_path)
            return 

        # Prepare translation string
        translations = self.prepareTranslationStrings(translations)

        # Write to target translation file,creating structure as necessary
        unstored_translations = self.storeTranslations(translations)

        # Inform user about unstored translations
        if unstored_translations.length > 0:
            self.informOfUnstoredTranslations(unstored_translations)

    def getTranslationUsage(self, full_path):
        translations = []

        return translations

    def prepareTranslationStrings(self, translations):
        return translations

    def storeTranslations(self, translations):
        print(translations)
        return translations

    def informOfUnstoredTranslations(self, unstored_translations):
        print(unstored_translations)

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