from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login()
ftp.cwd('download') #replace with your directory
ftp.retrlines('LIST')

def uploadFile():
 filename = 'source.txt' #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = 'mantap.txt' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

#uploadFile()
downloadFile()