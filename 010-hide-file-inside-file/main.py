from tkinter import *
from tkinter import filedialog
from hide_file import DestinationFileNotFoundError, SourceFileNotFoundError, hide_inside_file
from extract_file import InstructionsFileNotFoundError, MainFileNotFoundError, WrongFileSelectedError, extract_file_from


root = Tk() # Main Window Where User choose to Hide/Export Secrete File
root.minsize(width=400, height=400)
root.title('Hide/Export Secrete File')

def hiding_func(): 
    """
    Fucntion: Opens A new window that contains the approperiate widgets for Performing "hiding file"
    only passed to command argument of a button
    """
    root.destroy() #closes the root window after openning the new window

    new_window = Tk()
    new_window.minsize(width=400, height=400)
    new_window.title('Hide Secrete File')

    src = Label(new_window,text="Please Select File to be hidden!\n Warning: The Source File will be deleted after The Process")
    src.grid(row = 0, column = 0)

    dest = Label(new_window,text="Please Select File to hide inside")
    dest.grid(row = 1, column = 0)

    # opens Source File URL
    def open_src():
        filename =filedialog.askopenfilename(filetypes=(("jpg files","*.jpg"),("All files","*.*")))
        src.config(text=filename)

    # Opens Destination File URL
    def open_dest():
        filename =filedialog.askopenfilename(filetypes=(("jpg files","*.jpg"),("All files","*.*")))
        dest.config(text=filename)

    # Does the Hiding Process
    def hide_into():
        src_url = src.cget('text')
        dest_url = dest.cget('text')
        try:    
            hide_inside_file(dest=dest_url, src=src_url)
            new_window.destroy()
        except SourceFileNotFoundError:
            src.config(text="Please Open Source File Before Clicking on \" Start File Hidding \" button")
        except DestinationFileNotFoundError:
            dest.config(text="Please Open Destination File Before Clicking on \" Start File Hidding \" button")

    src_btn=Button(new_window,text="Open Source File",font=40,command=open_src)
    src_btn.grid(row=0,column=2)

    dest_btn=Button(new_window,text="Open Destination file",font=40,command=open_dest)
    dest_btn.grid(row=1,column=2)

    hide_file=Button(new_window,text="Start File Hidding",font=40,command=hide_into)
    hide_file.grid(row=3,column=1)

    new_window.mainloop()

def extraction_func():
    """
    Fucntion: Opens A new window that contains the approperiate widgets for Performing "Extracting the secret file"
    only passed to command argument of a button
    """
    root.destroy() # closes the Previous window
    new_window = Tk()

    new_window.minsize(width=400, height=400)
    new_window.title('Extract Secrete File')

    main_file = Label(new_window,text="Select File Containing the Hidden file")
    main_file.grid(row = 0, column = 0)

    instructions_file = Label(new_window,text="Select The Instructions File")
    instructions_file.grid(row = 1, column = 0)

    def open_main_file():
        filename =filedialog.askopenfilename(filetypes=(("jpg files","*.jpg"),("All files","*.*")))
        main_file.config(text=filename)

    def open_instructions_file():
        filename =filedialog.askopenfilename(filetypes=(("txt files","*.txt"),("All files","*.*")))
        instructions_file.config(text=filename)

    def start_extraction():
        main_file_url = main_file.cget('text')
        instructions_file_url = instructions_file.cget('text')
        # hide_inside_file(dest=dest_url, src=src_url)
        try:
            extract_file_from(src=main_file_url, instructions=instructions_file_url)
            new_window.destroy()
        except InstructionsFileNotFoundError:
            instructions_file.config(text="Please Open Instructions File Before clicking on \"Start File Extraction\" Button ")
        except MainFileNotFoundError:
            main_file.config(text='Please Select Main File Before Clicking on \"Start File Extraction\" Button')
        except WrongFileSelectedError:
            main_file.config(text="Wrong File Selected Please Select the File That Contains the Secret File")

    main_File_btn=Button(new_window,text="Open Main File",font=40,command=open_main_file)
    main_File_btn.grid(row=0,column=2)

    instructions_file_btn=Button(new_window,text="Open Instructions file",font=40,command=open_instructions_file)
    instructions_file_btn.grid(row=1,column=2)

    extract_file=Button(new_window,text="Start File Extraction",font=40,command=start_extraction)
    extract_file.grid(row=2,column=1)

    new_window.mainloop()

title_display = Label(root,text="Choose what You want")
title_display.grid(row = 0, column = 0)

hidn_file_btn=Button(root,text="Hide File",font=40, command=hiding_func)
hidn_file_btn.grid(row=1,column=1)

hidn_file_btn=Button(root,text="Export File",font=40, command=extraction_func)
hidn_file_btn.grid(row=2,column=1)

root.mainloop()