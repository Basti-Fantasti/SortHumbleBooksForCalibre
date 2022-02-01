import os
import sys
from os import walk


procdir = sys.argv[1]
print(f'Processing {procdir}')

f = []
for (dirpath, dirnames, filenames) in walk(procdir):
    f.extend(filenames)
    break
print(f'found these files: {f}')
print('processing...')
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
