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
	'''This function downloads the subtitle file '''
	hashcode=getHash(fileName)
	extensions=[".flv",".avi",".mov",".mp4",".mpg",".mpeg","wmv",".mkv"]
	for extension in extensions:
		if extension in fileName:
			fileName=fileName.replace(extension,"")
	subtitleFileName=fileName+".srt"
	if not os.path.exists(subtitleFileName):
		subtitleFile=open(subtitleFileName,"wb")
		headers={"User-agent":"SubDB/1.0 (vlc-subtitle-downloader/1.0; https://github.com/mihirlibran/vlc-subtitle-downloader)"}
		url="http://api.thesubdb.com/?action=download&hash="+hashcode+"&language=en"
		request=urllib2.Request(url,None,headers)
		response=urllib2.urlopen(request)
		subtitleFile.write(response.read())
		subtitleFile.close()
	

vlcPath=os.path.join("C:/","Program Files (x86)","VideoLAN","VLC","vlc.exe")

fileName=sys.argv[1]

try:
	getSubtitle(fileName)
	print("Subtitles downloaded")
except:
	print("Subtitles unavailable")

p=subprocess.Popen([vlcPath,fileName])