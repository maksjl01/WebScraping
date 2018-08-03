from bs4 import BeautifulSoup 
import requests as rq
import random
import webbrowser
import argparse
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}

DEPTH = 100

page = None

parser = argparse.ArgumentParser(description="Search the internet from one link")
parser.add_argument('--uri', metavar='u', type=str, help='Starting link')
parser.add_argument('--depth', metavar='d', type=int, help=('How deep do you wanna go'))

args = parser.parse_args()

START_URI = args.uri
DEPTH = args.depth

counter = 0

page = BeautifulSoup(rq.get(START_URI).content, 'html.parser')
start_a_tags = [link['href'] for link in page.find_all('a', attrs={'href': re.compile("^http://")})]
cur_link = random.choice(start_a_tags)

prev_page = page

try:
    for i in range(DEPTH):

        if counter % 2 == 0:
            counter = 0
            prev_page = page
        counter += 1

        page = BeautifulSoup(rq.get(cur_link).content, 'html.parser')
        a_tags = [link['href'] for link in page.find_all('a', attrs={'href': re.compile("^https://") })]
        
        if len(a_tags) > 0:
            cur_link = random.choice(a_tags)
        else:
            page = prev_page
            sa = [link['href'] for link in page.find_all('a', attrs={'href': re.compile("^http://")})]
            cur_link = random.choice(sa)
            DEPTH+=1

        print(cur_link)

    webbrowser.open(cur_link, new=2)
except IndexError as i:
    webbrowser.open(cur_link, new=2)









# a = BeautifulSoup(rq.get(START_URI).content, 'html.parser').find_all('a')
# aa = []
# for link in a:
#     if link.has_attr('href'):
#         if link['href'][0:4] == "http":
#             aa.append(link['href'])

# page = None

# def getalllinks(currentlk):
#     return [x['href'] for x in BeautifulSoup(rq.get(currentlk).content, 'html.parser').find_all('a') if x.has_attr('href') and x['href'][0:4] == "http"]

# def search(length):
#     currentlink = random.choice(aa)
#     prevlink = currentlink
#     for i in range(length):
#         all_links = getalllinks(currentlink)
#         currentlink = None
#         if len(all_links) > 0:
#             currentlink = random.choice(all_links)
#         else:
#             these = getalllinks(prevlink)
#             currentlink = random.choice(these)
#         prevlink = currentlink
#         print(currentlink)

# search(25)
        

# def find_all_links(uri):
#     try:
#         page = rq.get(uri, headers=headers)
#         try:
#             if "text/html" in page.headers['Content-Type']:
#                 soup = BeautifulSoup(page.content, 'html.parser')
#                 a = soup.find_all('a')
#                 links = []
#                 for link in a:
#                     if link.has_attr('href'):
#                         if link['href'][0:7] == "http://" or link['href'][0:8] == "https://":
#                             links.append(link['href'])
#                 return links
#             else:
#                 raise Exception("Not html")
#         except Exception:
#             print("Not html")
#     except TimeoutError:
#         print("timed out")

# def go_depth(depth):
#     first_a = find_all_links(START_URI)
#     a = random.choice(first_a)
#     prev_links = [START_URI]
#     prev_a = None

#     for i in range(depth):
#         c = None
#         prev_a = a
#         try:
#             c = find_all_links(a)
#         except Exception:
#             c = find_all_links(prev_a)

#         if len(c) > 0:
#             prev_links = c
#             a = random.choice(c)
#             print(a)
#         else:
#             c = find_all_links(prev_links)
#             a = random.choice(c)
#             print(a)
#     return a
            
# final_tag = go_depth(20)
# webbrowser.open(final_tag, new=2)
    




    