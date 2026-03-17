import os

def get_uploaded_images(upload_folder):
    #rootdir = os.getcwd()
    #print rootdir
    filenames = []
    upload_path = os.path.join(os.getcwd(), upload_folder)
    for subdir, dirs, files in os.walk(upload_path):
        for file in files:
            #print os.path.join(subdir, file) 
            filenames.append(file)
    return filenames