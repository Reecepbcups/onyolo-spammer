# Reecepbcups#3370 - May/23/19
# onyolo snapchat 3rd party spambot
import requests, json, time
import string, random

print('''              _                                 
             | |                                
  _   _  ___ | | ___  ___ _ __   __ _ _ __ ___  
 | | | |/ _ \| |/ _ \/ __| '_ \ / _` | '_ ` _ \ 
 | |_| | (_) | | (_) \__ \ |_) | (_| | | | | | |
  \__, |\___/|_|\___/|___/ .__/ \__,_|_| |_| |_|
   __/ |                 | |                    
  |___/   Reecepbcups    |_|\n\n''')


convoLinkID = input("Link ID (ex. lp6BILEY0Q): ")
usermessage = input("Enter the message you want to spam: ")
numOfTimes = input("Number of times to send the message: ")

def newCookie():
    '''Generates a new, random cookie every iteration of the spam bot'''
    cookie = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
    return cookie

headers = {
    'Connection': 'keep-alive','content-length': '50',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': f"popshow-temp-id={newCookie()}", 
    'Host': 'onyolo.com','Origin': 'http://onyolo.com',
    'Referer': f"http//onyolo.com/{convoLinkID}",
    # Spoofing as a Samsung Smart TV
    'User-Agent': 'Mozilla/5.0 (Linux; Tizen 2.3) AppleWebKit/538.1 (KHTML, like Gecko)Version/2.3 TV Safari/538.1'
}

# Don't touch the payload
payload = {"text":f"{usermessage}","cookie":f"{newCookie()}"} 

for iteration in range(int(numOfTimes)):
    r = requests.post(f"http://onyolo.com/{convoLinkID}/message", data=json.dumps(payload), headers=headers)
    print(f"Message #{str(iteration+1)} sent")

print("All messages have been sent... Closing in 10 seconds")
time.sleep(10)
