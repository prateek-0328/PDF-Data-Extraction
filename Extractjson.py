import os,zipfile
# This function is used to extract all the zipped files present in the zippedjsonoutput folder and then 
# create a new folder jsonoutput which has different folders for different unzipped json files and each 
# folder consists the json file for each teswtcase pdf provided.
def Extractjson():
    directory = os.path.dirname(os.path.abspath(__file__))+"\zippedjsonoutput"
    # Listing all files in the directory
    file_names = os.listdir(directory)
    for file in file_names:
        zip_path = directory+"\\"+file
        # Open the zip file
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            # Extract all files in the zip file
            zip_ref.extractall(os.path.dirname(directory)+"\jsonoutput"+"\\"+file[0:-4])
