import os,sys
#ls *.mp3|xargs python renameFiles.py
fileNames = sys.argv[1:]

for fileName in fileNames:
	newfileName = fileName.replace(".mp3","").lower()
	os.rename(fileName, newfileName)
