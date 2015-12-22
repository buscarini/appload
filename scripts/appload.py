#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ftplib import FTP
import os
import sys
import keyring

def uploadFiles(ftp,files):
    for file in files:
        name = os.path.basename(file)        
        if not os.path.exists(file):
            exit("Error: file " + file + " doesn't exist")
        
        if os.path.isdir(file):
            print "mkdir " + name
            remoteFiles = map(str.upper,ftp.nlst())
            if not name.upper() in remoteFiles and name!="/":
                ftp.mkd(name)

            ftp.cwd(name)
            
            children = os.listdir(file)
            subfiles = []
            for child in children:
                subfiles.append(os.path.join(file,child))    

            uploadFiles(ftp,subfiles)
            
            ftp.cwd("..")
        else:    
            print "upload " + file
            ftp.storbinary(('STOR ' + name).encode('utf-8'), open(file, 'rb'))
    

if len(sys.argv)<5:
    sys.exit('Usage: %s "keychain service" "keychain account" "server" "port" "remote path" "file 1" "file 2" … "file n"' % sys.argv[0])
    
params = sys.argv[1:]
service = params.pop(0)
account = params.pop(0)
server = params.pop(0)
port = params.pop(0)
path = params.pop(0)
files = params

password = keyring.get_password(service, account)
if password == None:
    print("FTP Password not found.")
    while password == None or len(password)==0:
        password = str(raw_input("Please enter the password for service \""+service+"\" and account \""+account+"\": "))
    keyring.set_password(service, account, password)
    
if password==None:
    sys.exit("Please create the password first or allow access for service: " + service + " account " + account)

print "connect to server " +  server + " port " + port
ftp = FTP()
ftp.connect(server,port)
ftp.login(account,password)
ftp.cwd('/')

if path.endswith("/"):
    path = path[:-1]

folders = []
while 1:
    path, folder = os.path.split(path)
    if folder != "":
        folders.append(folder)
    else:
        if path != "":
            folders.append(path)
        break
        
folders.reverse()
folders = filter(lambda x: x!="/",folders)

for folder in folders:
    remoteFiles = map(str.upper,ftp.nlst())
    if not folder.upper() in remoteFiles:
        print "mkdir " + folder
        ftp.mkd(folder)
        
    ftp.cwd(folder)


uploadFiles(ftp,files)

    
ftp.quit()