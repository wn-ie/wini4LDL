# wini4LDL
## general requirements
In order to run this code, you'll need python, the python requests module, and access to a specific OneDrive folder using the desktop application.

To download python on Windows (for free, if it costs money then it's the wrong application!) by searching the Microsoft Store for "python" or going to the following link:
https://www.microsoft.com/store/productId/9NRWMJP3717K

To run on a windows computer, save the file locally, then open a new command prompt window (by pressing the start button and then typing 'cmd') and type "py", followed by the path of the file you want to run.
For example, `py P:\ath\to\GitHub\wini4LDL\CheckForFilePairs.py` or `py P:\ath\to\GitHub\wini4LDL\RunRawGitHub.py`

Any further instructions or information will appear in the command line window, do NOT modify the python file.

## untar_unzip_xfer.py
### untar_unzip_xfer specific requirements
To run this file, you'll also need the python requests module. To install requests, make sure python is installed (via the microsoft store, see above) and then open the command prompt by pressing the start button and then typing 'cmd'. In the command prompt window that opens, type the following:
`pip install requests`

You'll also need access to the following OneDrive folder:
`https://lsumail2-my.sharepoint.com/:f:/g/personal/wschlin_lsu_edu/ElNhf_pbWD5KiAq9UTwJnd0BQhvlJQC10MNSDInGaES4sA`
If you don't have access, email Winnie (wschlin@lsu.edu) to get access. Once you have access, open the OneDrive application on your computer, find the path to the folder, and email it to Winnie (this is in order to get syncing to happen from your computer).

### untar_unzip_xfer use instructions
To use this code on materials, you'll use the windows command prompt (which you can find by pressing the start button and then typing 'cmd') and you can paste a command which has 5 components, a non-working sample/template of it looks like this:

py P:\ath\to\RunRawGitHub.py https://github.com/WinnieSchLin/wini4LDL/blob/main/untar_unzip_xfer.py P:\ath\to\SOURCE\drive P:\ath\to\DESTINATION\drive

If you forget to include any of these components, don't worry! This is just a shortcut, the code will ask you in the command prompt window and you can enter everything then.

#### explanation of components
`py`  
Indicates this is a python command. This will always be the same.

`P:\ath\to\RunRawGitHub.py`  
The location of the python code file (RunRawGitHub.py). This will change depending on where your version of this file is located.

`https://github.com/WinnieSchLin/wini4LDL/blob/main/untar_unzip_xfer.py`  
The GitHub link to the code that does the untarballing / unzipping / transfer. This will always be the same.

`"P:\ath\to\SOURCE\drive"`
The location of the source files, so the path to the hard drive (probably something like 'D:\' or 'E:\'). Make sure to use quotation marks!

`"P:\ath\to\DESTINATION\drive"`
The location of where you want the destination to be, probably a folder in either the R Drive or P Drive. Make sure to use quotation marks!

The command that you come up with (from substituting the above components where necessary) may change slightly between harddrives (maybe harddrive1 is '"D:\"' but harddrive2 is '"E:\"', or the destinations are '"R:\afolder\harddrive1"' and '"R:\afolder\harddrive2"' respectively, but they should generally be pretty similar and potentially copy-and-pastable!
