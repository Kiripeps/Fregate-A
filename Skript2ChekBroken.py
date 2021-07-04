import os
from hashlib import sha256
def fileResume(fn):
    import ftplib
    ftp = ftplib.FTP('v4rts.beget.tech')
    ftp.login('v4rts_test','1234Bb!')
    ftp.cwd('Fba')
    needFile = os.path.join("E:\\Files",fn)
    file = open(needFile, 'wb')
    ftp.retrbinary('RETR ' + fn, file.write)
    ftp.quit()
def makeFileArray(path, fileNameArray):
    fileArray = []
    for file in fileNameArray:
        fileArray.append(os.path.join(path, file))
    return fileArray
def chekSum():
    sha256Make = []
    sha256Download = []
 
    fileArray = makeFileArray("E:\Files", os.listdir("E:\Files"))

    for file in fileArray:
        with open(file, "r") as f:
            fRead = f.read()
            sha256Make.append(sha256(fRead.encode('utf-8')).hexdigest())

    for i in range(0, len(os.listdir("E:\Files"))):
       sha256Make[i] = sha256Make[i] + " " + os.listdir("E:\Files")[i]

    fileArray2 = makeFileArray("E:\FilesSha", os.listdir("E:\FilesSha"))
    
    for file in fileArray2:
        with open(file, "r") as f:
            fRead = f.read()
            sha256Download.append(fRead)
        
    for i in range(0, len(sha256Make)):
        if(sha256Make[i] == sha256Download[i]):
            print("Great")
        else:
            print("Fall. Перезапись.")
            fileResume(os.listdir("E:\Files")[i])
chekSum()       

