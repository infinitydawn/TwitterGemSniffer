import tweepy
import os
from collections import Counter






client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAIwbZwEAAAAA6MswMrUpRfqSFzjWvabbIOfYRX8%3Di7eUwoqby9C9gpkFNcXOInK7Y4dHbCU1lkKylYhOWO7ZuaJdI2',wait_on_rate_limit=True)



def getFollowers():
    # account usernames to parse
    parseList = ['dung_beetle4013',"tarumi_kei","cy_nakhaue",'candcfx']

    resultList = []

    for profile in parseList:
        # Convert Username To a Numeric ID
        id = client.get_user(username=profile).data.id

        usersFollowers = []

        
        for user in tweepy.Paginator(client.get_users_followers, id=id, max_results="1000").flatten():
            usersFollowers.append(user.username)
    
        resultList.append(usersFollowers)
    
    return resultList    

parseList = ['candcfx','churka','dung_beetle4013','dung_beetle4013','dung_beetle4013',"tarumi_kei","tarumi_kei","cy_nakhaue",'1a','2b','3c']

def counterTest(list):
    matches = Counter(list)
    
    comm = Counter({k: c for k, c in matches.items() if c >= 2})
    comm = comm.most_common()
    #comm.pop(len(comm-1))
    print(comm)
    for val in comm:
        print(val[0]+" - "+str(val[1]))
        if val[1]==1:
            comm.remove(val)
        #print(val[0]," - ", val[1])
    #print(comm)
    print("New comm is: "+str(comm))
#print(getFollowers())

counterTest(parseList)