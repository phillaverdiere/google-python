#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil

"""Copy Special exercise
"""

# +++your code here+++
def get_special_paths(dirs):
  found = []
  for dir in dirs:
    files = os.listdir(dir)
    for file in files:
      match = re.search("\w*__[a-zA-Z]+__[a-zA-Z.]*", file)
      if match:
        file = match.group()
        found.append(os.path.abspath(os.path.join(dir,file)))

  return found

def copy_to(paths, dir):
  for path in paths:
    if not os.path.exists(dir):
      os.mkdir(dir)
    shutil.copy(path, dir)

def zip_to(paths, zippath):
  pass



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  paths = get_special_paths(args)
  if todir != '':
    copy_to(paths, todir)
  elif tozip != '':
    zip_to(paths, tozip)
  else:
    for path in paths:
      print(path)
  
if __name__ == "__main__":
  main()
