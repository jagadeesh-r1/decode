import os
import sys
from PIL import Image

def resize_img(img_addr):
    print(img_addr)
    size = 500,500
    image = Image.open(img_addr[:-1])
    image = image.resize((size),Image.NEAREST)
    image.save(img_addr[:-1],"JPEG")
    print(image.size)


def main():
    i = 1
    level_count =0
    while(level_count<1):
        level_count +=1
        print(sys.argv[i])
        list_file = open(sys.argv[i],'rb')
        #print(list_file.readline())
        while True:
            addr = list_file.readline()
            if not addr:
                break
            l = addr.decode("utf-8")
            print(l)
            try:
                resize_img(l)
            except:
                pass
        i = i + 1
        list_file.close()
if __name__ == '__main__':
    main()


