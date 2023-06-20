import csv
# Creates a csv file by taking in input as the data extracted from all the test files.
def Createcsv(data):
    with open("ExtractedData.csv","w",newline='') as file:
        writer = csv.writer(file)
        dataheader=["Bussiness__City","Bussiness__Country",	"Bussiness__Description",	"Bussiness__Name",	"Bussiness__StreetAddress",	"Bussiness__Zipcode",	"Customer__Address__line1",	"Customer__Address__line2",	"Customer__Email",	"Customer__Name",	"Customer__PhoneNumber",	"Invoice__BillDetails__Name",	"Invoice__BillDetails__Quantity",	"Invoice__BillDetails__Rate",	"Invoice__Description",	"Invoice__DueDate",	"Invoice__IssueDate",	"Invoice__Number",	"Invoice__Tax"]
        data.insert(0,dataheader)
        writer.writerows(data)
    print("csv generated successfully")