import urllib.request
import requests
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import os
import shutil
import numpy as np

PARENT_DIR = "pages"
pages_crawled = []

#if the parent directory already there, we will delete it
if os.path.exists(PARENT_DIR):
	shutil.rmtree(PARENT_DIR)#os.rmdir(PARENT_DIR)

os.mkdir(PARENT_DIR) #parent directory
os.chdir(PARENT_DIR) #change directory so that we are inside the parent directory
print("Created parent directory ", PARENT_DIR)
n=1

def visit_url(url):
    global crawler_backlog
    if (len(crawler_backlog) > 100):
        return
    if (url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1

    try:
        page = urllib.request.urlopen(url)
        code = page.getcode()
        if (code == 200):
            n=1
            content = page.read()
            content_string = content.decode("utf-8")
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            regexp_title = re.compile('<title>(?P<title>(.*))</title>')
            links = soup.find_all('a', {'href': re.compile('^\/newhaven\/((?!:).)*$')})
            for link in links:
                if 'href' in link.attrs:
                    if link['href'].startswith('/wiki') and ':' not in link['href']:
                        if link['href'] not in pages_crawled:
                            new_link = f"http://www.newhaven.edu/{link['href']}"
                            pages_crawled.append(link)
                            try:
                                dir_name = {soup.title.text}
                                os.mkdir(str(dir_name))
                                os.chdir(str(dir_name))
                                with open("link_{}.txt".format(n), "w") as file:
                                    file.write(f'{soup.h1.text}; : {link["href"]}\n')
                                os.chdir("..")
                                visit_url(new_link)
                            except:
                                continue
            for (new_link) in re.findall(str(links), content_string):
                if (new_link not in crawler_backlog or crawler_backlog[new_link] != 1):
                    crawler_backlog[new_link] = 0

    except URLError as e:
        print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed] = 0

visit_url(seed)