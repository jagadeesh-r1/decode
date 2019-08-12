import cv2
import os
import base64
import sys
def load_and_convert(folder):
	print(folder)
	counter = 1
	for filename in os.listdir(folder):
		print(filename)
		img = cv2.imread(os.path.join(folder,filename))
		img = open(folder+'/'+filename,'rb')
		img = img.read()
		os.remove(folder + '/' +filename)
		if img is not None:
			img = base64.decodestring(img)
			#cv2.imwrite(filename,img)
			filename = filename.split('_')[0]
			filename = open(folder+'/'+filename+'_'+ str(counter)  +'.jpg','wb')
			counter  = counter + 1
			filename.write(img)
			print(filename)

def main():
	foldername=sys.argv[1]
	load_and_convert(foldername)

if __name__=="__main__":
	main()
