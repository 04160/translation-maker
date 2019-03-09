"""TranslationMaker.py: ..."""

import os
import argparse

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
                if any(exclude_name in sub_path for exclude_name in self.ex_name):
                    continue

                full_path = os.path.join(parent_path, sub_path)

                # If current full path is of file
                if os.path.isfile(full_path):
                    _, file_extension = os.path.splitext(full_path)
                    if file_extension in self.valid_ext:
                        self.parseFile(full_path)

                # If sub directory is not in excluded path, traverse it
                if os.path.isdir(full_path) and sub_path not in self.ex_folder:
                    # print(full_path)
                    self.loopThroughFileStructure(full_path, os.listdir(full_path), level + 1)

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
        '''
            Loop through file,
            if there is a "__(" or "trans(" record the content until the next valid closing parentheses
        '''
        translations = []

        with open(full_path) as file:
            print (full_path)
            translation_string = ''
            for key, line in enumerate(file):
                #Skip newlines
                if line == '\n':
                    continue

                #While new start indexes can be found on this line, record them
                loop_through_string = True
                current_line = line
                print(current_line)
                while (loop_through_string):
                    # If translation string was already started, its a multiline translation and we need to record from string start
                    if len(translation_string) > 0:
                        start_index = 0
                        prefix_length = 0
                        # print ('ping')
                    else:
                        #check for "__(", if not found then "trans(", if not found either, go to next line
                        start_index = current_line.find("__(")
                        prefix_length = len("__(")
                        if start_index == -1:
                            start_index = current_line.find("trans(")
                            prefix_length = len("trans(")
                            if start_index == -1:
                                break
                        # print ('pong')

                    substring = current_line[start_index + prefix_length:]
                    closing_parentheses = substring.find(")")
                    # break
                    # print({'substring': substring})
                    # print({'substring[:closing_parentheses]': substring[:closing_parentheses]})
                    # print({'closing_parentheses': closing_parentheses})
                    # If string does not contain closing parentheses, check and cleanup comment lines and start multiline translation recording
                    # print({'translation_string': translation_string})
                    # break
                    if closing_parentheses == -1:
                        translation_string += self.removeStringComments(substring)
                        loop_through_string: False
                        break
                    else:
                        translation_string += self.removeStringComments(substring[:closing_parentheses])
                        # loop_through_string: False

                    current_line = current_line[closing_parentheses:]

                    # print({'translation_string': translation_string})

                    # If there is a closing parentheses, check for opening parentheses in the middle of text, possibly skip to next parentheses
                    print({'current_line': current_line})
                    # break
                    # break
                    translations.append({
                        'file': full_path,
                        'line': key,
                        'translation': translation_string
                    })
                    translation_string = ''
                    # break
        # print(translations)
        return translations

    def removeStringComments(self, substring):
        print({'substring': substring})
        return substring

    def prepareTranslationStrings(self, translations):
        self.prettyPrint(translations)
        return translations

    def storeTranslations(self, translations):
        # print(translations)
        return translations

    def informOfUnstoredTranslations(self, unstored_translations):
        print(unstored_translations)

    def make(self, args):
        self.root = args.root
        self.ex_folder = args.exclude_folder
        self.ex_name = args.exclude_name
        self.max_level = args.max_level
        self.valid_ext = args.valid_extensions

        self.loopThroughFileStructure(self.root, os.listdir(self.root), 0)

        return 'end'

    def prettyPrint(self, list):
        for value in list:
            print(value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", help="root of file tree", default=".")
    parser.add_argument("-o", "--output", help="output file name", default="")
    parser.add_argument("-xf", "--exclude_folder", nargs='*', help="Exclude folder", default=['.git', '.vscode'])
    parser.add_argument("-xn", "--exclude_name", nargs='*', help="Exclude name", default=[])
    parser.add_argument("-m", "--max_level", help="max level", type=int, default=-1)
    parser.add_argument("-vex", "--valid_extensions", nargs='*', help="Valid file extensions", default=['.php'])

    args = parser.parse_args()

    print(TranslationMaker().make(args))