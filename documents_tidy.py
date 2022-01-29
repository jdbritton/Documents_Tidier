# ==============================================================================
# documents_tidy.py
#
# Tidies up the documents folder.
# Ran via Task Scheduler
# ==============================================================================
# Imports:
# ==============================================================================

import os, shutil
from colorama import Style, Fore, init
from time import process_time,sleep

os.chdir("H:\\data") # change dir to your documents folder
source_directory = os.getcwd()

init()
cyan = Fore.CYAN
yellow = Fore.YELLOW
bold = Style.BRIGHT
green = Fore.GREEN
reset = Fore.RESET
sreset = Style.RESET_ALL

###  Add new ones o' these for different kinds of files to be ordered.  ###
# MSG files (emails)
msg_dir = "H:\\data\\Emails" 
msg_files = []

pdf_dir = "H:\\data\\PDFs" 
pdf_files = []

docx_dir = "H:\\data\\Docs" 
docx_files = []


###  Defining the function to actually move the files.  ###
def movefiles(files_to_move,source_directory,target_directory):
    t_start = process_time()
    file_count = 0
    try:
        for file in files_to_move:
            shutil.move(file, target_directory)
            file_count += 1
        print(f"{yellow}{bold}Number of files moved: {file_count}{reset}")
        t_stop = process_time()
        total_time = t_stop-t_start
        print(f"{yellow}{bold}Total time taken for these files in secs: {total_time}{reset}")
    except:
        print("Some error occured. What error? Who cares, moving on.")
    finally:
        print(f"{green}============================{reset}\n")


###  Add things to the lists that we'll be working with  ###

### .MSG Files
for file in os.listdir():
    if file.endswith(".msg"):
        msg_files.append(file)

### .PDF Files
for file in os.listdir():
    if file.endswith(".pdf"):
        pdf_files.append(file)

### .PDF Files
for file in os.listdir():
    if file.endswith(".docx"):
        docx_files.append(file)


# Add more lists above and add more functions below if you want to handle other kinds of files

# ==============================================================================
# >>>  Do the actual moving: 
# ==============================================================================
print(f"{green}{bold}============================{reset}\n")

print(f"{cyan}{bold}Moving .msg files.{reset}{sreset}")
movefiles(msg_files,source_directory,msg_dir)
print(f"{cyan}{bold}Moving .pdf files.{reset}{sreset}")
movefiles(pdf_files,source_directory,pdf_dir)
print(f"{cyan}{bold}Moving .docx files.{reset}{sreset}")
movefiles(docx_files,source_directory,docx_dir)

print("Done.")
sleep(10)
