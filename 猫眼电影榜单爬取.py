import requests
from fake_useragent import UserAgent
from lxml import etree

url='https://maoyan.com/board'
headers={
    "User-Agent":UserAgent().chrome
}

response=requests.get(url,headers=headers)
# print(response.text)
e=etree.HTML(response.text)
names=e.xpath('//p[@class="name"]/a/text()')
stars=e.xpath('//p[@class="star"]/text()')
scores=e.xpath('//p[@class="score"]')
scores_movie=[]
for s in scores:
    score_movie=s.xpath('string(.)')
    scores_movie.append(score_movie)
relestimes=e.xpath('//p[@class="releasetime"]/text()')
infos=[]
for name,star,score,relestime in zip(names,stars,scores_movie,relestimes):
    infos.append(name+star.strip()+score+relestime)
with open('猫眼榜单电影.txt','w',encoding='utf-8') as f:
    for info in infos:
        f.write(info+'\n')
