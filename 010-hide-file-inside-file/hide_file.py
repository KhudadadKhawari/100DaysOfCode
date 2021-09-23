class Error(Exception):
    """Base Class for all exceptions"""
    pass


class SourceFileNotFoundError(Error):
    """Raised When Source File not selected or Couldn't Imported"""
    pass


class DestinationFileNotFoundError(Error):
    """Raised When Destination File not Selected or Couldn't Imported"""
    pass


# Extracts the File Extension which is going to be hidden 
def extract_file_extension(url):
    """Extracts The File Extension and save it before hiding the src file
    It will be needed for Extracting the src file again from the dest file
    """
    if '.' in url: # if that is really a url it will contain a "." Before file extension
        reverse_filename = url[::-1]
        v_ext = ''
        for a in reverse_filename:
            if a =='.':
                break
            v_ext += a
        return v_ext[::-1]
    else: # if any way couldn't open the file from url or find some files without extension
        raise SourceFileNotFoundError


import binascii
import os

def hide_inside_file(src, dest ):
    """Hides the Source (src) File inside the Destination (dest) File
    src = The file you want to hide (The Secret File)
    dest = The file Which will hide the src file (The Secret FIle) data inside it
    """
    try: 
        with open(dest, 'rb') as read_from_file:
            binary_file = read_from_file.read()

            # Finds the Last Bytes location in the file 
            reverse_str = binary_file[:-3:-1]
            extracted_charachters = reverse_str[::-1]
            lastbytes = binascii.hexlify(extracted_charachters)

            # Saving the src file extension and the last byte of the dest file in the "instructions.txt"
            # which is used for extracting the src file from dest file in Furture
            try:
                with open('instructions.txt','w') as txt:
                    extension = extract_file_extension(src)
                    txt.write(f'{extension}\n')
                    txt.write(str(lastbytes))
            except FileExistsError:
                with open('instructions.txt', 'w') as txt:
                    extension = extract_file_extension(src)
                    txt.write(f'{extension}\n')
                    txt.write(str(lastbytes))
            except SourceFileNotFoundError:
                raise SourceFileNotFoundError
    except FileNotFoundError:
        raise DestinationFileNotFoundError

    try:
        # Opens both src and dest files and writes the src file inside the dest file
        with open(dest, 'ab') as write_to_file, open(src, 'rb') as read_from_file:
            write_to_file.write(read_from_file.read())
        os.remove(src) # Delete the src file after hidding it inside the dest file

    except FileNotFoundError:
        raise SourceFileNotFoundError


