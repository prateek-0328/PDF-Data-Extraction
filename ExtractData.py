import json
#This function takes in the input of the absolute path of a json file and then returns the relevant 
# data extracted from that file in the form of a list.
def ExtractData(filepath):
    # retrieving all the data from the json file
    with open (filepath) as file:
        data= json.load(file)
    totalIDs = len(data["elements"])
    # this function can be used to get any type  of information related to an element in the data using its ID
    def getDatfromID(id,info):
        return(data["elements"][id-1][info])    
    # this is a dictionary which contains keys as id and value as text for all the elements which have text in it
    l={}
    i = 0
    for element in data["elements"]:
        i+=1
        try:
            l[i]=element["Text"]
        except KeyError:
            continue
    # function used to retrieve BussinessName from the data
    def getBussinessName():
        Bussiness__Name=""
        Bussinessid=0
        for id in l:
            if (getDatfromID(id,"TextSize")>20):
                Bussiness__Name+=l[id]
                Bussinessid=id
                break
        return Bussiness__Name,Bussinessid
    # function used to retrive the Bussiness__Description using business name
    def getBussiness__Description(id):
        Bussiness__Description=l[id+1]
        return Bussiness__Description,id+1
    # function to retrieve all the data present above the Bussiness name using the businessName id
    def getInvoiceAndBussinessDetails(BussinessNameid):
        Invoiceinfo=""
        Bussinessinfo=""
        for id in l:
            if id<BussinessNameid :
                if(getDatfromID(id,"Bounds")[2]>540):
                    Invoiceinfo+=l[id]
                elif (getDatfromID(id,"Bounds")[0]<78):
                    Bussinessinfo+=l[id]
        try:
            Invoice__Number,Invoice__IssueDate=Invoiceinfo.split("Issue date")
            Invoice__IssueDate=Invoice__IssueDate.strip()   #
            Invoice__Number=Invoice__Number.split("Invoice#")[-1].strip()#
            Bussinessinfo=Bussinessinfo.split()
            Bussiness__Zipcode=Bussinessinfo[-1]        #
            Bussiness__Country=(Bussinessinfo[-3]+" "+Bussinessinfo[-2])        #
            Bussiness__City=Bussinessinfo[-4].split(",")[0]         #
            Bussiness__StreetAddress=Bussinessinfo[len(l[BussinessNameid].split()):-4]
            Bussiness__StreetAddress=" ".join(Bussiness__StreetAddress).split(",")[:-1][0]  #
        except Exception as e:
            print (e)
        return Invoice__IssueDate,Invoice__Number,Bussiness__Zipcode,Bussiness__Country,Bussiness__City,Bussiness__StreetAddress
    # function to retrieve details about customer and invoice using description id
    def getCustomerAndInvoiceDetails(Bussiness__Descriptionid):
        CustDetails=""
        Invoice__Description=""
        Invoice__DueDate=""
        for id in l:
            if id>Bussiness__Descriptionid:
                if getDatfromID(id,"Font")["name"].endswith("BoldMT") and l[id].strip()=="ITEM":
                    tablebegin=id
                    break
                elif getDatfromID(id,"Bounds")[0]<83:
                    CustDetails+=l[id]
                elif getDatfromID(id,"Bounds")[2]>500:
                    Invoice__DueDate+=l[id]
                else:
                    Invoice__Description+=l[id]
        Invoice__Description=Invoice__Description.split()
        for wrd in Invoice__Description:
            if(wrd.strip()=="DETAILS" ):
                Invoice__Description.remove(wrd)
            elif("PAYMENT"  in wrd):
                Invoice__Description.remove(wrd)
            elif("$"in wrd):
                Invoice__Description.remove(wrd)
        if(Invoice__Description[0]=="PAYMENT"):
            Invoice__Description.pop(0)
        elif("$" in Invoice__Description[-1]):
            Invoice__Description.pop()
        Invoice__Description=" ".join(Invoice__Description)
        Invoice__DueDate=Invoice__DueDate.split("Due date:")[-1].strip()        #
        CustDetails=CustDetails.split()
        CustDetails.remove('BILL')
        CustDetails.remove('TO')
        Customer__Name=CustDetails[0]+" "+CustDetails[1]        #
        del CustDetails[0:2]
        for word in CustDetails:
            if('-' in word):
                if(len(word)==12 and len(word.split('-'))==3):
                    Customer__PhoneNumber=word  #
                    CustDetails.remove(word)
                    break
        if('@' in CustDetails[0]):
            if('.com' in CustDetails[0]):
                Customer__Email=CustDetails[0]
                del CustDetails[0]
            else:
                Customer__Email=CustDetails[0]+CustDetails[1]       #
                del CustDetails[0:2]
        Customer__Address__line1=" ".join(CustDetails[0:3])     #
        del CustDetails[0:3]
        Customer__Address__line2=" ".join(CustDetails)      #
        return Invoice__Description,Invoice__DueDate,Customer__PhoneNumber,Customer__Name,Customer__Email,Customer__Address__line1,Customer__Address__line2,tablebegin
    # this functions retrieves the required details from the table using the index of the first table column "ITEM"
    def getTableDetails(tablebegin,tableend):
        Invoice__BillDetails__Name=[]
        Invoice__BillDetails__Quantity=[]
        Invoice__BillDetails__Rate=[]
        IDs=list(l)
        for index in range (len(IDs)):
            if(IDs[index]==tablebegin):
                first =IDs[index+4]
            elif(IDs[index]==tableend):
                last=IDs[index-7]
                break
        for row in range(first,last+5,8):
            Invoice__BillDetails__Name.append(l[row].strip())
            Invoice__BillDetails__Quantity.append(int(l[row+2]))
            Invoice__BillDetails__Rate.append(int(l[row+4]))
        return Invoice__BillDetails__Rate,Invoice__BillDetails__Quantity,Invoice__BillDetails__Name
    # function used to retrieve tax
    def getInvoice__Tax():
        keys=list(l.keys())
        for index in range(len(keys)):
            if("Total Due" in l[keys[index]].strip()):
                try:
                    Invoice__Tax=int(l[keys[index-1]].strip())
                except :
                    try:
                        Invoice__Tax=int(l[keys[index-1]].strip().split()[-1])
                    except:
                        Invoice__Tax=10
                
                Invoice__Taxid=keys[index-1]
                break

        return Invoice__Tax,Invoice__Taxid

    Bussiness__Name,BussinessNameid=getBussinessName()
    Bussiness__Description,Bussiness__Descriptionid=getBussiness__Description(BussinessNameid)
    Invoice__Tax,Invoice__Taxid=getInvoice__Tax()
    Invoice__IssueDate,Invoice__Number,Bussiness__Zipcode,Bussiness__Country,Bussiness__City,Bussiness__StreetAddress=getInvoiceAndBussinessDetails(BussinessNameid)
    Invoice__Description,Invoice__DueDate,Customer__PhoneNumber,Customer__Name,Customer__Email,Customer__Address__line1,Customer__Address__line2,tablebegin=getCustomerAndInvoiceDetails(Bussiness__Descriptionid)
    Invoice__BillDetails__Rate,Invoice__BillDetails__Quantity,Invoice__BillDetails__Name=getTableDetails(tablebegin,Invoice__Taxid)
    dat=[]
    for rows in range(len(Invoice__BillDetails__Name)):
        dat.append([Bussiness__City,Bussiness__Country,Bussiness__Description,Bussiness__Name,Bussiness__StreetAddress,Bussiness__Zipcode,Customer__Address__line1,Customer__Address__line2,Customer__Email,Customer__Name,Customer__PhoneNumber,Invoice__BillDetails__Name[rows],Invoice__BillDetails__Quantity[rows],Invoice__BillDetails__Rate[rows],Invoice__Description,Invoice__DueDate,Invoice__IssueDate,Invoice__Number,Invoice__Tax])
    return dat
# ExtractData(r"C:\Users\A V Support\OneDrive\Desktop\projects\PapyrusNebulae\jsonoutput\output1\structuredData.json")

