
[![python](https://img.shields.io/badge/python-cyan.svg)](https://www.python.org/)
[![OS](https://img.shields.io/badge/Tested%20On-WindowsCmd-cyan.svg)])(https://en.wikipedia.org/wiki/Cmd.exe)

# Windows Website Blocker(WWB)

### Author : RKT ###

### Description ###


![maxresdefault](https://user-images.githubusercontent.com/69615463/99218498-a3e90300-2800-11eb-818c-66ccefb30e6c.jpg)


Block Adult or Unwanted Websites on windows.It is a easy  way to block adult website.Adult websites are dangerous for our young generation.I want to stop it.


# Script(Conecpt) 


import os
<br>
import sys
<br>
import time
<br> 
from datetime import datetime as dt 
 <br>
os.system("cls")
<br>
### change hosts path according to your OS ###
 <br>
hostsPath = r"C:\Windows\System32\drivers\etc\hosts"

### localhost's IP ### 
<br>
redirect = "127.0.0.1"
 <br>
### websites That you want to block ###
 <br>
web_list=["facebook.com","https://facebook.com"]
<br>
while True: 
  <br>
    # time of your work
     <br> 
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        <br> 
        print("WORKING HOURS...")
        <br> 
        with open(hostsPath, 'r+') as file:
            <br> 
            content = file.read() 
            <br>
            for website in web_list:
                <br> 
                if website in content:
                   <br> 
                    pass
                    <br>
                else: 
                  <br>
                  ### mapping hostnames to your localhost IP address ###
                    <br> 
                    file.write(redirect + " " + website + "\n")
                    <br> 
    else:
    <br> 
        with open(hostsPath, 'r+') as file:
             <br> 
            content=file.readlines()
            <br> 
            file.seek(0)
            <br> 
            for line in content:
                <br> 
                if not any(website in line for website in web_list):
                    <br> 
                    file.write(line) 
                    <br>                      
            # removing hostnmes from host file 
            <br>
            file.truncate() 
            <br>
        print("FUN TIME...")
           <br> 
    time.sleep(2)

### Tested On Facebook ###

![Screenshot at 2020-11-15 12-17-41](https://user-images.githubusercontent.com/69615463/99219052-da734d80-2801-11eb-9cc2-fbab8ece513a.png)


