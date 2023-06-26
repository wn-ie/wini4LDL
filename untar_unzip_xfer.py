# imports

import os, sys, subprocess, glob, zipfile, tarfile, shutil


# source input, windows only
drivepath = ''
while ('\\' not in drivepath):
    # asks for the directory in the CLI window
    drivepath_input = input('drag or paste the source (hard drive) path below:\n> ')
    if '\\' in drivepath_input:
        drivepath = drivepath_input.replace('''"''', '''''')
    # put in a path to a directory pls
    else:
        drivepath = ''

# destination input, windows only
destinationroot = ''
while ('\\' not in destinationroot):
    # asks for the directory in the CLI window
    destinationroot_input = input('drag or paste the destination (R or P drive folder) path below:\n> ')
    if '\\' in destinationroot_input:
        destinationroot =  destinationroot_input.replace('''"''', '''''')
    # put in a path to a directory pls
    else:
        destinationroot = ''


# find all root level tarballs
roottarfilesglob = "%s\\*.tar.gz" % drivepath
roottarfiles = [f for f in glob.glob((roottarfilesglob), recursive = False)]
# check to make sure this atarball hasn't already been transferred
for atarball in roottarfiles:
    atarballdestpath = atarball.replace(drivepath, destinationroot).replace('.tar.gz', '')
    summarypath = '%s\\copysummary.txt' % atarballdestpath
    if os.path.exists(summarypath) == False:
        # try/except for if this dir has already been partially transferred
        try:
            os.makedirs(atarballdestpath)
        except:
            print("%s destination folder already created" % atarball)
        atarballdir = atarball.replace('.tar.gz', '')
        atarballbasename = os.path.basename(atarball)
        dirstowalk = [atarballdir]
        # if not, open this one highest level tarball
        roottarball = tarfile.open(atarball)
        roottarball.extractall(atarballdir)
        # walk through this one tarball opening everything underneath it
        for walkdir in dirstowalk:
            for root, dirs, files in os.walk(walkdir):
                for walkname in files:
                    if walkname.startswith('._') == False:
                        if '.tar.gz' in walkname:
                            walknamefullpath = (os.path.join(root, walkname))
                            newdirfromwalkname = walknamefullpath.replace(".tar.gz", "")
                            with tarfile.open(walknamefullpath) as opentarball:
                                opentarball.extractall(newdirfromwalkname)
                            dirstowalk.append(newdirfromwalkname)
                        # this zipfile opening often creates dirs titled __MACOSX but that's fine
                        if '.zip' in walkname:
                            walknamefullpath = (os.path.join(root, walkname))
                            # print(walknamefullpath)
                            newdirfromwalkname = walknamefullpath.replace(".zip", "")
                            # print(root)
                            # print(newdirfromwalkname)
                            with zipfile.ZipFile(walknamefullpath) as openzip:
                                openzip.extractall(newdirfromwalkname)
                            dirstowalk.append(newdirfromwalkname)
        # create extension tallies and list of .xml and .pdf files to copy
        total_files = 0
        total_dirs = 0
        totaltocopy = 0
        # write new allfiles/filestocopy txts in case dir is partially processed
        with open('%s\\filestocopy.txt' % atarballdestpath, 'w') as filestocopytxt:
            filestocopytxt.write('''''')
        with open('%s\\allfiles.txt' % atarballdestpath, 'w') as allfilestxt:
            allfilestxt.write('''''')
        # for each folder and file within that directory
        for root, dirs, files in os.walk(atarballdir):
            for eachdir in dirs:
                if "__MACOS" not in eachdir:
                    total_dirs +=1
            for name in files:
                if name.startswith('._') == False:
                    full_file_path = os.path.join(root, name)
                    file_name, file_ext_uc = os.path.splitext(full_file_path)
                    file_ext = file_ext_uc.lower()
                    if file_ext == '.xml' or file_ext == '.pdf':
                        totaltocopy += 1
                        with open('%s\\filestocopy.txt' % atarballdestpath, 'a') as filestocopytxt:
                            filestocopytxt.write('''%s\n''' % full_file_path)
                        # print(full_file_path)
                    with open('%s\\allfiles.txt' % atarballdestpath, 'a') as allfilestxt:
                            allfilestxt.write('''%s\n''' % full_file_path)
                    total_files += 1
        # use robocopy to transfer individual files from filestocopy.txt
        with open('%s\\filestocopy.txt' % atarballdestpath, 'r') as filestocopyinput:
            txtfilepaths = (filestocopyinput.read()).split('''\n''')
        robologpath = "/unilog+:%s\\transferlog.txt" % atarballdestpath
        roboerrorspath = "%s\\roboerrors.txt" % atarballdestpath
        erroracc = 0
        successacc = 0
        for filepath in txtfilepaths:
            if filepath != '':
                filename = os.path.basename(filepath)
                filedir = os.path.dirname(filepath)
                robodestination = filedir.replace(drivepath, destinationroot)
                roboresult = subprocess.run(["robocopy", filedir, robodestination, "/COPY:DAT", "/mt", "/w:1", "/r:1", "/np", "/V", "/tee", robologpath, filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if int(roboresult.returncode) >= 8:
                    roboresult_output = '''%s\n%s\n%s\n\n\n''' % (roboresult.returncode, roboresult.stdout, roboresult.stderr)
                    erroracc += 1
                    with open(roboerrorspath, 'a') as errorsfile:
                        errorsfile.write('''%s\n\n\n''' % roboresult_output)
                else:
                    successacc += 1
        # all done, now summarize
        summarytext = '''original tarball path: %s\nnumber of files copied: %s\nnumber of copy errors: %s\ntotal number of files: %s\ntotal number of directories: %s\n''' % (atarball, successacc, erroracc, total_files, total_dirs)
        with open(summarypath, 'a') as summary:
                summary.write(summarytext)
        body = (summarytext)
        subject = '''%s pdf and xml transfer complete''' % atarballbasename
        print(subject)
        print(summarytext)
        # remove working dir created in source location
        shutil.rmtree(atarballdir)