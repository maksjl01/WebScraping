from bs4 import BeautifulSoup
from urllib import request
import requests as req
import argparse
import PIL 
import re
import os

parser = argparse.ArgumentParser(description="Find any image on the web")
parser.add_argument("--image", metavar='i', type=str, help="What kind of image you would like to download")
parser.add_argument("--size", metavar='s', type=int, help="0 - Small, 1 - Medium, 2 - Large")
parser.add_argument("--count", metavar='c', type=int, help="How many images you want to download")

args = parser.parse_args()

search = args.image
size = "s" if args.size == 0 else "m" if args.size == 1 else "l"
count = args.count

uri = "https://www.google.com/search?q={}&tbs=isz:{}&tbm=isch".format(search, size)

page = BeautifulSoup(req.get(uri).content, 'html.parser')
all_images = [img['src'] for img in page.find_all('img') if img['alt'] != 'Google']

image_names = 0

if not os.path.isdir(os.path.join(os.getcwd() + "\Images")):
    os.mkdir('Images')

for i in range(count):
    f = open("Images/" + str(image_names) + ".jpg", 'wb')
    f.write(request.urlopen(all_images[i]).read())
    f.close()
    image_names += 1
    count -= 1


