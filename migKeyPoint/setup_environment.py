import zipfile
import os
import shutil

def unzip_directory(zip_file_path, extract_to):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def main(zip_file_path = 'zipped_data.zip',extract_to=''):
    if not os.path.exists("zipped_data.zip"):
        raise OSError("Script will not run unless there is a zipped_data.zip file to unzip!")
    print("Unzipping zipped_data.zip")
    unzip_directory(zip_file_path, extract_to)
    print("Done!\n")
    print("Moving files\n")
    shutil.move("zipped_data/simulation",".")
    shutil.move("zipped_data/darks",".")
    shutil.move("zipped_data/pretrained/",".")
    print("Cleaning up\n")
    #os.remove("zipped_data.zip")
    #os.rmdir("zipped_data/")
    print("SUCCESS!")

if __name__ == '__main__':
    main()
