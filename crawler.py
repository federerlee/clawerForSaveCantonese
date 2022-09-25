from bs4 import BeautifulSoup
import requests
import re
import json
import time
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from google.colab import drive
drive.mount('/content/gdrive')


def saveImages(url_images,filename):  
    try:
        if url_images.find('http') or url_images.find('https'):
            print('http or https found')
            r = requests.get(url_images, stream=True) #Get request on full_url
            if r.status_code == 200:                     #200 status code = OK
                with open(filename, 'wb') as f: 
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                    print('download image')
                    return 'image files saved'
            else:
                return 'image files saved fail'
    except:
        print(str(Exception))
        print('caught')



url_base='https://news.mingpao.com/pns/%e5%89%af%e5%88%8a/article/20210131/s00005/1612031463219/%7b%e5%ae%88%e8%ad%b7%e7%b2%b5%e8%aa%9e%e9%81%94%e4%ba%ba%7d%e5%bc%b5%e9%8c%ab%e8%8e%89-%e5%ae%88%e8%ad%b7%e7%b2%b5%e8%aa%9e-%e5%ae%88%e8%ad%b7%e7%a7%bb%e6%b0%91%e5%be%8c%e4%bb%a3%e7%9a%84%e5%b0%8a%e5%9a%b4'
page=requests.get(url_base)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#print('list of children:')
#print(list(soup.children))


#print('type of list soup.children')
#for item in list(soup.children):
#    print(type(item))
    #print('contents of item:')
    #print(item)
 


#for i in list(soup.children):
#    html=i.replace_with_children
#    print('type of html')
#    print(type(html))
    #if type(html) is'bs4.element.NavigableString':
       # print('html from soup children')
        #print(html)
ptags=soup.find_all('p')
print('ptags:')
print(ptags)

titletags=soup.find_all('title')
print('title:')
print(titletags)

pselect=soup.select("div p")
print('p select')
print(pselect)

#imagetags=soup.find_all('img', alt=True)
#for i in imagetags:
#    imagetitle=i.select('alt')
#    print('image alt caption:')
#    print(i['alt'])

filename='/content/gdrive/My Drive/photoes_sharedwithAnya/'

imaglazy=soup.find_all('img',class_='lazy')
print('imag lazy')
print(imaglazy)
n=0
for i in imaglazy:
    #print(i.attrs['alt'])
    image_src=i.attrs['src']
    print(n,'th image attrs:')
    print(image_src)
    print(n, 'th data-original url:')
    print(i['data-original'])
    n=n+1
    filenames=filename+str(n)+'.jpg'
    if i['data-original'].find('http') or i['data-original'].find('https'):
        print('http or https found')
    retrunmessages=saveImages(i['data-original'],filenames)
    print(retrunmessages)


imagesource=soup.find('data-original')
print('image source original')
print(imagesource)
#url_image=url_base+image_src
url_image='https://fs.mingpao.com/pns/20210131/s00125/4dea407fd3f8ae06c18689bb79dfeecd.jpg'

#for link in soup.select("img[src^=https]"):
#        lnk = link["src"]
#        print('link url:')
#        print(lnk)
#        r = requests.get(lnk, stream=True) #Get request on full_url
        #with open(basename(lnk)," wb") as f:
        #    f.write(requests.get(lnk).content)





