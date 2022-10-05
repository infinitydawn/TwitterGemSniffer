import telebot
import textwrap
import time


API_KEY = "5345795883:AAGD2PIlg7Bqq_IEt1CIuGzmmgExOmOomDQ"
bot = telebot.TeleBot(API_KEY)

def reportNewFoll(username, subs):
    try:
        followers = ""
        for i in subs:
            followers +=  "https://twitter.com/"+i+"\n"

        message = username+' (https://twitter.com/'+username+') '+" followed "+str(len(subs))+" accounts today.\n"+followers
        #bot.send_message("@twittergemsmonitor",message)
        sendMsgFormated(message)
    except Exception as e:
        print(e)

def writeTotal(Matches):
    try: 
        message = 'Matches Between Accounts:\n\n'
        if len(Matches)>0:
            for val in Matches:
                message += 'https://twitter.com/'+val[0]+" - "+str(val[1])+"\n"
        else:
            message+="There weren't any matches today :("
        
        message+="\n\n#total"

        #bot.send_message("@twittergemsmonitor",message)
        sendMsgFormated(message)
    except Exception as e:
        print(e)

def writeSingle(Matches):
    try: 
        message = 'Single Mentions:\n\n'
        if len(Matches)>0:
            for val in Matches:
                message += 'https://twitter.com/'+val[0]+" - "+str(val[1])+"\n"
        else:
            message+="There weren't any single matches today :("
        
        message+="\n\n#single"
        
        sendMsgFormated(message)
    
    except Exception as e:
        print(e)


def sendMsgFormated(string):
    chunks = textwrap.wrap(string, width=4050,replace_whitespace=False)
    for i in chunks: 
        bot.send_message("@twittergemsmonitor",i)
        time.sleep(5)

# n = ["a","a","1","2","3","4","5","11","11"]
# writeSingle(n)
# subs = ''
# followers = ["1","2","3","4"]
# for i in followers:
#     subs +=  "https://twitter.com/"+i+"\n"

# print(subs)
#reportNewFoll("test_name", ["1","2","3","4","4"])
#writeTotal([('dung_beetle4013', 3), ('tarumi_kei', 2)])