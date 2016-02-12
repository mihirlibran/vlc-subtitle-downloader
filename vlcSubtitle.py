import os
import hashlib
import subprocess
import sys
import urllib2

def getHash(fileName):
	'''This hash function receives the name of the file and returns the hash code '''
	readSize=64 * 1024
	with open(fileName, 'rb') as f:
		data=f.read(readSize)
		f.seek(-readSize,os.SEEK_END)
		data+= f.read(readSize)
	return hashlib.md5(data).hexdigest()

def getSubtitle(fileName):
	hashcode=getHash(fileName)
	#print("Hashcode:"+hashcode)
	extensions=[".flv",".avi",".mov",".mp4",".mpg",".mpeg","wmv",".mkv"]
	for extension in extensions:
		if extension in fileName:
			fileName=fileName.replace(extension,"")
	#print(fileName)
	subtitleFileName=fileName+".srt"
	subtitleFile=open(subtitleFileName,"wb")
	headers={"User-agent":"SubDB/1.0 (vlc-subtitle-downloader/1.0; https://github.com/mihirlibran/vlc-subtitle-downloader)"}
	url="http://api.thesubdb.com/?action=download&hash="+hashcode+"&language=en"
	#print(url)
	request=urllib2.Request(url,None,headers)
	response=urllib2.urlopen(request)
	subtitleFile.write(response.read())
	subtitleFile.close()
	

vlcPath=os.path.join("C:/","Program Files (x86)","VideoLAN","VLC","vlc.exe")
#videoPath="\\E:\TV SHOWS\\CASTLE SEASON 1\\Castle [1x01] Flowers for Your Grave.mkv"
#print(vlcPath)

fileName=sys.argv[1]
getSubtitle(fileName)

#p=subprocess.Popen([vlcPath,videoPath])