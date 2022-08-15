#!/usr/bin/env python

import os

file_dir_input = ''
file_dir = ''
base_pairs = 0
total_files = 0
total_dirs = 0
names_dict = {}

# while there's no folder identified
while ('\\' not in file_dir_input) and ('/' not in file_dir_input):
    # the directory you want to work with
    file_dir_input = input('input folder path:\n> ')
    # for unix paths
    if file_dir_input.startswith('/') == True:
        file_dir = file_dir_input
    # for windows paths
    elif '\\' in file_dir_input:
        # add '\\?\' to make universal path\
        #   (combat character limit for long paths)
        file_dir = '\\\\?\\%s' % file_dir_input
    # put in a path to a directory pls
    if ('\\' not in file_dir_input) and ('/' not in file_dir_input):
        file_dir = ''

# for each folder and file within that directory
for root, dirs, files in os.walk(file_dir):
    # tally number of files and dirs
    total_dirs += len(dirs)
    total_files += len(files)
    # for each file
    for name in files:
        files_set = set(names_dict)
        # get absolute path, identify file's base name
        full_file_path = os.path.join(root, name)
        base_name_uc, file_ext = os.path.splitext(full_file_path)
        base_name = base_name_uc.lower()
        # if there's no name somehow
        if base_name == '':
            base_name = '[N/A]'
        # if the base name is already recorded, +1
        if base_name in files_set:
            names_dict[base_name] += 1
        # if it's a new base name, add it
        else:
            names_dict[base_name] = 1

# print results
print("\n-----\nrelative filepaths of irregular pairs")
for base in sorted(names_dict, key=names_dict.get, reverse=True):
    base_count = (names_dict[base])
    base_replace = base.replace(file_dir.lower(), '')
    # if there's an abnormal pairing
    if base_count != 2:
        print('%s: %s file(s)' % (base_replace, base_count))
    # if there's a problem with the name
    elif base == '[N/A]':
        print('[N/A] %s: %s file(s)' % (base_replace, base_count))
    # otherwise tally the successful pair matches
    else:
        base_pairs += 1
print('\nmatching basename pairs: %s\ntotal files: %s\
\ntotal directories: %s\n-----' % (base_pairs, total_files, total_dirs))