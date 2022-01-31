import argparse
import os

from os import walk

# Instantiate the parser
parser = argparse.ArgumentParser(description='Move Downloaded Epub, PDF, etc... files to a sub folder for each book for simple Calibre import')

# Required positional argument
parser.add_argument('input_dir', type=str,
                    help='The directory to process')

args = parser.parse_args()

procdir = args.input_dir
print(f'Processing {procdir}')

f = []
for (dirpath, dirnames, filenames) in walk(procdir):
    f.extend(filenames)
    break

for book in f:
    origin = os.path.join(procdir, book)
    fnam = os.path.splitext(book)[0]
    outdir = os.path.join(procdir,fnam)
    dest = os.path.join(outdir, book)
    print(f'Moving book {origin} to new location {dest}')
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    # now directory should exist
    # now move file to output dir
    os.rename(origin, dest)
    #print(book)
print('')
print('finished.')
print('')
print('Books can now be imported using the ')
print('"All books in same directory are different version of the same book" option')