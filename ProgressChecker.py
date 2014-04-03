#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Icon Theme Progress Checker

'''
Copyright (C) 2014 David Wright <david.wright12886@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

"""
TODO

1.

"""

import os, sys
from itertools import zip_longest

# Icon Directories

folders = ['actions', 'animations', 'applications', 'categories', 'devices', 'emblems', 'emotes', 'mimetypes', 'places', 'status']

folder_path = {'actions': './actions',
                      'animations':'./animations',
                      'applications': './apps',        # Could be 'applications' depending on theme
                      'categories': './categories',
                      'devices': './devices',
                      'emblems': './emblems',
                      'emotes': './emotes',
                      'mimetypes': './mimetypes',
                      'places': './places',
                      'status': './status'}

# Paths to freedesktop icon name databases (individual plain text files)

freedesktop_icons_db = {'actions': './zz_icon_names_db/actions_freedesktop',
                                     'animations':'./zz_icon_names_db/animations_freedesktop',
                                     'applications': './zz_icon_names_db/applications_freedesktop',
                                     'categories': './zz_icon_names_db/categories_freedesktop',
                                     'devices': './zz_icon_names_db/devices_freedesktop',
                                     'emblems': './zz_icon_names_db/emblems_freedesktop',
                                     'emotes': './zz_icon_names_db/emotes_freedesktop',
                                     'mimetypes': './zz_icon_names_db/mimetypes_freedesktop',
                                     'places': './zz_icon_names_db/places_freedesktop',
                                     'status': './zz_icon_names_db/status_freedesktop'}

# Functions 

def list_of_files(path):
  """
  Returns an a-z ordered list of files, minus their extension, from a given directory and outputs them into a list:
  
  >>> root = []
  >>> list_of_files('/')
  >>> root
  ['.config', '.rpmdb', 'bin', 'boot', ...]
  
  """
  x = []
  dirs = sorted(os.listdir(path))
  for file in dirs:
    stripped = os.path.splitext(file)[0]
    x.append(stripped)
  return(x)  

def difference(a, b):
  """ 
  Show what's in list 'b' which isn't in list 'a':
  
  >>> a = [1, 2, 3, 4]
  >>> b = [1, 2, 3, 4, 5, 6]
  >>> difference(a, b)
  [5, 6]
  
  """
  return(list(set(b).difference(set(a))))

def list_of_file_contents(filedb):
  """
  Opens a plain text file with an item on each line and converts into a list.
  
  Contents of 'test':
  testline1
  testline2
  testline3
  
  >>> list_of_file_contents('/home/david/test')
  ['testline1', 'testline2', 'testline3']
  
  """
  x = [line.strip() for line in open(filedb, 'r')]
  return(x)
    
def output_string(file_list):
  """
  
  Produces a column output when printed
  Used for testing other functions. 
  
  >>> list = [1, 2, 3, 4, 5]
  >>> output_string(list)
  '1\n2\n3\n4\n5'
  
  Alternate method that might prove to be better / more useful at some point:
  
  >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
  >>> for f in sorted(set(basket)):
  ...     print(f)
  ...
  apple
  banana
  orange
  pear
  
  """
  x = "\n".join(str(x) for x in file_list)
  return(x)


# Output

print("\n Icons Created / Todo \n")

for folder in folders:
  print('\n')
  print('{:-^30}'.format(folder))
  print("{:41}".format("In Database"), "{:41}".format("Todo"), "{:41}".format("Done"), "{:41}".format("Possible Error"))
  print('\n')
  
  dbcontents = list_of_file_contents(freedesktop_icons_db[folder])
  dbcontents_sorted = sorted(dbcontents)

  diff_todo = difference(list_of_files(folder_path[folder]), list_of_file_contents(freedesktop_icons_db[folder]))  
  diff_todo_sorted = sorted(diff_todo)
  
  diff_error = difference(list_of_file_contents(freedesktop_icons_db[folder]), list_of_files(folder_path[folder]))  
  diff_error_sorted = sorted(diff_error)
  
  done_sorted = sorted(list_of_files(folder_path[folder]))


  for elems in zip_longest(dbcontents_sorted, diff_todo_sorted, done_sorted, diff_error_sorted):
        for e in elems:
            if e is not None:
                print("{:40}".format(e), end= " ")
            else:
                print("{:40}".format(""), end= " ")
        print()
