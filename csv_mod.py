import csv

Name = "sanya"
users = "20"
matches = "10"
path = "C:/Users/AMD/Desktop/Misha Web Dev Projects/Twitter Scraper/etopchik"
target = "lesha"

def write_csv_Compare(name, users,matches,path,target):
    while True:
        try:
            open(path+'.csv', 'r', newline='')
            with open(path+'.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                #writer.writerow(["Username", "User_Count", "Matches", "Target Account: "+target])
                writer.writerow([name, users, matches])
                break
        except:
            print("File doesn't exist yet! Creating...")
            with open(path+'.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Username", "User_Count", "Matches", "Target Account: "+target])
                #writer.writerow([name, users, matches])




#write_csv_Compare(Name, users, matches,path,target)