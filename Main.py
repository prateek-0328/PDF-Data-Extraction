import os,ExtractData,getZipFiles,ExtractData,Createcsv,Extractjson
#this is the main function for the code file. The main function takes in the input as 
# the name of the directory in which all the Test invoice pdfs are stored. Note that this 
# directory should be present in the same directory as that of the Main.py file. 
def Main(TestDataSet):
    directory = os.path.dirname(os.path.abspath(__file__))+ "\\"+TestDataSet
    file_names = os.listdir(directory)
    for file in file_names:
        getZipFiles.getZipFiles("\\"+TestDataSet+"\\"+file,file[:-4]+".zip")
    Extractjson.Extractjson()
    directory=os.path.dirname(directory)+"\\"+"jsonoutput"
    files=os.listdir(directory)
    data=[]
    for dir in files:
        try:
            data.extend(ExtractData.ExtractData(directory+"\\"+dir+"\\"+"structuredData.json"))
            print(dir+" Extracted Successfully!")
        except:
            print("error in file "+ dir)
            continue
    Createcsv.Createcsv(data)

Main("TestDataSet")