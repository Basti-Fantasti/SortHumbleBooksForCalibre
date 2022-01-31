# Sort Books downloaded from Humble Book Bundle

When buying a book bundle from (https://www.humblebundle.com) you get the books in different formats like 
- pdf
- epub
- mobi
- cbz

The easiest way to import these books into Calibre is to move all files from the same book to a separate folder.
Then the import option "All books in a directory are another type of the same book" can be used.

So this small scripty moves all downloaded books from a folder to relative subfolders.

## Call the script

    python sort.py c:\temp
    
    
all the files inside the directory will be sorted like that:

|Original File | Moved File |
|--- |--- |
| c:\temp\book1.pdf | c:\temp\book1\book1.pdf |
| c:\temp\book1.epub | c:\temp\book1\book1.epub |
| c:\temp\book2.pdf | c:\temp\book2\book2.pdf |
| c:\temp\book2.epub | c:\temp\book2\book2.epub |

