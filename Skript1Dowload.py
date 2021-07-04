def ftpDownload(workDir, path):
    import ftplib
    import os
    
    ftp = ftplib.FTP('v4rts.beget.tech')
    ftp.login('v4rts_test','1234Bb!')
    ftp.cwd(workDir)
    filenames = ftp.nlst()
    
    print("Пример пути X:\\Xxxx")
    #path = input("Введите путь к папке для сохранения: ")
    
    if os.path.exists(path):
        print("Указанная папка существует")
    else:
        print("указанная папка не существует")
        os.mkdir(path)
    
    listDownloadFile = os.listdir(path)
    if(listDownloadFile == []):
        fileRecording(filenames[0], filenames, ftp, path)
    else:
        name = listDownloadFile[-1]
        if(name == filenames[-1]):
            print("Все значения скачаны")
        else:
            fileRecording(name, filenames, ftp, path)
    ftp.quit()
    
def fileRecording(filename, filenames, ftp, path):
    import ftplib
    import os
    for filename in filenames:
        host_file = os.path.join(path, filename)
        try:
            with open(host_file, 'wb') as local_file:
                ftp.retrbinary('RETR ' + filename, local_file.write)
        except ftplib.error_perm:
            pass
    
ftpDownload('FbaSha', "E:\FilesSha")
ftpDownload('Fba', "E:\Files")
