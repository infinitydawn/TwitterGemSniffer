from fileinput import filename
import gspread
from collections import Counter
import time

list1 = ['a1','a1','a3','a4','a5']
# asx = Counter(list1)
# print(asx)

sa = gspread.service_account()




# wks.update_cell(3,5,"Big")

def write_sheet(matchlist):
    sh = sa.open("TwitterParser")

    wks = sh.worksheet(openSheet().title)

    formatedList = []

    commonElems = matchlist.most_common()

    print(commonElems[0][1])

    for i,elem in enumerate(commonElems):
        tempDict= {"range": "A"+str(i+1)+":B"+str(i+1), "values" : [[elem[0],elem[1]]]}
        formatedList.append(tempDict)
    
    tenthList = formatedList[int(len(formatedList) * 0) : int(len(formatedList) * .1)]
    print(len(tenthList))
    print(len(formatedList))
    wks.batch_update(tenthList)
    print(tenthList)    
        

#shName =input("Input the name of the sheet: ")

def openSheet():
    sh = sa.open("TwitterParser")
    while True:
        
        # Try to input the sheet name
        try:
            shName = input('Input worksheet name: ')
            worksheet = sh.worksheet(shName)
            print("\n"+shName+" already exists!")
            while True:
                print("\nWould you like to clear sheet '"+shName+"' before writing?")
                tempInp = input("Enter y/n: ")
                if(tempInp == "y"):
                    # Clear sheet
                    print("\nPressed yes. Clearing Sheet")
                    worksheet.clear()
                    return worksheet
                    
                elif(tempInp == "n"):
                    print("\nYou chose not to clear sheet. Writing over anything that was in it before.")
                    worksheet.update_cell(3,6,"#2")
                    return worksheet

                else:
                    print("Wrong choice! Choose y/n. Try again!")      
            
                    
            
                        
            
        
        # Outcome if sheet doesn't exist
        except:
            print("This sheet doesn't exist!") 
            while True:
                print("Would you like to make a new worksheet named '"+shName+"'?") 
                tempInp = input("Enter y/n: ")
                if(tempInp == "y"):
                    newSh = sh.add_worksheet(title=shName, rows=10000, cols=50)
                    return newSh
                elif(tempInp == "n"):
                    print("no")
                    break
                else:
                    print("Wrong choice! Choose y/n. Try again!")  
            
    
def monitorSheet(sheetName, newFollowedList, Date):
    try:

        sh = sa.open("Monitor_Bot")
        
        totalSheet = sh.worksheet("Total")

        

        values_list = totalSheet.col_values(1)
        rowVals = totalSheet.row_values(1)
        frmtdDate = Date.replace("-","/")

        if Date not in rowVals:
            print("~"+Date+"~ VS ~"+frmtdDate)
            # APPEND A COLUMN
            print("Before there are: "+str(totalSheet.col_count))
            totalSheet.add_cols(1) 
            #time.sleep(20)
            sh = sa.open("Monitor_Bot")
            totalSheet = sh.worksheet("Total")
            print("Now there are: "+str(totalSheet.col_count))
            
            

        if sheetName not in values_list:
            #print("#")
            #linkWS = sh.worksheet(sheetName)
            #wsID = linkWS.id
            #totalSheet.append_row(["=HYPERLINK('#gid="+wsID+"','"+sheetName+"')"])
            totalSheet.append_row([sheetName])
            #MAKE ROW

        # GET ROW NUMBER TO WRITE VALUES
        cell = totalSheet.find(sheetName)
        rowNum = cell.row

        

        #Get A Column Number To Write A Date
        # ColNum = list(filter(None, totalSheet.row_values(1)))
        # print("COLNUM is: "+str(ColNum))
        # lastCol = str(len(ColNum))
        
        lastCol = totalSheet.col_count
        print("lastCol is: "+str(lastCol))

        
        

        # ADD DATE COLUMN
        totalSheet.update_cell(1, lastCol, Date)
        
        # ADD VALUE COL
        totalSheet.update_cell(rowNum, lastCol, len(newFollowedList))





        #Try to make a new sheet
        try:
            worksheet = sh.worksheet(sheetName)
            print("\n"+sheetName+" already exists!")
        except:
            print("This sheet doesn't exist!")
            worksheet = sh.add_worksheet(title=sheetName, rows=1, cols=2)
            worksheet.append_row(["Date", "Followed"])
        
        # GET EMPTY ROW
        str_list = list(filter(None, worksheet.col_values(1)))
        lastRow = len(str_list)+1
        print(lastRow)

        # CREATE ROW OBJECT
        cellVal=""
        for i in newFollowedList:
            cellVal+=i+"\n"

        print(cellVal)    
        # tempDict= {"range": "A"+lastRow+":B"+lastRow, "values" : [[elem[0],elem[1]]]}

        # WRITE ROW TO LIST
        worksheet.append_row([Date, cellVal])
    except Exception as e:
        print(e)
    
    

    

                

#monitorSheet("user_3_total", ["user4","user5","user7"], "02/07/2022")
    
# sh = sa.open("Monitor_Bot")
        
# totalSheet = sh.worksheet("Total")


# rowVals = totalSheet.row_values(1)
# if "05/01/2022" not in rowVals:
#     print("true")
# print(rowVals)




#    for match,i in matchlist.items():
#        print(list(matchlist.keys())[i])
       
#    wks.batch_update([{"range": "A8:C8", 
#                     "values" : [["Texas", 5261485, 5261485]]},
#                      {"range": "A9:C9", 
#                     "values" : [["Wisconsin", 1630673, 1610065]]},
#                     ])
   # wks.append_rows(values=[["Pennsylvania", 3458312, 3376499]])
   
   
   
    # print(list(matchlist.values())[0])
    
    # for match,i in matchlist.items():
    #     print(i)
    #     wks.update_cell(i+2,1,list(matchlist.keys())[i])
    #     wks.update_cell(i+2,2,list(matchlist.values())[i])

# Try to input the sheet name
  
                    
                    
               