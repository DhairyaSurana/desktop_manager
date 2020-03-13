import os
import magic
import mimetypes

# MIME types list: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types

def moveFile(orig_path, new_path):
    if(orig_path != new_path and new_path is not None):
        os.rename(orig_path, new_path)

def getType(file_path):

    content_type = None

    try:    # Reads the file to determine the type
        content_type = magic.from_file(file_path, mime=True)
    except: # In case there are issues with reading the file
        content_type =  mimetypes.MimeTypes().guess_type(file_path)[0]

    content_type =  mimetypes.MimeTypes().guess_type(file_path)[0]

    return content_type

def createDirs():

    doc_path = os.path.expanduser("~/Desktop/Documents")
    img_path = os.path.expanduser("~/Desktop/Images")
    
    if not os.path.isdir(doc_path):
        os.makedirs('Documents')

    if not os.path.isdir(img_path):
        os.makedirs('Images')


if __name__ == "__main__":

    print(__file__)

    current_path = os.path.dirname(os.path.abspath(__file__))
    desktop_path = os.path.expanduser("~\Desktop")

    if(current_path != desktop_path):
        print("Error: Clean_Desktop.py must be in the Desktop")
    else:

        createDirs()

        xlsx_mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        docx_mime = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        pdf_mime = "application/pdf"
        txt_mime = "text/plain"
        png_mime = "image/png"
        jpg_mime = "image/jpeg"
        pptx_mime = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        unknown_mime = "application/octet-stream"

       
        
        try:
            for file in os.listdir():

                file_path = os.path.join(current_path, file)
                new_path = None 

                if(os.path.isfile(file_path) and ".py" not in file):
                    
                    content_type = getType(file_path)
                    
                    if(content_type in (docx_mime, pdf_mime, txt_mime, xlsx_mime, pptx_mime)):
                        new_path = os.path.join(current_path, "Documents", file)
                                            
                    elif(content_type == png_mime or content_type == jpg_mime):
                        new_path = os.path.join(current_path, "Images", file)

                    moveFile(file_path, new_path)


        except Exception as e:
            print(e)
        

    


            