import sys
import glob
import os

def main(argv):
    for filename in glob.iglob('./tests', recursive=True):
        print(filename)
        if os.path.isfile(filename): # filter dirs
            print(filename)
    pass

if __name__ == "__main__":
    main(sys.argv)