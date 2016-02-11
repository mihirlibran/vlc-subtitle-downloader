import os
import hashlib
import subprocess
import sys

def getHash(fileName):
	'''This hash function receives the name of the file and returns the hash code '''
	readSize=64 * 1024
	with open(fileName, 'rb') as f:
		data=f.read(readSize)
		f.seek(-readSize,os.SEEK_END)
		data+= f.read(readSize)
	return hashlib.md5(data).hexdigest()

vlcPath=os.path.join("C:/","Program Files (x86)","VideoLAN","VLC","vlc.exe")
#videoPath="\\E:\TV SHOWS\\CASTLE SEASON 1\\Castle [1x01] Flowers for Your Grave.mkv"
print(vlcPath)

fileName=sys.argv[1]
hashcode=getHash(fileName)
print(hashcode)

#p=subprocess.Popen([vlcPath,videoPath])