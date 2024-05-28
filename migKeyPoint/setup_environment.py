import zipfile
import os
import shutil

def unzip_directory(zip_file_path, extract_to):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def makedirs():
    paths = ['data/raw_simulation/','darks/','models/']
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

def main(zip_file_path = 'zipped_files.zip',extract_to=''):
    if not os.path.exists("zipped_files.zip"):
        raise OSError("Script will not run unless there is a zipped_files.zip file to unzip!")
    print("Unzipping zipped_files.zip")
    unzip_directory(zip_file_path, extract_to)
    print("Done!\n")
    print("Making relevant directories\n")
    makedirs()
    print("Moving files\n")
    shutil.move("zipped_files/ERs_cont_spectrum_correctE.feather","data/raw_simulation/ERs_cont_spectrum_correctE.feather")
    shutil.move("zipped_files/MIG_Dark_0V_230803T130339.DARK.0001.MTIFF","darks/MIG_Dark_0V_230803T130339.DARK.0001.MTIFF")
    shutil.move("zipped_files/master_dark_230803.npz","darks/master_dark_230803.npz")
    shutil.move("zipped_files/pretrained/",".")
    print("Cleaning up\n")
    os.remove("zipped_files.zip")
    os.rmdir("zipped_files/")
    print("SUCCESS!")

if __name__ == '__main__':
    main()
