# restore-mcafee

Script to restore files in a bup folder

## Requirements

Install argparse, sys, os.path in Python3

## Usage 

```sh
$ unzip path_zip.bup
$ ./restore-mcafee.py -i [file_extracted from_bup_zip] -o [output_file]
```

## Example

```sh
$ ls 
macfee.bup  LICENSE  README.md  restore-mcafee.py
$ unzip mcafee.bup
$ ls 
mcafee.bup  Details  File_0  LICENSE  README.md  restore-mcafee.py
$ ./restore-mcafee.py -i File_0 -o File_0_result
[+] Restoration file done
$ ./restore-mcafee.py -i Details -o Details_result
[+] Restoration file done
$ ls 
mcafee.bup  Details  Details_result  File_0  File0_result  LICENSE  README.md  restore-mcafee.py
```
