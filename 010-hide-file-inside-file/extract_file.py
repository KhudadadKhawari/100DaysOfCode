class Error(Exception):
    """base class for other exceptions"""
    pass

class InstructionsFileNotFoundError(Error):
    """raised when instructions text file not found or couldn't open"""
    pass

class MainFileNotFoundError(Error):
    """Raised when the main file is not found"""
    pass

class WrongFileSelectedError(Error):
    """Raised when the wrong Main File is Selected """
    pass

def extraction_details(url):
    """
    returns a dictionary of extractions details from the url (instructions file)
    url = instructions file [text file]

    return values:
    {hex : [last_hex], file type: [the extension of the secret file was hidden inside the src file] }
    """
    try:
        with open(url, 'r') as instrut:
            content = instrut.read()
            # print(content)
            file_extension = content.partition('\n')[0]
            last_hex = content.split('\n')[1].replace('b\'','').replace('\'','')
            return {'hex':last_hex, 'file_type':file_extension}
    except FileNotFoundError:
        raise FileNotFoundError



def extract_file_from(src,instructions):
    """
    Extracts the Hidden file from the src file using infromation from instructions file

    src = The File contains the Hidden File (The Secret File) data
    instructions = The Text file [Contains the Extension of The hidden file (The Secret File) and a byte from the src file]
    """
    try:
        instructions = extraction_details(instructions)
        file_type = instructions['file_type']
        hex = instructions['hex']
        file_name = f'Exported.{file_type}' # name for the hidden file which is gonna exported
    except FileNotFoundError:
        raise InstructionsFileNotFoundError
 


    try:
        with open(src,'rb') as f, open(file_name, 'wb') as result:    
            content = f.read()
            try:
                offset = content.index(bytes.fromhex(hex)) # finding the position of the hex valie (form instruction file) in the src file

            except ValueError:
                raise WrongFileSelectedError
            
            f.seek(offset + 2) # changes the cursor position
            result.write(f.read()) 
    except FileNotFoundError:
        raise MainFileNotFoundError


        
