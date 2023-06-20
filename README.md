# PDF-Data-Extraction
This project is created for the Hackathon "Papyrus Nebulae" round 1 organized by Adobe. The goal of this project is  "Extracting information from PDF invoices using Adobe PDF Services Extract API". The extracted data is then sorted and stored in a CSV file.

# Code Prerequisites:
-all the test files must be in the same directory and no other directory must be present in the Test directory file
- The API credential and private key must be in the same directory as that of the Main.py file.

- The Final CSV Output file consists of the output for the TestDataSet that was provided. If the code is run again the output will again be generated but it will be in the same directory as that of Main.py
- The zippedjsonoutput file contains all the zipped files that are extracted using the Adobe API. If the code is run again then these files will be rewritten.
- The jsonoutput file contains the folders which have unzipped JSON files ready to be used in them. If the code is run again then the same folders will be recreated and the JSON files will be updated accordingly.

# The code starts from the Main.py file and this file calls all the other necessary functions from other files to generate the output 
