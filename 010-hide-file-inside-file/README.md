# Hide Secrete File inside another File
## Description
This Application is Designed to Hide a file inside another file. In current version you can't hide more than one file inside another file.<br>
There are **Two** scripts which perform the actions.<br>
The **main .py** contains The User interface which is made with Tkinter. <br>
The **hide_file .py** contains the script for hidding a file<br>
And the **extract_file .py** contains the script for Extracting the Hidden file from a file which u used to hide another file inside it previously.<br>

### hide_file.py
To use this script you need to import the **hide_inside_file** function from it. This function gets Two Arguments:<br>
**src:** This is the path and name of File that you want to hide. This file will be deleted after the process is done<br> 
**dest:** This is the path and name of File that you want to hidde the **src** file inside it <br>

This function will create another extra file [instructions.txt], which contains the info for extracting the hidden file and you will have to  use it later with the extraction script to extract the hidden file

### extract_file.py
To use this script you need to import the **extract_file_from** function from it.<br>
This function takes two arguments:<br>
**src:** takes the path and file name of the file that contains the hidden file  <br>
**instructions:** takes the path and name of the instructions.txt file which contains the details for the extraction of the hidden file.<br>

This function will extract the Hidden file and save it to current directory. <br>
In current version it doesn't delete the hidden file from the src file so the file may contain the hidden file after the extraction too. 
