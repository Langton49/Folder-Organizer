import os
import shutil
import mimetypes

def cleanUp(filePath):
    if os.path.exists(filePath) and os.path.isdir(filePath):
        documentTypes = [
                'application/pdf',
                'application/msword',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                'application/vnd.ms-powerpoint',
                'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                'application/vnd.openxmlformats-officedocument.presentationml.slideshow',
                'application/vnd.openxmlformats-officedocument.presentationml.template',
                'application/vnd.ms-excel',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.template'
            ]
        for files in os.listdir(filePath):
            source = os.path.join(filePath, files)
            fileType, _ = mimetypes.guess_type(source)
            category = None
            if fileType:
                if fileType.startswith("image"):
                    category = "Pictures"
                elif fileType.startswith("audio"):
                    category = "Audio"
                elif fileType.startswith("video"):
                    category = "Videos"
                elif fileType.startswith("application/x-zip-compressed") or fileType.startswith("application/x-compressed"):
                    category = "Compressed"
                elif any(fileType.startswith(doc) for doc in documentTypes):
                    category = "Documents"
                elif fileType.startswith("application/x-msdownload"):
                    category = "Executables"
                else:
                    category = "Miscellaneous"
            elif not os.path.isdir(source):
                category = "Miscellaneous"
            
            if category:
                destination = os.path.join(filePath, category)
                os.makedirs(destination, exist_ok=True)
                try:
                    shutil.move(source, destination)
                except Exception as e:
                    print(f"Unexpected error: {e}")

if __name__ == "__main__":
    filepath = input("Enter Path to Folder: ")
    cleanUp(filepath)
    print("Cleanup Successful!")
    

