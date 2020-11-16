
import os
import sys
import time 
from datetime import datetime as dt 
 
os.system("cls")

print ("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print ("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print ("''''''''''''''''''''''Website Blocker'''''''''''''''''''''''''''''''")
print ("''''''''''''''''Author : Rahat Khan Tusar(RKT)''''''''''''''''''''''")
print ("''''''''''''''Github : https://github.com/r3k4t'''''''''''''''''''''")
print ("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''") 
print ("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
# change hosts path according to your OS 
hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
# localhost's IP 
redirect = "127.0.0.1"
  
# websites That you want to block
 
web_list=["facebook.com","https://facebook.com"]

while True: 
  
    # time of your work 
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): 
        print("WORKING HOURS...") 
        with open(hostsPath, 'r+') as file: 
            content = file.read() 
            for website in web_list: 
                if website in content: 
                    pass
                else: 
                    # mapping hostnames to your localhost IP address 
                    file.write(redirect + " " + website + "\n") 
    else: 
        with open(hostsPath, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in web_list): 
                    file.write(line) 
                    
  
            # removing hostnmes from host file 
            file.truncate() 
  
        print("FUN TIME...") 
    time.sleep(2)
    
