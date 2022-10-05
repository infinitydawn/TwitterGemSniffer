from sqlite3 import Date
import tweepy
import csv_mod
import os
import sheets
from collections import Counter
from tkinter import filedialog
# from tkinter import Tk
import tkinter as tk
from tkinter.filedialog import askdirectory
from datetime import date
from datetime import timedelta
import time
import sys
import tg_bot


# path = askdirectory(title='Select Folder') # shows dialog box and return the path
# print(path)  


""" access_token = "1394176113346293761-RkIQR52KvXcxmpO9BvMzgwtiQddbWn"
access_token_secret = "TzljZ4Pc0c3If9MeqLybN0HE2h5hq6u8ZaA5D9M2ciHDz"
consumer_key = "L418n7x5OS24WtOpcJp01AJys"
consumer_secret = "qBCr4A6CXsNpnNGhoAyrBDevJ39Wd4MRCAFkxf4yLgZnuTQx2F"
screen_name = "0x1526" """

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAIwbZwEAAAAA6MswMrUpRfqSFzjWvabbIOfYRX8%3Di7eUwoqby9C9gpkFNcXOInK7Y4dHbCU1lkKylYhOWO7ZuaJdI2',wait_on_rate_limit=True)



def getFollowers():
    # Read Parse List
    with open("parse_followers_list.txt") as file:
        parseList = [line.rstrip() for line in file]
        print("Total Profiles In Parse List: "+str(len(parseList))) 
    
    # Make A Folder To Save All Parsed Lists
    newFolder = input("Name the folder for the parsed lists: ")
    """ final_directory = os.path.join(os.getcwd(), r'new folder') """

    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, newFolder)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

   
    for profile in parseList:
        print("Now Parsing "+profile+"'s Account.")

        # Convert Username To a Numeric ID
        id = client.get_user(username=profile).data.id

        # Get All Users in Followers || Store them in Pages 1000 each
        usersFollowers = []

        # Each user is an object with username, id, etc... example: user.id
        for user in tweepy.Paginator(client.get_users_followers, id=id, max_results="1000").flatten():
            usersFollowers.append(user.username)
    
        # Write Followers to file
        with open(newFolder+"/"+profile+".txt", 'w+') as filehandle:
            for follower in usersFollowers:
                filehandle.write('%s\n' % follower)   
        
        print(profile+"'s Total Followers: "+str(len(usersFollowers)))



def getFollowing(monitorMode):
    try:
        # Read Parse List
        with open("parse_following_list.txt") as file:
            parseList = [line.rstrip() for line in file]
            print("Total Profiles In Parse List: "+str(len(parseList))) 
        
        nonExistUser = []
        for i in parseList:
            f = client.get_user(username=i)
            if  len(f.errors) != 0:
                print(len(f.errors))
                nonExistUser.append(i)
       
        
        l3 = [x for x in parseList if x not in nonExistUser]
        
        print("The following accounts are non-existent.")
        print(nonExistUser)

        parseList = l3

        print("\n\n\nthe New Parselist is...")
        print(parseList)

        resultList = []
        
        for profile in parseList:
            print("Now Parsing "+profile+"'s Account.")

        

            # Convert Username To a Numeric ID
            id = client.get_user(username=profile).data.id

            #print(id+" is related to "+profile)

            
            # Get All Users in Followers || Store them in Pages 1000 each
            usersFollowing = []
    

    
            # Each user is an object with username, id, etc... example: user.id
            # index=0
            # paginated = tweepy.Paginator(client.get_users_following, id=id, max_results="1000").flatten()
            # while index < len(paginated):
            #     usersFollowing.append(paginated[index])

            for user in tweepy.Paginator(client.get_users_following, id=id, max_results="1000").flatten():
                usersFollowing.append(user.username) 
            
            resultList.append(usersFollowing)    
        
        if not monitorMode:
            print("NON MONITOR")
            # Make A Folder To Save All Parsed Lists
            newFolder = input("Name the folder for the parsed lists: ")
            """ final_directory = os.path.join(os.getcwd(), r'new folder') """

            current_directory = os.getcwd()
            final_directory = os.path.join(current_directory, newFolder)
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)


            for i,followingList in enumerate(resultList):
                print("List length TEST: "+str(len(followingList)))
                # Write Followings to file
                with open(newFolder+"/"+parseList[i]+".txt", 'w+') as filehandle:
                    for user in followingList:
                        filehandle.write('%s\n' % user)   
            
            print(profile+"'s Total Following: "+str(len(usersFollowing)))     

        if (monitorMode):
            print("MONITOR MODE")
            print("Monitor Mode Enabled. Returning List...")
            return(resultList)
    except Exception as e:
        print(str(e)+"\nThis is a getfollowing error")

    


def compareLists():
    

    # Read Following
    print("Choose a file that will be compared to other files...")
    tempTargFoll = openFile()
    with open(tempTargFoll) as file:
        list1 = [line.rstrip() for line in file]
        print("Total "+tempTargFoll+" Following: "+str(len(list1)))

    targName = os.path.split(tempTargFoll)[1]  
    
    # Make A Folder To Save All Parsed Lists
    newFolder = input("Name the folder for the parsed lists: ")
    """ final_directory = os.path.join(os.getcwd(), r'new folder') """

    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, newFolder)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    # Read Second list Following
    files,folderPath = openFolder()

    for profileList in files:
        print("123123123 "+profileList+"!")

        # open the list
        with open(folderPath+"/"+profileList) as file:
            
            # Read every username from file
            followersList = [line.rstrip() for line in file]
            print("Total in "+profileList.replace(".txt", "")+"'s followers: "+str(len(followersList)))

            matchlist =[]

            #Find matches in 2 lists
            print("Looking for matches with "+targName.replace(".txt", "")+" in "+profileList.replace(".txt", ""))
            for user_l1 in list1:
                
                for user_l2 in followersList:
                    if(user_l2 == user_l1):
                        matchlist.append(user_l2)
            print(str(len(matchlist))+" matches found!\n\n")


            
            print("Saving matches to "+targName.replace(".txt", "")+"_x_"+profileList.replace(".txt", ""))
            with open(newFolder+"/"+targName.replace(".txt", "")+"_x_"+profileList.replace(".txt", "")+".txt", 'w+') as filehandle:
                for follower in matchlist:
                    filehandle.write('%s\n' % follower)

            print("Writing Overall Stats")
            with open(newFolder+"/"+targName.replace(".txt", "")+"_Overall_Stats.txt", 'a+') as filehandle:
                filehandle.write('%s\n' % str(str(len(matchlist))+" matches in "+profileList))

            print("writing overall stats to csv")
            csv_mod.write_csv_Compare(profileList, len(followersList),len(matchlist),newFolder+"/"+os.path.split(newFolder)[1],targName)    






    


def getListIntersect():
    inputUser = "empty"
    count = 0
   
    bigList = []

    # Open folder, get files
    files,folderPath = openFolder()

    for profileList in files:

        # open the list
        with open(folderPath+"/"+profileList) as file:
            
            # Read every username from file
            followersList = [line.rstrip() for line in file]
            print("Total in "+profileList.replace(".txt", "")+"'s followers: "+str(len(followersList)))

            # Put every user name in big list
            for username in followersList:
                bigList.append(username)
            print("Added "+str(len(followersList))+" To Big List. Now There Are A Total of "+str(len(bigList))+" Profiles To Be Cross Matched\n")

    
    # Read Target List
    # with open("target_list.txt") as file:
    #     targetList = [line.rstrip() for line in file]
    #     print("Total in Target List: "+str(len(targetList)))    
    
    # for target in targetList:
    #     with open(target+".txt") as file:
    #         follows = [line.rstrip() for line in file]
    #         all_lists.append(follows)
    #         print("Total in Follows List: "+str(len(follows)))

    # print("Total Objects in All Lists: "+str(len(all_lists)))  
    # #print(len(all_lists[3]))  
    # l1=["a-1", "b-1", "c-1", "d-1", "e-1"]
    # l2=["a-2", "b-1", "c-2", "d-2", "e-1"]
    # l3=["a-3", "b-1", "c-3", "d-3", "e-1"]
    # l4=["a-4", "b-1", "c-4", "d-4", "e-1"]
    # l5=["a-5", "b-1", "c-5", "d-5", "e-1"]
    
    # print("Data About 'all lists variable':%s\nList1 size: "+str(len(all_lists[0])))
    
    #all_lists = [ l1, l2, l3, l4, l5]

    result_set = set()
    if len(bigList)>1:
        result_set = set(bigList[0]).intersection(*bigList[1:]) 
    else:
        result_set = set(bigList[0])
    
    print(result_set)
    print("Matching Cariables: "+str(len(result_set)))

    # with open("matches.txt", 'a+') as filehandle:
    #     for follower in result_set:
    #         filehandle.write('%s\n' % follower)

def calculateIntersections(monitorMode,list):
    
    # Big list with all followers from all accounts
    bigList = []

    if not monitorMode:
        # Open folder, get files
        files,folderPath = openFolder()
    
        # Only Collect .txt files
        editedList = [x for x in files if ".txt" in x]

        # Access each List In The Folder
        for profileList in editedList:

            # open the list
            with open(folderPath+"/"+profileList) as file:
                
                # Read every username from file
                followersList = [line.rstrip() for line in file]
                print("Total in "+profileList.replace(".txt", "")+"'s followers: "+str(len(followersList)))

                # Put every user name in big list
                for username in followersList:
                    bigList.append(username)
                print("Added "+str(len(followersList))+" To Count List. Now There Are A Total of "+str(len(bigList))+" Profiles To Be Cross Matched\n")
        # Use Counter () To Get All Intersects
        print("%s\nStarting to Count All Matches In The Count List")

        matches = Counter(bigList)
        

        if(input("Would you like to write information to sheet? (y/n) ") == "y"):
            sheets.write_sheet(matches)
        else:
            print("Information Not Saved!")    

    if monitorMode:
        for i in list:
            bigList.append(i)

    


    
    

def getTopPercent():
    while True:
        try:
            percent = int(input('What percentage of the first joined users do you need? '))
            break
        except:
            print("That's not a valid option!")
     

    # Open folder, get files
    files,folderPath = openFolder()
    print(os.path.basename(os.path.normpath(folderPath))+"_first_"+str(percent)+"%")
    
    final_directory = os.path.join(folderPath, os.path.basename(os.path.normpath(folderPath))+"_first_"+str(percent)+"%")
    print(final_directory)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    
    # Only Collect .txt files
    editedList = [x for x in files if ".txt" in x]
    #print(editedList)
    

    for profileList in editedList:
        
        # НУЖНО ПОФИКСИТЬ ТОП % ЮЗЕРОВ!!!
        with open(folderPath+"/"+profileList) as file:
            followersList = [line.rstrip() for line in file]
            print("Total in "+profileList.replace(".txt", "")+"'s followers: "+str(len(followersList)))

            firstList = followersList[int(len(followersList) * 0) : int(len(followersList) * (percent/100))]

            # Write Followers to file
            with open(final_directory+"/"+profileList+"_first_"+str(percent)+"%"+".txt", 'w+') as filehandle:
                for follower in firstList:
                    filehandle.write('%s\n' % follower)   



def openFolder():
    root = tk.Tk()
    root.withdraw()
    askDir = askdirectory(title='Select Folder')
    print(askDir)
    files = os.listdir(askDir)
    return files,askDir
   
def openFile():
    root = tk.Tk()
    root.withdraw()

    filePath = filedialog.askopenfilename()

    return filePath

def monitorList():

    while True:
        dateToday = formatDate(date.today())
        dateYest = formatDate(date.today() - timedelta(days = 1))
        # Read Parse List
        with open("parse_following_list.txt") as file:
            watchList = [line.rstrip() for line in file]
            print("Total Profiles In Watch List: "+str(len(watchList)))

        followingInfo = getFollowing(True)
        print(followingInfo)
       
        newFollowsList = []

        print(followingInfo)

        
        
        watchList = followingInfo


    
        for i,username in enumerate(watchList):
            print("i is: "+str(i))
            print(len(followingInfo))
            with open("Monitor/"+username+"_"+dateToday+".txt", 'w+') as filehandle:
                    for user in followingInfo[i]:
                            filehandle.write('%s\n' % user) 

            
            yestList = []

           


            if(os.path.exists("Monitor/"+username+"_"+dateYest+".txt")):
                with open("Monitor/"+username+"_"+dateYest+".txt") as file:
                    yestList = [line.rstrip() for line in file]
                    print("Total Profiles In Yesterday's List: "+str(len(yestList))) 
                
            
                newFollows = list(set(yestList) - set(followingInfo[i])) + list(set(followingInfo[i]) - set(yestList))
                #print(newFollows)
                
                sheets.monitorSheet(username, newFollows, dateToday)  



                    
                if not len(newFollows) == 0:
                    tg_bot.reportNewFoll(username, newFollows)
                    for acc in newFollows:
                        newFollowsList.append(acc)
                    time.sleep(10)
            else:
                print("No file from Yesterday. Wait 24 hrs.")
        
        matches = Counter(newFollowsList)
        sortMatch = Counter({k: c for k, c in matches.items() if c >= 2})
        singleMatch = Counter({k: c for k, c in matches.items() if c == 1})
        sortMatch = sortMatch.most_common()
        singleMatch = singleMatch.most_common()
        
        tg_bot.writeSingle(singleMatch)
        tg_bot.writeTotal(sortMatch)

        print("Sleep 24 hours")
        time.sleep(86400)

   

def formatDate(dateString):
    formatted_date = date.strftime(dateString, "%m-%d-%Y")
    return(formatted_date)

#calculateIntersections(False,[])
#compareLists()

#getListIntersect()

#"""getFollowing("1142993282659696640")"""

#timetest()
#monitorList()
#print(getFollowing(True))
#getTopPercent()
#getFollowers()
#getFollowing(False)
#calculateIntersections()

#monitorList()
#openFile()
#compareLists()
